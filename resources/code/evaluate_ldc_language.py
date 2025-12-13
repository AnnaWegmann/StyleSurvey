
"""
Evaluate LUAR-MUD embeddings on the LDC dataset using UMAP visualization.
This script generates embeddings for essays and visualizes them using UMAP.

Usage: 
    python evaluate_ldc_language.py --base_data_path <path_to_ldc_data>
"""

import argparse
import random
import os
import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
import umap
import matplotlib.pyplot as plt
from transformers import AutoModel, AutoTokenizer
from tqdm import tqdm

def load_txt_file(file_path: str) -> str:
    """Reads and returns the content of a text file."""
    with open(file_path, "r") as f:
        return f.read()

def load_data(base_data_path: str) -> list:
    """
    Loads data from the LDC dataset index file.
    
    Args:
        base_data_path (str): The path to the directory containing index.csv
        
    Returns:
        list: A list of dictionaries containing text content and language labels.
    """
    index_path = os.path.join(base_data_path, "index.csv")
    if not os.path.exists(index_path):
        raise FileNotFoundError(f"Index file not found at {index_path}")

    # Read the index CSV file
    df = pd.read_csv(
        index_path,
        names=["File", "Prompt", "Language", "Level"]
    )

    data = []
    # Iterate through the dataframe and load text content
    for _, row in df.iterrows():
        try:
            filename = row["File"]
            # Construct path to the original response file
            file_path = os.path.join(base_data_path, "responses", "original", filename)
            text = load_txt_file(file_path)
            language = row["Language"]
            record = {
                "text": text,
                "language": language,
            }
            data.append(record)
        except Exception as e:
            # Skip files that cannot be loaded
            continue
    
    return data

def make_episodes(
    data: list,
):
    """
    Groups texts by language and chunks them into episodes of fixed size.
    
    Args:
        data (list): List of data records.
        
    Returns:
        list: List of episodes, where each episode contains 'essays_per_embedding' texts.
    """
    essays_per_embedding = 5
    
    df = pd.DataFrame(data)
    # Group all texts by language
    df = df.groupby("language").agg(list).reset_index()
    
    # Create chunks of size `essays_per_embedding`
    df["text"] = df["text"].apply(lambda lst: [lst[i:i+essays_per_embedding] for i in range(0, len(lst), essays_per_embedding)][:-1])
    
    # Keep only text and language columns
    df = df[["text", "language"]]
    df.rename(columns={"language": "label"}, inplace=True)
    
    # Explode the list of episodes so each row is one episode
    ret = df.explode("text").to_dict("records")
        
    # Shuffle the episodes
    random.shuffle(ret)
    return ret

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Evaluate LUAR-MUD on LDC dataset with UMAP visualization.")
    parser.add_argument("--base_data_path", type=str, required=True, help="Path to the LDC data directory.")
    args = parser.parse_args()

    # Set random seed for reproducibility
    random.seed(42)
    np.random.seed(42)

    print(f"Loading data from {args.base_data_path}...")
    data = load_data(base_data_path=args.base_data_path)
    print(f"Loaded {len(data)} documents.")

    # Create episodes from the loaded data
    episodes = make_episodes(data)
    print(f"Created {len(episodes)} episodes.")
    labels = [ep["label"] for ep in episodes]
    
    print("Loading LUAR-MUD model...")
    # Load the pre-trained model and tokenizer
    model = AutoModel.from_pretrained("rrivera1849/LUAR-MUD", trust_remote_code=True)
    tokenizer = AutoTokenizer.from_pretrained("rrivera1849/LUAR-MUD", trust_remote_code=True)
    model.cuda()
    model.eval()

    embeddings = []
    print("Generating embeddings...")
    essays_per_embedding = 5
    
    # Generate embeddings for each episode
    for episode in tqdm(episodes):
        # Tokenize the texts in the episode
        inputs = tokenizer(
            episode["text"],
            max_length=512,
            padding="max_length",
            truncation=True,
            return_tensors="pt",
        )
        inputs.to(model.device)
    
        # Reshape inputs to match model expectation (batch_size, num_essays, seq_len)
        # Here batch_size is 1
        inputs["input_ids"] = inputs["input_ids"].reshape(1, essays_per_embedding, 512)
        inputs["attention_mask"] = inputs["attention_mask"].reshape(1, essays_per_embedding, 512)
        
        with torch.no_grad():
            # Get embeddings from the model
            emb = model(**inputs)
            # Normalize embeddings
            emb = F.normalize(emb, dim=-1)
        
        embeddings.append(emb)

    # Prepare data for UMAP
    print("Running UMAP visualization...")
    X = torch.cat(embeddings, dim=0).cpu().numpy()
    labels_np = np.array(labels)

    # Downsample if too many points to avoid clutter and save time
    max_points = 500   
    if len(X) > max_points:
        idx = np.random.choice(len(X), size=max_points, replace=False)
        X = X[idx]
        labels_np = labels_np[idx]

    # Fit UMAP with cosine metric
    mapper = umap.UMAP(metric="cosine")
    Z = mapper.fit_transform(X)

    # Okabe–Ito colorblind-friendly palette
    okabe_ito = [
        "#E69F00", # orange
        "#56B4E9", # sky blue
        "#009E73", # bluish green
        "#F0E442", # yellow
        "#0072B2", # blue
        "#D55E00", # vermillion
        "#CC79A7", # reddish purple
        "#999999"  # gray
    ]

    unique_labels = np.unique(labels_np)
    colors = [okabe_ito[i % len(okabe_ito)] for i in range(len(unique_labels))]

    # Plotting
    plt.figure(dpi=300, figsize=(6,4.2))
    for i, ulab in enumerate(unique_labels):
        idx = labels_np == ulab
        plt.scatter(
            Z[idx, 0], Z[idx, 1],
            c=colors[i],
            label=str(ulab),
            s=45,
            alpha=0.85,
            edgecolors="k",
            linewidth=0.3
        )

    plt.legend(title="Labels", bbox_to_anchor=(1.05, 1), loc="upper left")
    
    # Hide ticks and values for cleaner plot
    plt.xticks([])
    plt.yticks([])
    plt.gca().set_xticklabels([])
    plt.gca().set_yticklabels([])

    # Remove axis labels
    plt.xlabel("")
    plt.ylabel("")
    title = "Native Language Clustering"
    plt.title(f"{title}", fontsize=16)

    # Save the plot
    umap_savename = "NLI.png"
    plt.tight_layout()
    plt.savefig(umap_savename)
    plt.close()
    print(f"UMAP visualization saved to {umap_savename}")
    
    return 0

if __name__ == '__main__':
    main()
