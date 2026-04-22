## Papers and works from the Style Survey

*We welcome contributions via GitHub issues or pull requests to collect relevant style papers that are not mentioned in our survey.* Note that this list includes all references from our survey which includes works that might not be directly related to style or style representations. 

This page is intended to list the references from the Style Survey paper as a **sortable, searchable table**.

To filter the table, start typing in the search box below; click any column header to sort.

<input
  type="search"
  placeholder="Filter by title, author, year, venue…"
  data-table-filter="#papers-table"
  style="width: 100%; padding: 0.4rem; margin: 0.5rem 0;"
/>

<table id="papers-table">
  <thead>
    <tr>
      <th>Title</th>
      <th>Authors</th>
      <th>Link</th>
      <th>Year</th>
      <th>Venue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="has-tooltip"><em>Writeprints: A stylometric approach to identity-level identification and similarity detection in cyberspace</em><span class="tooltip">One of the problems often associated with online anonymity is that it hinders social accountability, as substantiated by the high levels of cybercrime. Although identity cues are scarce in cyberspace, individuals often leave behind textual identity traces. In this study we proposed the use of stylometric analysis techniques to help identify individuals based on writing style. We incorporated a rich set of stylistic features, including lexical, syntactic, structural, content-specific, and idiosyncratic attributes. We also developed the Writeprints technique for identification and similarity detection of anonymous identities. Writeprints is a Karhunen-Loeve transforms-based technique that uses a sliding window and pattern disruption algorithm with individual author-level feature sets. The Writeprints technique and extended feature set were evaluated on a testbed encompassing four online datasets spanning different domains: email, instant messaging, feedback comments, and program code. Writeprints outperformed benchmark techniques, including SVM, Ensemble SVM, PCA, and standard Karhunen-Loeve transforms, on the identification and similarity detection tasks with accuracy as high as 94% when differentiating between 100 authors. The extended feature set also significantly outperformed a baseline set of features commonly used in previous research. Furthermore, individual-author-level feature sets generally outperformed use of a single group of attributes.</span></span></td>
      <td>Ahmed Abbasi and Hsinchun Chen</td>
      <td><a href="https://dl.acm.org/doi/10.1145/1344411.1344413">link</a></td>
      <td>2008</td>
      <td>ACM Transactions on Information Systems (TOIS), 26(2):1–29</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Fine-grained Analysis of Sentence Embeddings Using Auxiliary Prediction Tasks</em><span class="tooltip">There is a lot of research interest in encoding variable length sentences into fixed length vectors, in a way that preserves the sentence meanings. Two common methods include representations based on averaging word vectors, and representations based on the hidden states of recurrent neural networks such as LSTMs. The sentence vectors are used as features for subsequent machine learning tasks or for pre-training in the context of deep learning. However, not much is known about the properties that are encoded in these sentence representations and about the language information they capture. We propose a framework that facilitates better understanding of the encoded representations. We define prediction tasks around isolated aspects of sentence structure (namely sentence length, word content, and word order), and score representations by the ability to train a classifier to solve each prediction task when using the representation as input. We demonstrate the potential contribution of the approach by analyzing different sentence representation mechanisms. The analysis sheds light on the relative strengths of different sentence embedding methods with respect to these low level prediction tasks, and on the effect of the encoded vector’s dimensionality on the resulting representations.</span></span></td>
      <td>Yossi Adi, Einat Kermany, Yonatan Belinkov, Ofer Lavi, and Yoav Goldberg</td>
      <td><a href="https://openreview.net/forum?id=BJh6Ztuxl">link</a></td>
      <td>2017</td>
      <td>ICLR</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Can Authorship Attribution Models Distinguish Speakers in Speech Transcripts?</em><span class="tooltip">Abstract Authorship verification is the task of determining if two distinct writing samples share the same author and is typically concerned with the attribution of written text. In this paper, we explore the attribution of transcribed speech, which poses novel challenges. The main challenge is that many stylistic features, such as punctuation and capitalization, are not informative in this setting. On the other hand, transcribed speech exhibits other patterns, such as filler words and backchannels (e.g., um, uh-huh), which may be characteristic of different speakers. We propose a new benchmark for speaker attribution focused on human-transcribed conversational speech transcripts. To limit spurious associations of speakers with topic, we employ both conversation prompts and speakers participating in the same conversation to construct verification trials of varying difficulties. We establish the state of the art on this new benchmark by comparing a suite of neural and non-neural baselines, finding that although written text attribution models achieve surprisingly good performance in certain settings, they perform markedly worse as conversational topic is increasingly controlled. We present analyses of the impact of transcription style on performance as well as the ability of fine-tuning on speech transcripts to improve performance.1</span></span></td>
      <td>Cristina Aggazzotti, Nicholas Andrews, and Elizabeth Allyn Smith</td>
      <td><a href="https://doi.org/10.1162/tacl_a_00678">link</a></td>
      <td>2024</td>
      <td>Transactions of the Association for Computational Linguistics, 12:875–891</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Content Anonymization for Privacy in Long-form Audio</em><span class="tooltip">Voice anonymization techniques have been found to successfully obscure a speaker&#x27;s acoustic identity in short, isolated utterances in benchmarks such as the VoicePrivacy Challenge. In practice, however, utterances seldom occur in isolation: long-form audio is commonplace in domains such as interviews, phone calls, and meetings. In these cases, many utterances from the same speaker are available, which pose a significantly greater privacy risk: given multiple utterances from the same speaker, an attacker could exploit an individual&#x27;s vocabulary, syntax, and turns of phrase to re-identify them, even when their voice is completely disguised. To address this risk, we propose a new approach that performs a contextual rewriting of the transcripts in an ASR-TTS pipeline to eliminate speaker-specific style while preserving meaning. We present results in a long-form telephone conversation setting demonstrating the effectiveness of a content-based attack on voice-anonymized speech. Then we show how the proposed content-based anonymization methods can mitigate this risk while preserving speech utility. Overall, we find that paraphrasing is an effective defense against content-based attacks and recommend that stakeholders adopt this step to ensure anonymity in long-form audio.</span></span></td>
      <td>Cristina Aggazzotti, Ashi Garg, Zexin Cai, and Nicholas Andrews</td>
      <td><a href="https://doi.org/10.48550/arXiv.2510.12780">link</a></td>
      <td>2025</td>
      <td>arXiv preprint ArXiv:2510.12780</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>The impact of automatic speech transcription on speaker attribution</em><span class="tooltip">Speaker attribution from speech transcripts is the task of identifying a speaker from the transcript of their speech based on patterns in their language use. This task is especially useful when the audio is unavailable (e.g. deleted) or unreliable (e.g. anonymized speech). Prior work in this area has primarily focused on the feasibility of attributing speakers using transcripts produced by human annotators. However, in real-world settings, one often only has more errorful transcripts produced by automatic speech recognition (ASR) systems. In this paper, we conduct what is, to our knowledge, the first comprehensive study of the impact of automatic transcription on speaker attribution performance. In particular, we study the extent to which speaker attribution performance degrades in the face of transcription errors, as well as how properties of the ASR system impact attribution. We find that attribution is surprisingly resilient to word-level transcription errors and that the objective of recovering the true transcript is minimally correlated with attribution performance. Overall, our findings suggest that speaker attribution on more errorful transcripts produced by ASR is as good, if not better, than attribution based on human-transcribed data, possibly because ASR transcription errors can capture speaker-specific features revealing of speaker identity.</span></span></td>
      <td>Cristina Aggazzotti, Matthew Wiesner, Elizabeth Allyn Smith, and Nicholas Andrews</td>
      <td><a href="https://doi.org/10.48550/arXiv.2507.08660">link</a></td>
      <td>2025</td>
      <td>Transactions of the Association for Computational Linguistics, in press</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Neurobiber: Fast and Interpretable Stylistic Feature Extraction</em><span class="tooltip">Linguistic style is pivotal for understanding how texts convey meaning and fulfill communicative purposes, yet extracting detailed stylistic features at scale remains challenging. We present Neurobiber, a transformer-based system for fast, interpretable style profiling built on Biber&#x27;s Multidimensional Analysis (MDA). Neurobiber predicts 96 Biber-style features from our open-source BiberPlus library (a Python toolkit that computes stylistic features and provides integrated analytics, e.g., PCA and factor analysis). Despite being up to 56 times faster than existing open source systems, Neurobiber replicates classic MDA insights on the CORE corpus and achieves competitive performance on the PAN 2020 authorship verification task without extensive retraining. Its efficient and interpretable representations readily integrate into downstream NLP pipelines, facilitating large-scale stylometric research, forensic analysis, and real-time text monitoring. All components are made publicly available.</span></span></td>
      <td>Kenan Alkiek, Anna Wegmann, Jian Zhu, and David Jurgens</td>
      <td><a href="https://doi.org/10.48550/arXiv.2502.18590">link</a></td>
      <td>2025</td>
      <td>arXiv preprint ArXiv:2502.18590</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>SmolLM2: When Smol Goes Big — Data-Centric Training of a Fully Open Small Language Model</em><span class="tooltip">Large language models, while groundbreaking, are computationally expensive and difficult to deploy in resource-constrained settings. To address this challenge, small language models have emerged, but their performance critically depends on the quality and composition of the pretraining datasets—yet many recent models, such as Qwen2.5-1.5B and Llama3.2-1B, remain opaque about their training data, limiting reproducibility and scientific understanding. In this paper, we document and publicly release SmolLM2, a fully transparent state-of-the-art ``small&#x27;&#x27; (1.7 billion parameter) language model (LM), along with its training datasets and code. To attain strong performance, we overtrain SmolLM2 on 11 trillion tokens of data using a multi-stage training process that mixes web text with specialized math, code, and instruction-following data. We additionally curate and release new specialized datasets (FineMath, Stack-Edu, and SmolTalk) at stages where we found existing datasets to be problematically small or low-quality. To inform our design decisions, we perform both small-scale ablations and a manual refinement process that updates the dataset mixing rates at each stage based on the performance at the previous one. Ultimately, we demonstrate that SmolLM2 outperforms other recent small LMs including Qwen2.5-1.5B, Llama3.2-1B, and Falcon3-1.6B. By releasing our model, datasets, and code, we aim to facilitate future research on LM development as well as applications of small LMs.</span></span></td>
      <td>Team SmolLM, Loubna Ben Allal, Anton Lozhkov, Elie Bakouch, et al.</td>
      <td><a href="https://openreview.net/forum?id=3JiCl2A14H#discussion">link</a></td>
      <td>2025</td>
      <td>COLM</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Masks and mimicry: Strategic obfuscation and impersonation attacks on authorship verification</em><span class="tooltip">The increasing use of Artificial Intelligence(AI) technologies, such as Large LanguageModels (LLMs) has led to nontrivial improvementsin various tasks, including accurate authorshipidentification of documents. However,while LLMs improve such defense techniques,they also simultaneously provide a vehicle formalicious actors to launch new attack vectors.To combat this security risk, we evaluate theadversarial robustness of authorship models(specifically an authorship verification model)to potent LLM-based attacks. These attacksinclude untargeted methods - authorship obfuscationand targeted methods - authorshipimpersonation. For both attacks, the objectiveis to mask or mimic the writing style of an authorwhile preserving the original texts’ semantics,respectively. Thus, we perturb an accurateauthorship verification model, and achievemaximum attack success rates of 92% and 78%for both obfuscation and impersonation attacks,respectively.</span></span></td>
      <td>Kenneth Alperin, Rohan Leekha, Adaku Uchendu, Trang Nguyen, Srilakshmi Medarametla, Carlos Levya Capote, Seth Aycock, and Charlie Dagli</td>
      <td><a href="https://doi.org/10.18653/v1/2025.nlp4dh-1.10">link</a></td>
      <td>2025</td>
      <td>Proceedings of the 5th International Conference on NLP for Digital Humanities, pages 102–116</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Latent Space Interpretation for Stylistic Analysis and Explainable Authorship Attribution</em><span class="tooltip">Recent state-of-the-art authorship attribution methods learn authorship representations of text in a latent, uninterpretable space, which hinders their usability in real-world applications. We propose a novel approach for interpreting learned embeddings by identifying representative points in the latent space and leveraging large language models to generate informative natural language descriptions of the writing style associated with each point. We evaluate the alignment between our interpretable and latent spaces and demonstrate superior prediction agreement over baseline methods. Additionally, we conduct a human evaluation to assess the quality of these style descriptions and validate their utility in explaining the latent space. Finally, we show that human performance on the challenging authorship attribution task improves by +20% on average when aided with explanations from our method.</span></span></td>
      <td>Milad Alshomary, Narutatsu Ri, Marianna Apidianaki, Ajay Patel, Smaranda Muresan, and Kathleen McKeown</td>
      <td><a href="https://aclanthology.org/2025.coling-main.75/">link</a></td>
      <td>2025</td>
      <td>COLING, pages 1124–1135</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Layered Insights: Generalizable Analysis of Human Authorial Style by Leveraging All Transformer Layers</em><span class="tooltip">We propose a new approach for the authorship attribution task that leverages the various linguistic representations learned at different layers of pre-trained transformer-based models. We evaluate our approach on two popular authorship attribution models and three evaluation datasets, in in-domain and out-of-domain scenarios. We found that utilizing various transformer layers improves the robustness of authorship attribution models when tested on out-of-domain data, resulting in a much stronger performance. Our analysis gives further insights into how our model’s different layers get specialized in representing certain linguistic aspects that we believe benefit the model when tested out of the domain.</span></span></td>
      <td>Milad Alshomary, Nikhil Reddy Varimalla, Vishal Anand, Smaranda Muresan, and Kathleen McKeown</td>
      <td><a href="https://doi.org/10.18653/v1/2025.emnlp-main.521">link</a></td>
      <td>2025</td>
      <td>EMNLP, pages 10290–10303</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>The topic confusion task: A novel evaluation scenario for authorship attribution</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Malik Altakrori, Jackie Chi Kit Cheung, and Benjamin CM Fung</td>
      <td><a href="https://aclanthology.org/2021.findings-emnlp.359.pdf">link</a></td>
      <td>2021</td>
      <td>Findings of EMNLP 2021, pages 4242–4256</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Learning invariant representations of social media users</em><span class="tooltip">The evolution of social media users’ behavior over time complicates user-level comparison tasks such as verification, classification, clustering, and ranking. As a result, naive approaches may fail to generalize to new users or even to future observations of previously known users. In this paper, we propose a novel procedure to learn a mapping from short episodes of user activity on social media to a vector space in which the distance between points captures the similarity of the corresponding users’ invariant features. We fit the model by optimizing a surrogate metric learning objective over a large corpus of unlabeled social media content. Once learned, the mapping may be applied to users not seen at training time and enables efficient comparisons of users in the resulting vector space. We present a comprehensive evaluation to validate the benefits of the proposed approach using data from Reddit, Twitter, and Wikipedia.</span></span></td>
      <td>Nicholas Andrews and Marcus Bishop</td>
      <td><a href="https://doi.org/10.18653/v1/D19-1178">link</a></td>
      <td>2019</td>
      <td>EMNLP-IJCNLP, pages 1684–1695</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>(Dis)improved?! How Simplified Language Affects Large Language Model Performance across Languages</em><span class="tooltip">Simplified language enhances the accessibility and human understanding of texts. However, whether it also benefits large language models (LLMs) remains underexplored. This paper extensively studies whether LLM performance improves on simplified data compared to its original counterpart. Our experiments span six datasets and nine automatic simplification systems across three languages. We show that English models, including GPT-4o-mini, show a weak generalization and exhibit a significant performance drop on simplified data. This introduces an intriguing paradox: simplified data is helpful for humans but not for LLMs. At the same time, the performance in non-English languages sometimes improves, depending on the task and quality of the simplifier. Our findings offer a comprehensive view of the impact of simplified language on LLM performance and uncover severe implications for people depending on simple language.</span></span></td>
      <td>Miriam Anschütz, Anastasiya Damaratskaya, Chaeeun Joy Lee, Arthur Schmalz, Edoardo Mosca, and Georg Groh</td>
      <td><a href="https://aclanthology.org/2025.gem-1.70/">link</a></td>
      <td>2025</td>
      <td>GEM² Workshop, pages 847–861</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>A light in the dark web: Linking dark web aliases to real internet identities</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Ehsan Arabnezhad, Massimo La Morgia, Alessandro Mei, Eugenio Nerio Nemmi, and Julinda Stefa</td>
      <td><a href="https://doi.org/10.1109/ICDCS47774.2020.00081">link</a></td>
      <td>2020</td>
      <td>ICDCS, pages 311–321</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Computational forensic authorship analysis: Promises and pitfalls</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Shlomo Argamon</td>
      <td><a href="https://papers.ssrn.com/abstract=3396724">link</a></td>
      <td>2018</td>
      <td>Language and Law/Linguagem e Direito, 5(2):7–37</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Overview of the International Authorship Identification Competition at PAN-2011</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Shlomo Argamon and Patrick Juola</td>
      <td><a href="https://ceur-ws.org/Vol-1177/CLEF2011wn-PAN-ArgamonEt2011.pdf">link</a></td>
      <td>2011</td>
      <td>CLEF 2011</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Efficient Large Scale Language Modeling with Mixtures of Experts</em><span class="tooltip">Mixture of Experts layers (MoEs) enable efficient scaling of language models through conditional computation. This paper presents a detailed empirical study of how autoregressive MoE language models scale in comparison with dense models in a wide range of settings: in- and out-of-domain language modeling, zero- and few-shot priming, and full-shot fine-tuning. With the exception of fine-tuning, we find MoEs to be substantially more compute efficient. At more modest training budgets, MoEs can match the performance of dense models using ~4 times less compute. This gap narrows at scale, but our largest MoE model (1.1T parameters) consistently outperforms a compute-equivalent dense model (6.7B parameters). Overall, this performance gap varies greatly across tasks and domains, suggesting that MoE and dense models generalize differently in ways that are worthy of future study. We make our code and models publicly available for research use.</span></span></td>
      <td>Meta AI, Mikel Artetxe, Shruti Bhosale, Naman Goyal, et al.</td>
      <td><a href="https://doi.org/10.18653/v1/2022.emnlp-main.804">link</a></td>
      <td>2022</td>
      <td>EMNLP, pages 11699–11732</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>The Routledge Handbook of Sociolinguistics Around the World, 2nd edition</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Martin J. Ball, Rajend Mesthrie, and Chiara Meluzzi</td>
      <td><a href="https://doi.org/10.4324/9781003198345">link</a></td>
      <td>2023</td>
      <td>Routledge</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>The Language That Drives Engagement: A Systematic Large-scale Analysis of Headline Experiments</em><span class="tooltip">We use a large-scale data set of thousands of field experiments conducted on Upworthy.com , an online media platform, to investigate the cognitive, motivational, affective, and grammatical factors implementable in messages that increase engagement with online content.</span></span></td>
      <td>Akshina Banerjee and Oleg Urminsky</td>
      <td><a href="https://doi.org/10.1287/mksc.2021.0018">link</a></td>
      <td>2025</td>
      <td>Marketing Science, 44(3):566–592</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Keep it Private: Unsupervised privatization of online text</em><span class="tooltip">Authorship obfuscation techniques hold the promise of helping people protect their privacy in online communications by automatically rewriting text to hide the identity of the original author. However, obfuscation has been evaluated in narrow settings in the NLP literature and has primarily been addressed with superficial edit operations that can lead to unnatural outputs. In this work, we introduce an automatic text privatization framework that fine-tunes a large language model via reinforcement learning to produce rewrites that balance soundness, sense, and privacy. We evaluate it extensively on a large-scale test set of English Reddit posts by 68k authors composed of short-medium length texts. We study how the performance changes among evaluative conditions including authorial profile length and authorship detection strategy. Our method maintains high text quality according to both automated metrics and human evaluation, and successfully evades several automated authorship attacks.</span></span></td>
      <td>Calvin Bao and Marine Carpuat</td>
      <td><a href="https://doi.org/10.18653/v1/2024.naacl-long.480">link</a></td>
      <td>2024</td>
      <td>NAACL, pages 8678–8693</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Measuring what Matters: Construct Validity in Large Language Model Benchmarks</em><span class="tooltip">Evaluating large language models (LLMs) is crucial for both assessing their capabilities and identifying safety or robustness issues prior to deployment. Reliably measuring abstract and complex phenomena such as `safety&#x27; and `robustness&#x27; requires strong construct validity, that is, having measures that represent what matters to the phenomenon. With a team of 29 expert reviewers, we conduct a systematic review of 445 LLM benchmarks from leading conferences in natural language processing and machine learning. Across the reviewed articles, we find patterns related to the measured phenomena, tasks, and scoring metrics which undermine the validity of the resulting claims. To address these shortcomings, we provide eight key recommendations and detailed actionable guidance to researchers and practitioners in developing LLM benchmarks.</span></span></td>
      <td>Andrew M. Bean, Ryan Othniel Kearns, Angelika Romanou, Franziska Sofia Hafner, Harry Mayne, Jan Batzner, Negar Foroutan, Chris Schmitz, Karolina Korgul, Hunar Batra, Oishi Deb, Emma Beharry, Cornelius Emde, Thomas Foster, Anna Gausen, María Grandury, Simeng Han, Valentin Hofmann, Lujain Ibrahim, Hazel Kim, et al.</td>
      <td><a href="https://openreview.net/forum?id=mdA5lVvNcU">link</a></td>
      <td>2025</td>
      <td>NeurIPS</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Probing classifiers: Promises, shortcomings, and advances</em><span class="tooltip">Abstract Probing classifiers have emerged as one of the prominent methodologies for interpreting and analyzing deep neural network models of natural language processing. The basic idea is simple—a classifier is trained to predict some linguistic property from a model’s representations—and has been used to examine a wide variety of models and properties. However, recent studies have demonstrated various methodological limitations of this approach. This squib critically reviews the probing classifiers framework, highlighting their promises, shortcomings, and advances.</span></span></td>
      <td>Yonatan Belinkov</td>
      <td><a href="https://doi.org/10.1162/coli_a_00422">link</a></td>
      <td>2022</td>
      <td>Computational Linguistics, 48(1):207–219</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>What do neural machine translation models learn about morphology?</em><span class="tooltip">Neural machine translation (MT) models obtain state-of-the-art performance while maintaining a simple, end-to-end architecture. However, little is known about what these models learn about source and target languages during the training process. In this work, we analyze the representations learned by neural MT models at various levels of granularity and empirically evaluate the quality of the representations for learning morphology through extrinsic part-of-speech and morphological tagging tasks. We conduct a thorough investigation along several parameters: word-based vs. character-based representations, depth of the encoding layer, the identity of the target language, and encoder vs. decoder representations. Our data-driven, quantitative evaluation sheds light on important aspects in the neural MT system and its ability to capture word structure.</span></span></td>
      <td>Yonatan Belinkov, Nadir Durrani, Fahim Dalvi, Hassan Sajjad, and James Glass</td>
      <td><a href="https://doi.org/10.18653/v1/P17-1080">link</a></td>
      <td>2017</td>
      <td>ACL, pages 861–872</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Language style as audience design</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Allan Bell</td>
      <td><a href="http://www.jstor.org/stable/4167516">link</a></td>
      <td>1984</td>
      <td>Language in Society, 13(2):145–204</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Overview of PAN 2025: Generative AI Detection, Multilingual Text Detoxification, Multi-author Writing Style Analysis, and Generative Plagiarism Detection</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Janek Bevendorff, Daryna Dementieva, Maik Fröbe, Bela Gipp, André Greiner-Petter, Jussi Karlgren, Maximilian Mayerl, Preslav Nakov, Alexander Panchenko, Martin Potthast, Artem Shelmanov, Efstathios Stamatatos, Benno Stein, Yuxia Wang, Matti Wiegmann, and Eva Zangerle</td>
      <td><a href="https://doi.org/10.1007/978-3-031-88720-8_64">link</a></td>
      <td>2025</td>
      <td>Advances in Information Retrieval, pages 434–441</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>The two paradigms of LLM detection: Authorship attribution vs. authorship verification</em><span class="tooltip">The detection of texts generated by LLMs has quickly become an important research problem. Many supervised and zero-shot detectors have already been proposed, yet their effectiveness and precision remain disputed. Current research therefore focuses on making detectors robust against domain shifts and on building corresponding benchmarks. In this paper, we show that the actual limitations hindering progress in LLM detection lie elsewhere: LLM detection is often implicitly modeled as an authorship attribution task, while its true nature is that of authorship verification. We systematically analyze the current research with respect to this misunderstanding, conduct an in-depth comparative analysis of the benchmarks, and validate our claim using state-of-the-art LLM detectors. Our contributions open the realm of authorship analysis technology for understanding and tackling the problem of LLM detection.</span></span></td>
      <td>Janek Bevendorff, Matti Wiegmann, Emmelie Richter, Martin Potthast, and Benno Stein</td>
      <td><a href="https://doi.org/10.18653/v1/2025.findings-acl.194">link</a></td>
      <td>2025</td>
      <td>Findings of ACL 2025, pages 3762–3787</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Variation across Speech and Writing</em><span class="tooltip">Similarities and differences between speech and writing have been the subject of innumerable studies, but until now there has been no attempt to provide a unified linguistic analysis of the whole range of spoken and written registers in English. In this widely acclaimed empirical study, Douglas Biber uses computational techniques to analyse the linguistic characteristics of twenty three spoken and written genres, enabling identification of the basic, underlying dimensions of variation in English. In Variation Across Speech and Writing, six dimensions of variation are identified through a factor analysis, on the basis of linguistic co-occurence patterns. The resulting model of variation provides for the description of the distinctive linguistic characteristics of any spoken or written text andd emonstrates the ways in which the polarization of speech and writing has been misleading, and thus enables reconciliation of the contradictory conclusions reached in previous research.</span></span></td>
      <td>Douglas Biber</td>
      <td><a href="https://doi.org/10.1017/CBO9780511621024">link</a></td>
      <td>1988</td>
      <td>Cambridge University Press</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Register, Genre, and Style, 2nd edition</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Douglas Biber and Susan Conrad</td>
      <td><a href="https://doi.org/10.1017/9781108686136">link</a></td>
      <td>2019</td>
      <td>Cambridge University Press</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Natural Language Processing with Python</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Steven Bird, Ewan Klein, and Edward Loper</td>
      <td><a href="https://www.nltk.org/book/">link</a></td>
      <td>2019</td>
      <td>O'Reilly Media</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Centering the speech community</em><span class="tooltip">How can NLP/AI practitioners engage with oral societies and develop locally appropriate language technologies? We report on our experience of working together over five years in a remote community in the far north of Australia, and how we prototyped simple language technologies to support our collaboration. We navigated different understandings of language, the functional differentiation of oral vs institutional languages, and the distinct technology opportunities for each. Our collaboration unsettled the first author’s western framing of language as data for exploitation by machines, and we devised a design pattern that seems better aligned with local interests and aspirations. We call for new collaborations on the design of locally appropriate technologies for languages with primary orality.</span></span></td>
      <td>Steven Bird and Dean Yibarbuk</td>
      <td><a href="https://aclanthology.org/2024.eacl-long.50/">link</a></td>
      <td>2024</td>
      <td>EACL, pages 826–839</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>ETS corpus of non-native written English LDC2014T06</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Daniel Blanchard, Joel Tetreault, Derrick Higgins, Aoife Cahill, and Martin Chodorow</td>
      <td><a href="https://doi.org/10.35111/7ez0-x912">link</a></td>
      <td>2014</td>
      <td>Linguistic Data Consortium</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>The language of intergroup distinctiveness</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Richard Y. Bourhis and Howard Giles</td>
      <td><a href="https://www.researchgate.net/publication/269710388_The_Language_of_Intergroup_Distinctiveness">link</a></td>
      <td>1977</td>
      <td>Language, Ethnicity and Intergroup Relations, pages 119–135</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Rethinking the Authorship Verification Experimental Setups</em><span class="tooltip">One of the main drivers of the recent advances in authorship verification is the PAN large-scale authorship dataset. Despite generating significant progress in the field, inconsistent performance differences between the closed and open test sets have been reported. To this end, we improve the experimental setup by proposing five new public splits over the PAN dataset, specifically designed to isolate and identify biases related to the text topic and to the author’s writing style. We evaluate several BERT-like baselines on these splits, showing that such models are competitive with authorship verification state-of-the-art methods. Furthermore, using explainable AI, we find that these baselines are biased towards named entities. We show that models trained without the named entities obtain better results and generalize better when tested on DarkReddit, our new dataset for authorship verification.</span></span></td>
      <td>Florin Brad, Andrei Manolache, Elena Burceanu, Antonio Barbalau, Radu Tudor Ionescu, and Marius Popescu</td>
      <td><a href="https://doi.org/10.18653/v1/2022.emnlp-main.380">link</a></td>
      <td>2022</td>
      <td>EMNLP, pages 5634–5643</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Adversarial stylometry: Circumventing authorship recognition to preserve privacy and anonymity</em><span class="tooltip">The use of stylometry, authorship recognition through purely linguistic means, has contributed to literary, historical, and criminal investigation breakthroughs. Existing stylometry research assumes that authors have not attempted to disguise their linguistic writing style. We challenge this basic assumption of existing stylometry methodologies and present a new area of research: adversarial stylometry. Adversaries have a devastating effect on the robustness of existing classification methods. Our work presents a framework for creating adversarial passages including obfuscation , where a subject attempts to hide her identity, and imitation , where a subject attempts to frame another subject by imitating his writing style, and translation where original passages are obfuscated with machine translation services. This research demonstrates that manual circumvention methods work very well while automated translation methods are not effective. The obfuscation method reduces the techniques&#x27; effectiveness to the level of random guessing and the imitation attempts succeed up to 67% of the time depending on the stylometry technique used. These results are more significant given the fact that experimental subjects were unfamiliar with stylometry, were not professional writers, and spent little time on the attacks. This article also contributes to the field by using human subjects to empirically validate the claim of high accuracy for four current techniques (without adversaries). We have also compiled and released two corpora of adversarial stylometry texts to promote research in this field with a total of 57 unique authors. We argue that this field is important to a multidisciplinary approach to privacy, security, and anonymity.</span></span></td>
      <td>Michael Brennan, Sadia Afroz, and Rachel Greenstadt</td>
      <td><a href="https://doi.org/10.1145/2382448.2382450">link</a></td>
      <td>2012</td>
      <td>ACM TISSEC, 15:1–22</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>'Delta': a measure of stylistic difference and a guide to likely authorship</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>John Burrows</td>
      <td><a href="https://doi.org/10.1093/llc/17.3.267">link</a></td>
      <td>2002</td>
      <td>Literary and Linguistic Computing, 17(3):267–287</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>How the communication style of chatbots influences consumers' satisfaction, trust, and engagement in the context of service failure</em><span class="tooltip">Abstract This study examines consumers’ reactions to the communication styles of chatbots during failed service experiences. The current study explores whether the communication style adopted by a chatbot impacts consumer satisfaction and behavior intention and how expectancy violations can moderate these relationships in the service context. A pre-test examined the validity of the stimuli of chatbots that were either task-oriented or social-oriented after consumers encountered service failure. For more information, the experiment was designed to manipulate the AI-based chatbot agent’s process and style of communication and measure the role of expectancy violations. The main experiment results showed that interactions with social-oriented communication style chatbots enhance the level of consumers’ interaction satisfaction and intention of behavior. Respondents experienced a higher perception of warmth when interacting with social-oriented communication style chatbots than task-oriented. Moreover, expectancy violation moderates the mediation of warmth on the relationship between the chatbot’s communication style/type and interaction satisfaction, trust, and intention of patronage. Setting chatbots’ communication styles to be social-oriented can help reduce negative emotions among consumers caused by service failure; specifically, the perception of warmth created by the social-oriented communication style can alleviate negative evaluations of service agents and companies, such as dissatisfaction and loss of interest. Therefore, in managerial practice, the firm should choose the social-oriented communication style chatbot agent to recover the customer relationship after a service failure.</span></span></td>
      <td>Na Cai, Shuhong Gao, and Jinzhe Yan</td>
      <td><a href="https://doi.org/10.1057/s41599-024-03212-0">link</a></td>
      <td>2024</td>
      <td>Humanities and Social Sciences Communications, 11(1):687</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Accent, (ING), and the social logic of listener perceptions</em><span class="tooltip">This article reports on the relationship between the English variable (ING) and two divergent accents (Southern and gay) as they are conceptualized and given social meaning in listeners&#x27; perceptions of spontaneous speech. The study used an expanded form of the Matched Guise Technique, using recordings collected through sociolinguistic interviews with 8 speakers from North Carolina and California. Excerpts were digitally manipulated to create 32 matched pairs differing only in tokens of (ING), which were used to collect responses in group interviews (N = 55) and a Web-based experiment (N = 124). The alveolar variant -in increased the perceived strength of Southern accents and dampened an accent heard as gay and urban. The influence of (ING) on these accents is linked to shared social meanings of the alveolar form -in and Southern accents on the one hand (lack of education, the country, and the term “redneck”) and the velar variant -ing and the gay accent on the other (lowered masculinity, the city, and the term “metrosexual”). These two accents are contrasted with a third variety, heard as nonaccented and aregional. These effects demonstrate the status of the three linguistic objects, the two accents and (ING), as social objects as well.</span></span></td>
      <td>Kathryn Campbell-Kibler</td>
      <td><a href="https://doi.org/10.1215/00031283-2007-002">link</a></td>
      <td>2007</td>
      <td>American Speech, 82(1):32–64</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>The nature of sociolinguistic perception</em><span class="tooltip">Abstract This study investigates how linguistic variation carries social meaning, examining the impact of the English variable (ING) on perceptions of eight speakers from the U.S. West Coast and South. Thirty-two excerpts of spontaneous speech were digitally manipulated to vary only in tokens of (ING) and used to collect listener perceptions in group interviews ( N = 55) and an experiment ( N = 124). Interview data and experimental results show that (ING) impacts social perception variably, inhabiting an indexical field of related meanings (Eckert, Penelope. [2008]. Variation and the indexical field. Journal of Sociolinguistics 12(4):453–476). One of these meanings, intelligence/education, is explored in detail to understand how a given meaning is realized or not in a specific context. Speakers were heard as less educated/intelligent when they used -in , but this effect is driven by reactions to speakers heard as aregional and not as working-class. Some implications on our future understanding of the processing of socially laden variation are discussed.</span></span></td>
      <td>Kathryn Campbell-Kibler</td>
      <td><a href="https://doi.org/10.1017/S0954394509000052">link</a></td>
      <td>2009</td>
      <td>Language Variation and Change, 21(1):135–156</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>The sociolinguistic variant as a carrier of social meaning</em><span class="tooltip">Abstract Traditionally used as a “heuristic device” (Labov, 1978), the sociolinguistic variable has taken on a new role as a primitive of speaker/hearer mental models in third-wave variation work (Eckert, 2005, 2008). Results from a sociolinguistic perception study suggest that at least in some cases, variants of the same variable function independently as loci of indexically linked social meaning. Listener responses were collected to three matched guises of the English variable (ING): -in , -ing , and a neutral guise with no audible (ING) tokens. The results counter the study hypothesis that listener expectation, triggered by speaker regional accent, would shape (ING)&#x27;s impact. Instead, the two variants showed distinct social associations: the -ing guises were rated as more intelligent/educated, more articulate, and less likely to be a student than either the -in or neutral guises, which did not differ significantly. In contrast, -in guises made speakers sound less formal and less likely to be gay than the -ing and neutral guises, which did not differ. These results suggest that third-wave work needs to more closely examine the role of the variable in theorizing the relationship between linguistic and social structures.</span></span></td>
      <td>Kathryn Campbell-Kibler</td>
      <td><a href="https://doi.org/10.1017/S0954394510000177">link</a></td>
      <td>2011</td>
      <td>Language Variation and Change, 22(3):423–441</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>The elements of style</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Kathryn Campbell-Kibler, Penelope Eckert, Norma Mendoza-Denton, and Emma Moore</td>
      <td><a href="https://www.asc.ohio-state.edu/campbell-kibler.1//HMB_poster.pdf">link</a></td>
      <td>2006</td>
      <td>NWAV Poster Session</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Expertise style transfer: A new task towards better communication between experts and laymen</em><span class="tooltip">The curse of knowledge can impede communication between experts and laymen. We propose a new task of expertise style transfer and contribute a manually annotated dataset with the goal of alleviating such cognitive biases. Solving this task not only simplifies the professional language, but also improves the accuracy and expertise level of laymen descriptions using simple words. This is a challenging task, unaddressed in previous work, as it requires the models to have expert intelligence in order to modify text with a deep understanding of domain knowledge and structures. We establish the benchmark performance of five state-of-the-art models for style transfer and text simplification. The results demonstrate a significant gap between machine and human performance. We also discuss the challenges of automatic evaluation, to provide insights into future research directions. The dataset is publicly available at &lt;a href=https://srhthu.github.io/expertise-style-transfer/ class=acl-markup-url&gt;https://srhthu.github.io/expertise-style-transfer/&lt;/a&gt;.</span></span></td>
      <td>Yixin Cao, Ruihao Shui, Liangming Pan, Min-Yen Kan, Zhiyuan Liu, and Tat-Seng Chua</td>
      <td><a href="https://doi.org/10.18653/v1/2020.acl-main.100">link</a></td>
      <td>2020</td>
      <td>ACL, pages 1061–1071</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>On the diversity of synthetic data and its impact on training large language models</em><span class="tooltip">The rise of Large Language Models (LLMs) has accentuated the need for diverse, high-quality pre-training data. Synthetic data emerges as a viable solution to the challenges of data scarcity and inaccessibility. While previous literature has focused predominantly on the quality and quantity of real data, our work enables the measurement of diversity in synthetic data and explores its impact on LLM performance. We study the downstream effects of synthetic data diversity during both the pre-training and fine-tuning stages by introducing a new diversity metric, \textit{LLM cluster-agent}, designed to evaluate the diversity of synthetic datasets. Through a series of controlled experiments with models of 350M and 1.4B parameters, we demonstrate that the proposed cluster-based LLM scoring of diversity correlates positively with both pre-training and supervised fine-tuning performance. Our findings also reveal that synthetic data diversity in pre-training affects supervised fine-tuning more significantly than pre-training itself, even for smaller models. We hope this study advances our understanding of the optimal use of synthetic data in LLM training and opens new avenues for efficient data generation processes.</span></span></td>
      <td>Hao Chen, Abdul Waheed, Xiang Li, Yidong Wang, Jindong Wang, Bhiksha Raj, and Marah I. Abdin</td>
      <td><a href="https://doi.org/10.48550/arXiv.2410.15226">link</a></td>
      <td>2024</td>
      <td>arXiv preprint ArXiv:2410.15226</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>HumT DumT: Measuring and controlling human-like language in LLMs</em><span class="tooltip">Should LLMs generate language that makes them seem human? Human-like language might improve user experience, but might also lead to deception, overreliance, and stereotyping. Assessing these potential impacts requires a systematic way to measure human-like tone in LLM outputs. We introduce HumT and SocioT, metrics for human-like tone and other dimensions of social perceptions in text data based on relative probabilities from an LLM. By measuring HumT across preference and usage datasets, we find that users prefer less human-like outputs from LLMs in many contexts. HumT also offers insights into the perceptions and impacts of anthropomorphism: human-like LLM outputs are highly correlated with warmth, social closeness, femininity, and low status, which are closely linked to the aforementioned harms. We introduce DumT, a method using HumT to systematically control and reduce the degree of human-like tone while preserving model performance. DumT offers a practical approach for mitigating risks associated with anthropomorphic language generation.</span></span></td>
      <td>Myra Cheng, Sunny Yu, and Dan Jurafsky</td>
      <td><a href="https://doi.org/10.18653/v1/2025.acl-long.1261">link</a></td>
      <td>2025</td>
      <td>ACL, pages 25983–26008</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>CLUB: a contrastive log-ratio upper bound of mutual information</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Pengyu Cheng, Weituo Hao, Shuyang Dai, Jiachang Liu, Zhe Gan, and Lawrence Carin</td>
      <td><a href="https://proceedings.mlr.press/v119/cheng20b.html">link</a></td>
      <td>2020</td>
      <td>ICML</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Improving disentangled text representation learning with information-theoretic guidance</em><span class="tooltip">Learning disentangled representations of natural language is essential for many NLP tasks, e.g., conditional text generation, style transfer, personalized dialogue systems, etc. Similar problems have been studied extensively for other forms of data, such as images and videos. However, the discrete nature of natural language makes the disentangling of textual representations more challenging (e.g., the manipulation over the data space cannot be easily achieved). Inspired by information theory, we propose a novel method that effectively manifests disentangled representations of text, without any supervision on semantics. A new mutual information upper bound is derived and leveraged to measure dependence between style and content. By minimizing this upper bound, the proposed method induces style and content embeddings into two independent low-dimensional spaces. Experiments on both conditional text generation and text-style transfer demonstrate the high quality of our disentangled representation in terms of content and style preservation.</span></span></td>
      <td>Pengyu Cheng, Martin Renqiang Min, Dinghan Shen, Christopher Malon, Yizhe Zhang, Yitong Li, and Lawrence Carin</td>
      <td><a href="https://doi.org/10.18653/v1/2020.acl-main.673">link</a></td>
      <td>2020</td>
      <td>ACL, pages 7530–7541</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Evaluating synthetic data generation from user generated text</em><span class="tooltip">Abstract User-generated content provides a rich resource to study social and behavioral phenomena. Although its application potential is currently limited by the paucity of expert labels and the privacy risks inherent in personal data, synthetic data can help mitigate this bottleneck. In this work, we introduce an evaluation framework to facilitate research on synthetic language data generation for user-generated text. We define a set of aspects for assessing data quality, namely, style preservation, meaning preservation, and divergence, as a proxy for privacy. We introduce metrics corresponding to each aspect. Moreover, through a set of generation strategies and representative tasks and baselines across domains, we demonstrate the relation between the quality aspects of synthetic user generated content, generation strategies, metrics, and downstream performance. To our knowledge, our work is the first unified evaluation framework for user-generated text in relation to the specified aspects, offering both intrinsic and extrinsic evaluation. We envisage it will facilitate developments towards shareable, high-quality synthetic language data.</span></span></td>
      <td>Jenny Chim, Julia Ive, and Maria Liakata</td>
      <td><a href="https://doi.org/10.1162/coli_a_00540">link</a></td>
      <td>2025</td>
      <td>Computational Linguistics, 51(1):191–233</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>When Variants Lack Semantic Equivalence: Adverbial Subclause Word Order</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Tanya Karoli Christensen and Torben Juel Jensen</td>
      <td><a href="https://doi.org/10.1017/9781108674942.008">link</a></td>
      <td>2022</td>
      <td>Cambridge University Press, pages 171–206</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Conventionality and contrast: Pragmatic principles with lexical consequences</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Eve V. Clark</td>
      <td><a href="https://doi.org/10.4324/9780203062821-8">link</a></td>
      <td>1992</td>
      <td>Frames, Fields, and Contrasts, pages 171–188</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Dimensions of abusive language on Twitter</em><span class="tooltip">In this paper, we use a new categorical form of multidimensional register analysis to identify the main dimensions of functional linguistic variation in a corpus of abusive language, consisting of racist and sexist Tweets. By analysing the use of a wide variety of parts-of-speech and grammatical constructions, as well as various features related to Twitter and computer-mediated communication, we discover three dimensions of linguistic variation in this corpus, which we interpret as being related to the degree of interactive, antagonistic and attitudinal language exhibited by individual Tweets. We then demonstrate that there is a significant functional difference between racist and sexist Tweets, with sexists Tweets tending to be more interactive and attitudinal than racist Tweets.</span></span></td>
      <td>Isobelle Clarke and Jack Grieve</td>
      <td><a href="https://doi.org/10.18653/v1/W17-3001">link</a></td>
      <td>2017</td>
      <td>First Workshop on Abusive Language Online, pages 1–11</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Detecting collaborations in text comparing the authors' rhetorical language choices in the federalist papers</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Jeff Collins, David Kaufer, Pantelis Vlachos, Brian Butler, and Suguru Ishizaki</td>
      <td><a href="https://doi.org/10.1023/B:CHUM.0000009291.06947.52">link</a></td>
      <td>2004</td>
      <td>Computers and the Humanities, 38:15–36</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Author identification, idiolect, and linguistic uniqueness</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Malcolm Coulthard</td>
      <td><a href="https://doi.org/10.1093/applin/25.4.431">link</a></td>
      <td>2004</td>
      <td>Applied Linguistics, 25(4):431–447</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Style: Language Variation and Identity</em><span class="tooltip">Style refers to ways of speaking - how speakers use the resource of language variation to make meaning in social encounters. This 2007 book develops a coherent theoretical approach to style in sociolinguistics, illustrated with copious examples. It explains how speakers project different social identities and create different social relationships through their style choices, and how speech-style and social context inter-relate. Style therefore refers to the wide range of strategic actions and performances that speakers engage in, to construct themselves and their social lives. Coupland draws on and integrates a wide variety of contemporary sociolinguistic research as well as his own extensive research in this field. The emphasis is on how social meanings are made locally, in specific relationships, genres, groups and cultures, and on studying language variation as part of the analysis of spoken discourse.</span></span></td>
      <td>Nikolas Coupland</td>
      <td><a href="https://doi.org/10.1017/CBO9780511755064">link</a></td>
      <td>2007</td>
      <td>Cambridge University Press</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Txtng: The gr8 db8</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>David Crystal</td>
      <td><a href="https://doi.org/10.1002/9781444302776">link</a></td>
      <td>2008</td>
      <td>Oxford University Press</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>A Dictionary of Linguistics and Phonetics, 6th edition</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>David Crystal</td>
      <td><a href="https://doi.org/10.1002/9781444302776">link</a></td>
      <td>2011</td>
      <td>Blackwell Publishing</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Investigating English Style</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>David Crystal and Derek Davy</td>
      <td><a href="https://doi.org/10.4324/9781315538419">link</a></td>
      <td>1969</td>
      <td>Routledge</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Learning stylometric representations for authorship analysis</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Steven H. H. Ding, Benjamin C. M. Fung, Farkhund Iqbal, and William K. Cheung</td>
      <td><a href="https://doi.org/10.1109/TCYB.2017.2766189">link</a></td>
      <td>2019</td>
      <td>IEEE Transactions on Cybernetics, 49(1):107–121</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Speaker recognition based on idiolectal differences between speakers</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>George R. Doddington</td>
      <td><a href="https://doi.org/10.21437/Eurospeech.2001-417">link</a></td>
      <td>2001</td>
      <td>Eurospeech 2001, pages 2521–2524</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Automatically constructing a corpus of sentential paraphrases</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>William B. Dolan and Chris Brockett</td>
      <td><a href="https://aclanthology.org/I05-5002/">link</a></td>
      <td>2005</td>
      <td>IWP2005</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Triplet loss in siamese network for object tracking</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Xingping Dong and Jianbing Shen</td>
      <td><a href="https://doi.org/10.1007/978-3-030-01261-8_28">link</a></td>
      <td>2018</td>
      <td>ECCV 2018, pages 472–488</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Refocusing on relevance: Personalization in NLG</em><span class="tooltip">Many NLG tasks such as summarization, dialogue response, or open domain question answering, focus primarily on a source text in order to generate a target response. This standard approach falls short, however, when a user’s intent or context of work is not easily recoverable based solely on that source text– a scenario that we argue is more of the rule than the exception. In this work, we argue that NLG systems in general should place a much higher level of emphasis on making use of additional context, and suggest that relevance (as used in Information Retrieval) be thought of as a crucial tool for designing user-oriented text-generating tasks. We further discuss possible harms and hazards around such personalization, and argue that value-sensitive design represents a crucial path forward through these challenges.</span></span></td>
      <td>Shiran Dudy, Steven Bedrick, and Bonnie Webber</td>
      <td><a href="https://doi.org/10.18653/v1/2021.emnlp-main.421">link</a></td>
      <td>2021</td>
      <td>EMNLP, pages 5190–5202</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>HotFlip: White-Box Adversarial Examples for Text Classification</em><span class="tooltip">We propose an efficient method to generate white-box adversarial examples to trick a character-level neural classifier. We find that only a few manipulations are needed to greatly decrease the accuracy. Our method relies on an atomic flip operation, which swaps one token for another, based on the gradients of the one-hot input vectors. Due to efficiency of our method, we can perform adversarial training which makes the model more robust to attacks at test time. With the use of a few semantics-preserving constraints, we demonstrate that HotFlip can be adapted to attack a word-level classifier as well.</span></span></td>
      <td>Javid Ebrahimi, Anyi Rao, Daniel Lowd, and Dejing Dou</td>
      <td><a href="https://doi.org/10.18653/v1/P18-2006">link</a></td>
      <td>2018</td>
      <td>ACL, pages 31–36</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Jocks and Burnouts: Social Categories and Identity in the High School</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Penelope Eckert</td>
      <td>-</td>
      <td>1989</td>
      <td>Teachers College Press</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Variation and the indexical field</em><span class="tooltip">This paper argues for a focus on the social meaning of variation, based in a study of stylistic practice. It is common in the study of variation to interpret variables as reflections of speakers&#x27; membership in social categories. Others have argued more recently that variables are associated not with the categories themselves, but with stances and characteristics that constitute those categories. The paper reviews some variation studies that show that variables do not have static meanings, but rather general meanings that become more specific in the context of styles. Building on Michael Silverstein&#x27;s notion of indexical order, I argue that the meanings of variables are not precise or fixed but rather constitute a field of potential meanings – an indexical field , or constellation of ideologically related meanings, any one of which can be activated in the situated use of the variable. The field is fluid, and each new activation has the potential to change the field by building on ideological connections. Thus variation constitutes an indexical system that embeds ideology in language and that is in turn part and parcel of the construction of ideology.</span></span></td>
      <td>Penelope Eckert</td>
      <td><a href="https://doi.org/10.1111/j.1467-9841.2008.00374.x">link</a></td>
      <td>2008</td>
      <td>Journal of Sociolinguistics, 12(4):453–476</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Three waves of variation study: The emergence of meaning in the study of sociolinguistic variation</em><span class="tooltip">The treatment of social meaning in sociolinguistic variation has come in three waves of analytic practice. The first wave of variation studies established broad correlations between linguistic variables and the macrosociological categories of socioeconomic class, gender, ethnicity, and age. The second wave employed ethnographic methods to explore the local categories and configurations that inhabit, or constitute, these broader categories. In both waves, variation was seen as marking social categories. This article sets out a theoretical foundation for the third wave, arguing that (a) variation constitutes a robust social semiotic system, potentially expressing the full range of social concerns in a given community; (b) the meanings of variables are underspecified, gaining more specific meanings in the context of styles, and (c) variation does not simply reflect, but also constructs, social meaning and hence is a force in social change.</span></span></td>
      <td>Penelope Eckert</td>
      <td><a href="https://doi.org/10.1146/annurev-anthro-092611-145828">link</a></td>
      <td>2012</td>
      <td>Annual Review of Anthropology, 41(1):87–100</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Stylometry with R: A Package for Computational Text Analysis</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Maciej Eder, Jan Rybicki, and Mike Kestemont</td>
      <td><a href="https://doi.org/10.32614/RJ-2016-007">link</a></td>
      <td>2016</td>
      <td>The R Journal, 8(1):107–121</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Analyzing the Persuasive Effect of Style in News Editorial Argumentation</em><span class="tooltip">News editorials argue about political issues in order to challenge or reinforce the stance of readers with different ideologies. Previous research has investigated such persuasive effects for argumentative content. In contrast, this paper studies how important the style of news editorials is to achieve persuasion. To this end, we first compare content- and style-oriented classifiers on editorials from the liberal NYTimes with ideology-specific effect annotations. We find that conservative readers are resistant to NYTimes style, but on liberals, style even has more impact than content. Focusing on liberals, we then cluster the leads, bodies, and endings of editorials, in order to learn about writing style patterns of effective argumentation.</span></span></td>
      <td>Roxanne El Baff, Henning Wachsmuth, Khalid Al Khatib, and Benno Stein</td>
      <td><a href="https://doi.org/10.18653/v1/2020.acl-main.287">link</a></td>
      <td>2020</td>
      <td>ACL, pages 3154–3160</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Adversarial removal of demographic attributes from text data</em><span class="tooltip">Recent advances in Representation Learning and Adversarial Training seem to succeed in removing unwanted features from the learned representation. We show that demographic information of authors is encoded in—and can be recovered from—the intermediate representations learned by text-based neural classifiers. The implication is that decisions of classifiers trained on textual data are not agnostic to—and likely condition on—demographic attributes. When attempting to remove such demographic information using adversarial training, we find that while the adversarial component achieves chance-level development-set accuracy during training, a post-hoc classifier, trained on the encoded sentences from the first part, still manages to reach substantially higher classification accuracies on the same data. This behavior is consistent across several tasks, demographic properties and datasets. We explore several techniques to improve the effectiveness of the adversarial component. Our main conclusion is a cautionary one: do not rely on the adversarial training to achieve invariant representation to sensitive features.</span></span></td>
      <td>Yanai Elazar and Yoav Goldberg</td>
      <td><a href="https://doi.org/10.18653/v1/D18-1002">link</a></td>
      <td>2018</td>
      <td>EMNLP, pages 11–21</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Evaluating the efficacy of AI content detection tools in differentiating between human and AI-generated text</em><span class="tooltip">Abstract The proliferation of artificial intelligence (AI)-generated content, particularly from models like ChatGPT, presents potential challenges to academic integrity and raises concerns about plagiarism. This study investigates the capabilities of various AI content detection tools in discerning human and AI-authored content. Fifteen paragraphs each from ChatGPT Models 3.5 and 4 on the topic of cooling towers in the engineering process and five human-witten control responses were generated for evaluation. AI content detection tools developed by OpenAI, Writer, Copyleaks, GPTZero, and CrossPlag were used to evaluate these paragraphs. Findings reveal that the AI detection tools were more accurate in identifying content generated by GPT 3.5 than GPT 4. However, when applied to human-written control responses, the tools exhibited inconsistencies, producing false positives and uncertain classifications. This study underscores the need for further development and refinement of AI content detection tools as AI-generated content becomes more sophisticated and harder to distinguish from human-written text.</span></span></td>
      <td>Ahmed M. Elkhatat, Khaled Elsaid, and Saeed Almeer</td>
      <td><a href="https://doi.org/10.1007/s40979-023-00140-5">link</a></td>
      <td>2023</td>
      <td>International Journal for Educational Integrity, 19(1):1–16</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>MMTEB: Massive Multilingual Text Embedding Benchmark</em><span class="tooltip">Text embeddings are typically evaluated on a narrow set of tasks, limited in terms of languages, domains, and task types. To circumvent this limitation and to provide a more comprehensive evaluation, we introduce the Massive Multilingual Text Embedding Benchmark (MMTEB) -- a large-scale community-driven initiative expanding MTEB to over 500 quality-controlled evaluation tasks across 1,000+ languages. MMTEB includes a wide range of challenging novel tasks such as instruction following, long-document retrieval, and code retrieval, and represents the largest multilingual collection of evaluation tasks for embedding models to date. We use this collection to construct multiple highly multilingual benchmarks. We evaluate a representative set of models on these benchmarks. Our findings indicate that, while LLM-based models can achieve state-of-the-art performance on a subset of languages, the best-performing publicly available model across languages is the notably smaller, multilingual-e5-large-instruct. Massive benchmarks often impose high computational demands, limiting accessibility, particularly for low-resource communities. To address this, we downsample tasks based on inter-task correlation (i.e., selecting only a diverse set of tasks) while preserving relative rankings. We further optimize tasks such as retrieval by sampling hard negatives, creating smaller but effective splits. These optimizations allow us to introduce benchmarks at a significantly lower computational cost. For instance, we introduce a new zero-shot English benchmark that maintains a similar ordering at a fraction of the cost.</span></span></td>
      <td>Team MMTEB, Kenneth Enevoldsen, Isaac Chung, Imene Kerboua, et al.</td>
      <td><a href="https://openreview.net/forum?id=zl3pfz4VCV&trk=public_post_comment-text">link</a></td>
      <td>2024</td>
      <td>ICLR</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Variety, style-shifting, and ideology</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Susan M. Ervin-Tripp</td>
      <td><a href="https://doi.org/10.1017/CBO9780511613258.003">link</a></td>
      <td>2001</td>
      <td>Style and Sociolinguistic Variation, pages 44–56</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>OLMo 3</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Team OLMo, Allyson Ettinger, Amanda Bertsch, Bailey Kuehl, et al.</td>
      <td><a href="https://www.datocms-assets.com/64837/1763662397-1763646865-olmo_3_technical_report-1.pdf">link</a></td>
      <td>2025</td>
      <td>Technical Report</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Leveraging Measurement Theory for Natural Language Processing Research</em><span class="tooltip">This dissertation explores the intersection of natural language processing (NLP) and measurement theory. NLP is a field aimed at enabling machines to process and generate human languages, such as English, German, and Mandarin. These languages are complex, diverse, and full of irregularities, making them challenging for machines to handle compared to structured artificial languages, like programming languages. NLP research ranges from simple tasks, like word frequency analysis, to complex ones involving the understanding and generation of human language. Measurement theory, traditionally applied in social sciences, addresses how we measure various properties scientifically. Key concepts include construct validity, which examines whether a measure accurately represents what it intends to measure, and reliability, which focuses on the consistency of a measure across different conditions. This dissertation argues that many challenges in NLP relate to measurement issues and suggests that principles from measurement theory can help address these challenges, particularly by providing tools to evaluate and improve the quality of NLP models. The structure of the dissertation is as follows: Chapter 2 offers background on NLP and measurement theory, covering essential text representation techniques in NLP, the history of measurement theory, and recent discussions on its unification across fields. Chapters 3-5 apply measurement theory to evaluate NLP models: Chapter 3 explores the reliability of gender bias measures in NLP by using classical reliability estimators from social sciences. Chapter 4 adapts a construct validity testing framework to assess the quality of text representations for social science constructs. Chapter 5 introduces a psychometric-based benchmarking approach to evaluate large language models, demonstrated through a case study on eighth-grade math proficiency. Chapters 6-7 focus on using measurement theory to improve NLP model performance: Chapter 6 presents a framework for designing user models based on measurement principles, achieving better-quality user representations than current methods. Chapter 7 examines how integrating human values into model training can enhance models’ ability to recognize values in human arguments. Chapters 8 and 9 reflect on current NLP research challenges and propose future directions: Chapter 8 identifies challenges in text-based personality computing, offering potential solutions and avenues for research. Chapter 9 concludes with a summary of the dissertation’s findings and suggests future work at the intersection of measurement theory and NLP. This work underscores the potential of measurement theory to enhance NLP research by offering frameworks for evaluating and designing more reliable and valid models. By integrating these approaches, the dissertation aims to bridge NLP and measurement theory, advancing NLP&#x27;s capability to address complex measurement challenges.</span></span></td>
      <td>Qixiang Fang</td>
      <td><a href="https://doi.org/10.33540/473">link</a></td>
      <td>2024</td>
      <td>Dissertation, Utrecht University</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Linguistic bias in ChatGPT: Language models reinforce dialect discrimination</em><span class="tooltip">We present a large-scale study of linguistic bias exhibited by ChatGPT covering ten dialects of English (Standard American English, Standard British English, and eight widely spoken non-”standard” varieties from around the world). We prompted GPT-3.5 Turbo and GPT-4 with text by native speakers of each variety and analyzed the responses via detailed linguistic feature annotation and native speaker evaluation. We find that the models default to “standard” varieties of English; based on evaluation by native speakers, we also find that model responses to non-”standard” varieties consistently exhibit a range of issues: stereotyping (19% worse than for “standard” varieties), demeaning content (25% worse), lack of comprehension (9% worse), and condescending responses (15% worse). Moreover, if these models are asked to imitate the writing style of prompts in non-”standard” varieties, they produce text that exhibits lower comprehension of the input and is especially prone to stereotyping. GPT-4 improves on GPT-3.5 in terms of comprehension, warmth, and friendliness, but also exhibits a marked increase in stereotyping (+18%). The results indicate that GPT-3.5 Turbo and GPT-4 can perpetuate linguistic discrimination toward speakers of non-”standard” varieties.</span></span></td>
      <td>Eve Fleisig, Genevieve Smith, Madeline Bossi, Ishita Rustagi, Xavier Yin, and Dan Klein</td>
      <td><a href="https://doi.org/10.18653/v1/2024.emnlp-main.750">link</a></td>
      <td>2024</td>
      <td>EMNLP, pages 13541–13564</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Survey of the state of the art in natural language generation: Core tasks, applications and evaluation</em><span class="tooltip">This paper surveys the current state of the art in Natural Language Generation (NLG), defined as the task of generating text or speech from non-linguistic input. A survey of NLG is timely in view of the changes that the field has undergone over the past two decades, especially in relation to new (usually data-driven) methods, as well as new applications of NLG technology. This survey therefore aims to (a) give an up-to-date synthesis of research on the core tasks in NLG and the architectures adopted in which such tasks are organised; (b) highlight a number of recent research topics that have arisen partly as a result of growing synergies between NLG and other areas of artificial intelligence; (c) draw attention to the challenges in NLG evaluation, relating them to similar challenges faced in other areas of NLP, with an emphasis on different evaluation methods and the relationships between them.</span></span></td>
      <td>Albert Gatt and Emiel Krahmer</td>
      <td><a href="https://doi.org/10.1613/jair.5477">link</a></td>
      <td>2018</td>
      <td>JAIR, 61:65–170</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>GLTR: Statistical detection and visualization of generated text</em><span class="tooltip">The rapid improvement of language models has raised the specter of abuse of text generation systems. This progress motivates the development of simple methods for detecting generated text that can be used by non-experts. In this work, we introduce GLTR, a tool to support humans in detecting whether a text was generated by a model. GLTR applies a suite of baseline statistical methods that can detect generation artifacts across multiple sampling schemes. In a human-subjects study, we show that the annotation scheme provided by GLTR improves the human detection-rate of fake text from 54% to 72% without any prior training. GLTR is open-source and publicly deployed, and has already been widely used to detect generated outputs.</span></span></td>
      <td>Sebastian Gehrmann, Hendrik Strobelt, and Alexander Rush</td>
      <td><a href="https://doi.org/10.18653/v1/P19-3019">link</a></td>
      <td>2019</td>
      <td>ACL System Demonstrations, pages 111–116</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Accommodation theory: Communication, context, and consequence</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Howard Giles, Nikolas Coupland, and Justine Coupland</td>
      <td><a href="https://doi.org/10.1017/CBO9780511613258.002">link</a></td>
      <td>1991</td>
      <td>Contexts of accommodation, 1:1–68</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Speech Style and Social Evaluation</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Howard Giles and Peter F. Powesland</td>
      <td>-</td>
      <td>1975</td>
      <td>Academic Press</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Assessing BERT's syntactic abilities</em><span class="tooltip">I assess the extent to which the recently introduced BERT model captures English syntactic phenomena, using (1) naturally-occurring subject-verb agreement stimuli; (2) &quot;coloreless green ideas&quot; subject-verb agreement stimuli, in which content words in natural sentences are randomly replaced with words sharing the same part-of-speech and inflection; and (3) manually crafted stimuli for subject-verb agreement and reflexive anaphora phenomena. The BERT model performs remarkably well on all cases.</span></span></td>
      <td>Yoav Goldberg</td>
      <td><a href="https://doi.org/10.48550/arXiv.1901.05287">link</a></td>
      <td>2019</td>
      <td>arXiv preprint ArXiv:1901.05287</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Coh-Metrix: Analysis of text on cohesion and language</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Arthur C. Graesser, Danielle S. McNamara, Max M. Louwerse, and Zhiqiang Cai</td>
      <td><a href="https://doi.org/10.3758/BF03195564">link</a></td>
      <td>2004</td>
      <td>Behavior Research Methods, Instruments, & Computers, 36(2):193–202</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>The Idea of Progress in Forensic Authorship Analysis</em><span class="tooltip">This Element examines progress in research and practice in forensic authorship analysis. It describes the existing research base and examines what makes an authorship analysis more or less reliable. Further to this, the author describes the recent history of forensic science and the scientific revolution brought about by the invention of DNA evidence. They chart the rise of three major changes in forensic science – the recognition of contextual bias in analysts, the need for validation studies and shift in logic of providing identification evidence. This Element addresses the idea of progress in forensic authorship analysis in terms of these three issues with regard to new knowledge about the nature of authorship and methods in stylistics and stylometry. The author proposes that the focus needs to shift to validation of protocols for approaching case questions, rather than on validation of systems or general approaches. This title is also available as Open Access on Cambridge Core.</span></span></td>
      <td>Tim Grant</td>
      <td><a href="https://doi.org/10.1017/9781108974714">link</a></td>
      <td>2022</td>
      <td>Cambridge University Press</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Quantitative authorship attribution: An evaluation of techniques</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Jack Grieve</td>
      <td><a href="https://doi.org/10.1093/llc/fqm020">link</a></td>
      <td>2007</td>
      <td>Literary and Linguistic Computing, 22(3):251–270</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Register variation explains stylometric authorship analysis</em><span class="tooltip">Abstract For centuries, investigations of disputed authorship have shown that people have unique styles of writing. Given sufficient data, it is generally possible to distinguish between the writings of a small group of authors, for example, through the multivariate analysis of the relative frequencies of common function words. There is, however, no accepted explanation for why this type of stylometric analysis is successful. Authorship analysts often argue that authors write in subtly different dialects, but the analysis of individual words is not licensed by standard theories of sociolinguistic variation. Alternatively, stylometric analysis is consistent with standard theories of register variation. In this paper, I argue that stylometric methods work because authors write in subtly different registers. To support this claim, I present the results of parallel stylometric and multidimensional register analyses of a corpus of newspaper articles written by two columnists. I demonstrate that both analyses not only distinguish between these authors but identify the same underlying patterns of linguistic variation. I therefore propose that register variation, as opposed to dialect variation, provides a basis for explaining these differences and for explaining stylometric analyses of authorship more generally.</span></span></td>
      <td>Jack Grieve</td>
      <td><a href="https://doi.org/doi:10.1515/cllt-2022-0040">link</a></td>
      <td>2023</td>
      <td>Corpus Linguistics and Linguistic Theory, 19(1):47–77</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>The sociolinguistic foundations of language modeling</em><span class="tooltip">In this article, we introduce a sociolinguistic perspective on language modeling. We claim that language models in general are inherently modeling varieties of language , and we consider how this insight can inform the development and deployment of language models. We begin by presenting a technical definition of the concept of a variety of language as developed in sociolinguistics. We then discuss how this perspective could help us better understand five basic challenges in language modeling: social bias, domain adaptation, alignment, language change , and scale . We argue that to maximize the performance and societal value of language models it is important to carefully compile training corpora that accurately represent the specific varieties of language being modeled, drawing on theories, methods, and descriptions from the field of sociolinguistics.</span></span></td>
      <td>Jack Grieve, Sara Bartl, Matteo Fuoli, Jason Grafmiller, Weihang Huang, Alejandro Jawerbaum, Akira Murakami, Marcus Perlman, Dana Roemling, and Bodo Winter</td>
      <td><a href="https://doi.org/10.3389/frai.2024.1472411">link</a></td>
      <td>2025</td>
      <td>Frontiers in Artificial Intelligence, 7:1472411</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Variation among blogs: A multi-dimensional analysis</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Jack Grieve, Douglas Biber, Eric Friginal, and Tatiana Nekrasova</td>
      <td><a href="https://doi.org/10.1007/978-90-481-9178-9_14">link</a></td>
      <td>2011</td>
      <td>Genres on the Web, pages 303–322</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Benchmarking Linguistic Diversity of Large Language Models</em><span class="tooltip">The development and evaluation of Large Language Models (LLMs) has primarily focused on their task-solving capabilities, with recent models even surpassing human performance in some areas. However, this focus often neglects whether machine-generated language matches the human level of diversity, in terms of vocabulary choice, syntactic construction, and expression of meaning, raising questions about whether the fundamentals of language generation have been fully addressed. This paper emphasizes the importance of examining the preservation of human linguistic richness by language models, given the concerning surge in online content produced or aided by LLMs. We propose a comprehensive framework for evaluating LLMs from various linguistic diversity perspectives including lexical, syntactic, and semantic dimensions. Using this framework, we benchmark several state-of-the-art LLMs across all diversity dimensions, and conduct an in-depth case study for syntactic diversity. Finally, we analyze how different development and deployment choices impact the linguistic diversity of LLM outputs.</span></span></td>
      <td>Yanzhu Guo, Guokan Shang, and Chloé Clavel</td>
      <td><a href="https://doi.org/10.48550/arXiv.2412.10271">link</a></td>
      <td>2025</td>
      <td>arXiv preprint ArXiv:2412.10271</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>The curious decline of linguistic diversity: Training language models on synthetic text</em><span class="tooltip">This study investigates the consequences of training language models on synthetic data generated by their predecessors, an increasingly prevalent practice given the prominence of powerful generative models. Diverging from the usual emphasis on performance metrics, we focus on the impact of this training methodology on linguistic diversity, especially when conducted recursively over time. To assess this, we adapt and develop a set of novel metrics targeting lexical, syntactic, and semantic diversity, applying them in recursive finetuning experiments across various natural language generation tasks in English. Our findings reveal a consistent decrease in the diversity of the model outputs through successive iterations, especially remarkable for tasks demanding high levels of creativity. This trend underscores the potential risks of training language models on synthetic text, particularly concerning the preservation of linguistic richness. Our study highlights the need for careful consideration of the long-term effects of such training approaches on the linguistic capabilities of language models.</span></span></td>
      <td>Yanzhu Guo, Guokan Shang, Michalis Vazirgiannis, and Chloé Clavel</td>
      <td><a href="https://doi.org/10.18653/v1/2024.findings-naacl.228">link</a></td>
      <td>2024</td>
      <td>Findings of NAACL 2024, pages 3589–3604</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Annotation artifacts in natural language inference data</em><span class="tooltip">Large-scale datasets for natural language inference are created by presenting crowd workers with a sentence (premise), and asking them to generate three new sentences (hypotheses) that it entails, contradicts, or is logically neutral with respect to. We show that, in a significant portion of such data, this protocol leaves clues that make it possible to identify the label by looking only at the hypothesis, without observing the premise. Specifically, we show that a simple text categorization model can correctly classify the hypothesis alone in about 67% of SNLI (Bowman et. al, 2015) and 53% of MultiNLI (Williams et. al, 2017). Our analysis reveals that specific linguistic phenomena such as negation and vagueness are highly correlated with certain inference classes. Our findings suggest that the success of natural language inference models to date has been overestimated, and that the task remains a hard open problem.</span></span></td>
      <td>Suchin Gururangan, Swabha Swayamdipta, Omer Levy, Roy Schwartz, Samuel Bowman, and Noah A. Smith</td>
      <td><a href="https://doi.org/10.18653/v1/N18-2017">link</a></td>
      <td>2018</td>
      <td>NAACL, pages 107–112</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Towards style alignment in cross-cultural translation</em><span class="tooltip">Successful communication depends on the speaker’s intended style (i.e., what the speaker is trying to convey) aligning with the listener’s interpreted style (i.e., what the listener perceives). However, cultural differences often lead to misalignment between the two; for example, politeness is often lost in translation. We characterize the ways that LLMs fail to translate style – biasing translations towards neutrality and performing worse in non-Western languages. We mitigate these failures with RASTA (Retrieval-Augmented STylistic Alignment), a method that leverages learned stylistic concepts to encourage LLM translation to appropriately convey cultural communication norms and align style.</span></span></td>
      <td>Shreya Havaldar, Adam Stein, Eric Wong, and Lyle Ungar</td>
      <td><a href="https://doi.org/10.18653/v1/2025.acl-long.1550">link</a></td>
      <td>2025</td>
      <td>ACL, pages 32213–32230</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Representation learning of writing style</em><span class="tooltip">In this paper, we introduce a new method of representation learning that aims to embed documents in a stylometric space. Previous studies in the field of authorship analysis focused on feature engineering techniques in order to represent document styles and to enhance model performance in specific tasks. Instead, we directly embed documents in a stylometric space by relying on a reference set of authors and the intra-author consistency property which is one of two components in our definition of writing style. The main intuition of this paper is that we can define a general stylometric space from a set of reference authors such that, in this space, the coordinates of different documents will be close when the documents are by the same author, and spread away when they are by different authors, even for documents by authors who are not in the set of reference authors. The method we propose allows for the clustering of documents based on stylistic clues reflecting the authorship of documents. For the empirical validation of the method, we train a deep neural network model to predict authors of a large reference dataset consisting of news and blog articles. Albeit the learning process is supervised, it does not require a dedicated labeling of the data but it relies only on the metadata of the articles which are available in huge amounts. We evaluate the model on multiple datasets, on both the authorship clustering and the authorship attribution tasks.</span></span></td>
      <td>Julien Hay, Bich-Lien Doan, Fabrice Popineau, and Ouassim Ait Elhara</td>
      <td><a href="https://doi.org/10.18653/v1/2020.wnut-1.30">link</a></td>
      <td>2020</td>
      <td>W-NUT 2020, pages 232–243</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Measuring Mathematical Problem Solving With the MATH Dataset</em><span class="tooltip">Many intellectual endeavors require mathematical problem solving, but this skill remains beyond the capabilities of computers. To measure this ability in machine learning models, we introduce MATH, a new dataset of 12,500 challenging competition mathematics problems. Each problem in MATH has a full step-by-step solution which can be used to teach models to generate answer derivations and explanations. To facilitate future research and increase accuracy on MATH, we also contribute a large auxiliary pretraining dataset which helps teach models the fundamentals of mathematics. Even though we are able to increase accuracy on MATH, our results show that accuracy remains relatively low, even with enormous Transformer models. Moreover, we find that simply increasing budgets and model parameter counts will be impractical for achieving strong mathematical reasoning if scaling trends continue. While scaling Transformers is automatically solving most other text-based tasks, scaling is not currently solving MATH. To have more traction on mathematical problem solving we will likely need new algorithmic advancements from the broader research community.</span></span></td>
      <td>Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt</td>
      <td><a href="https://openreview.net/forum?id=7Bywt2mQsCe">link</a></td>
      <td>2021</td>
      <td>NeurIPS</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Looking for the inner music: Probing LLMs' understanding of literary style</em><span class="tooltip">Abstract Language models have the ability to identify the characteristics of much shorter literary passages than was thought feasible with traditional stylometry. We evaluate authorship and genre detection for a new corpus of literary novels. We find that a range of LLMs are able to distinguish authorship and genre, but that different models do so in different ways. Some models rely more on memorization, while others make greater use of author or genre characteristics learned during fine-tuning. We additionally use three methods – direct syntactic ablation of input text and two means of studying internal model values – to probe one high-performing LLM for features that characterize styles. We find that authorial style is easier to characterize than genre-level style and is more impacted by minor syntactic decisions and contextual word usage. However, some traits like pronoun usage and word order prove significant for defining both kinds of literary style.</span></span></td>
      <td>Rebecca M. M. Hicke and David Mimno</td>
      <td><a href="https://doi.org/10.1017/chr.2025.10003">link</a></td>
      <td>2025</td>
      <td>Computational Humanities Research, 1:e3</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>AI generates covertly racist decisions about people based on their dialect</em><span class="tooltip">Abstract Hundreds of millions of people now interact with language models, with uses ranging from help with writing 1,2 to informing hiring decisions 3 . However, these language models are known to perpetuate systematic racial prejudices, making their judgements biased in problematic ways about groups such as African Americans 4–7 . Although previous research has focused on overt racism in language models, social scientists have argued that racism with a more subtle character has developed over time, particularly in the United States after the civil rights movement 8,9 . It is unknown whether this covert racism manifests in language models. Here, we demonstrate that language models embody covert racism in the form of dialect prejudice, exhibiting raciolinguistic stereotypes about speakers of African American English (AAE) that are more negative than any human stereotypes about African Americans ever experimentally recorded. By contrast, the language models’ overt stereotypes about African Americans are more positive. Dialect prejudice has the potential for harmful consequences: language models are more likely to suggest that speakers of AAE be assigned less-prestigious jobs, be convicted of crimes and be sentenced to death. Finally, we show that current practices of alleviating racial bias in language models, such as human preference alignment, exacerbate the discrepancy between covert and overt stereotypes, by superficially obscuring the racism that language models maintain on a deeper level. Our findings have far-reaching implications for the fair and safe use of language technology.</span></span></td>
      <td>Valentin Hofmann, Pratyusha Ria Kalluri, Dan Jurafsky, and Sharese King</td>
      <td><a href="https://doi.org/10.1038/s41586-024-07856-5">link</a></td>
      <td>2024</td>
      <td>Nature, 633:147–154</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Intonation and referee design phenomena in the narrative speech of Black/biracial men</em><span class="tooltip">This study examines how men with one Black parent and one white parent variably construct their racial identities through both linguistic practice and explicit testimonials, with a specific focus on how this construction is realized in narratives about law enforcement. The data consist of interviews with five young men, aged 18-32, in Washington, D.C., and the analysis compares use of intonational phenomena associated with African American Language (AAL) in response to questions about aspects of their racial identities. Declarative intonational phrases from responses to questions were MAE-ToBi annotated and analyzed for use of intonational features subject to racialized stylistic variation, including use of L+H* versus H*, focus marking, and peak delay interval length. Results of multiple regression models indicate speakers avoid intonational features associated with AAL in police narratives, especially L+H* pitch accents with broad focus marking and longer peak delay intervals. These findings illuminate an important aspect of the relationship between linguistic performance and identity: both racial and linguistic identities are subject to topic and audience/referee-conditioned variation and individuals can use specific intonational variables to align themselves within specific audience and topic-influenced constraints. In the context of police narratives, avoidance of salient features of AAL intonation can serve as linguistic respectability politics; these speakers have motivation to employ linguistic behavior that distances them from the most societally and physically precarious implications of their identities.</span></span></td>
      <td>Nicole Holliday</td>
      <td><a href="https://doi.org/10.1177/00754242211024722">link</a></td>
      <td>2021</td>
      <td>Journal of English Linguistics, 49(3):283–304</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>The analysis of literary style – a review</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>David I. Holmes</td>
      <td><a href="https://doi.org/10.2307/2981893">link</a></td>
      <td>1985</td>
      <td>Journal of the Royal Statistical Society: Series A, 148(4):328–341</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>ParaGuide: Guided diffusion paraphrasers for plug-and-play textual style transfer</em><span class="tooltip">Textual style transfer is the task of transforming stylistic properties of text while preserving meaning. Target &quot;styles&quot; can be defined in numerous ways, ranging from single attributes (e.g. formality) to authorship (e.g. Shakespeare). Previous unsupervised style-transfer approaches generally rely on significant amounts of labeled data for only a fixed set of styles or require large language models. In contrast, we introduce a novel diffusion-based framework for general-purpose style transfer that can be flexibly adapted to arbitrary target styles at inference time. Our parameter-efficient approach, ParaGuide, leverages paraphrase-conditioned diffusion models alongside gradient-based guidance from both off-the-shelf classifiers and strong existing style embedders to transform the style of text while preserving semantic information. We validate the method on the Enron Email Corpus, with both human and automatic evaluations, and find that it outperforms strong baselines on formality, sentiment, and even authorship style transfer.</span></span></td>
      <td>Zachary Horvitz, Ajay Patel, Chris Callison-Burch, Zhou Yu, and Kathleen McKeown</td>
      <td><a href="https://doi.org/10.1609/aaai.v38i16.29780">link</a></td>
      <td>2024</td>
      <td>AAAI, pages 18216–18224</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>TinyStyler: Efficient few-shot text style transfer with authorship embeddings</em><span class="tooltip">The goal of text style transfer is to transform the style of texts while preserving their original meaning, often with only a few examples of the target style. Existing style transfer methods generally rely on the few-shot capabilities of large language models or on complex controllable text generation approaches that are inefficient and underperform on fluency metrics. We introduce TinyStyler, a lightweight but effective approach, which leverages a small language model (800M params) and pre-trained authorship embeddings to perform efficient, few-shot text style transfer. We evaluate on the challenging task of authorship style transfer and find TinyStyler outperforms strong approaches such as GPT-4. We also evaluate TinyStyler’s ability to perform text attribute style transfer (formal &lt;span class=tex-math&gt;↔</span></span></td>
      <td>Zachary Horvitz, Ajay Patel, Kanishk Singh, Chris Callison-Burch, Kathleen McKeown, and Zhou Yu</td>
      <td><a href="https://doi.org/10.18653/v1/2024.findings-emnlp.781">link</a></td>
      <td>2024</td>
      <td>Findings of EMNLP 2024, pages 13376–13390</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>N-gram feature selection for authorship identification</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>John Houvardas and Efstathios Stamatatos</td>
      <td><a href="https://doi.org/10.1007/11861461_10">link</a></td>
      <td>2006</td>
      <td>AIMSA'06, pages 77–86</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Demographic factors improve classification performance</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Dirk Hovy</td>
      <td><a href="https://doi.org/10.3115/v1/P15-1073">link</a></td>
      <td>2015</td>
      <td>ACL-IJCNLP, pages 752–762</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>"You Sound Just Like Your Father" Commercial Machine Translation Systems Include Stylistic Biases</em><span class="tooltip">The main goal of machine translation has been to convey the correct content. Stylistic considerations have been at best secondary. We show that as a consequence, the output of three commercial machine translation systems (Bing, DeepL, Google) make demographically diverse samples from five languages “sound” older and more male than the original. Our findings suggest that translation models reflect demographic bias in the training data. This opens up interesting new research avenues in machine translation to take stylistic considerations into account.</span></span></td>
      <td>Dirk Hovy, Federico Bianchi, and Tommaso Fornaciari</td>
      <td><a href="https://aclanthology.org/2020.acl-main.154/">link</a></td>
      <td>2020</td>
      <td>ACL, pages 1686–1690</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>The social impact of natural language processing</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Dirk Hovy and Shannon L. Spruit</td>
      <td><a href="https://doi.org/10.18653/v1/P16-2096">link</a></td>
      <td>2016</td>
      <td>ACL, pages 591–598</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Tagging Performance Correlates with Author Age</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Dirk Hovy and Anders Søgaard</td>
      <td><a href="https://doi.org/10.3115/v1/P15-2079">link</a></td>
      <td>2015</td>
      <td>ACL-IJCNLP, pages 483–488</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>The importance of modeling social factors of language: Theory and practice</em><span class="tooltip">Natural language processing (NLP) applications are now more powerful and ubiquitous than ever before. With rapidly developing (neural) models and ever-more available data, current NLP models have access to more information than any human speaker during their life. Still, it would be hard to argue that NLP models have reached human-level capacity. In this position paper, we argue that the reason for the current limitations is a focus on information content while ignoring language’s social factors. We show that current NLP systems systematically break down when faced with interpreting the social factors of language. This limits applications to a subset of information-related tasks and prevents NLP from reaching human-level performance. At the same time, systems that incorporate even a minimum of social factors already show remarkable improvements. We formalize a taxonomy of seven social factors based on linguistic theory and exemplify current failures and emerging successes for each of them. We suggest that the NLP community address social factors to get closer to the goal of human-like language understanding.</span></span></td>
      <td>Dirk Hovy and Diyi Yang</td>
      <td><a href="https://doi.org/10.18653/v1/2021.naacl-main.49">link</a></td>
      <td>2021</td>
      <td>NAACL, pages 588–602</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Authorship Attribution in the Era of LLMs: Problems, Methodologies, and Challenges</em><span class="tooltip">Accurate attribution of authorship is crucial for maintaining the integrity of digital content, improving forensic investigations, and mitigating the risks of misinformation and plagiarism. Addressing the imperative need for proper authorship attribution is essential to uphold the credibility and accountability of authentic authorship. The rapid advancements of Large Language Models (LLMs) have blurred the lines between human and machine authorship, posing significant challenges for traditional methods. We present a comprehensive literature review that examines the latest research on authorship attribution in the era of LLMs. This survey systematically explores the landscape of this field by categorizing four representative problems: (1) Human-written Text Attribution; (2) LLM-generated Text Detection; (3) LLM-generated Text Attribution; and (4) Human-LLM Co-authored Text Attribution. We also discuss the challenges related to ensuring the generalization and explainability of authorship attribution methods. Generalization requires the ability to generalize across various domains, while explainability emphasizes providing transparent and understandable insights into the decisions made by these models. By evaluating the strengths and limitations of existing methods and benchmarks, we identify key open problems and future research directions in this field. This literature review serves a roadmap for researchers and practitioners interested in understanding the state of the art in this rapidly evolving field. Additional resources and a curated list of papers are available and regularly updated at https://llm-authorship.github.io/.</span></span></td>
      <td>Baixiang Huang, Canyu Chen, and Kai Shu</td>
      <td><a href="https://doi.org/10.1145/3715073.3715076">link</a></td>
      <td>2025</td>
      <td>ACM SIGKDD Explorations Newsletter, 26(2):21–43</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Sparse autoencoders find highly interpretable features in language models</em><span class="tooltip">One of the roadblocks to a better understanding of neural networks&#x27; internals is \textit{polysemanticity}, where neurons appear to activate in multiple, semantically distinct contexts. Polysemanticity prevents us from identifying concise, human-understandable explanations for what neural networks are doing internally. One hypothesised cause of polysemanticity is \textit{superposition}, where neural networks represent more features than they have neurons by assigning features to an overcomplete set of directions in activation space, rather than to individual neurons. Here, we attempt to identify those directions, using sparse autoencoders to reconstruct the internal activations of a language model. These autoencoders learn sets of sparsely activating features that are more interpretable and monosemantic than directions identified by alternative approaches, where interpretability is measured by automated methods. Moreover, we show that with our learned set of features, we can pinpoint the features that are causally responsible for counterfactual behaviour on the indirect object identification task \citep{wang2022interpretability} to a finer degree than previous decompositions. This work indicates that it is possible to resolve superposition in language models using a scalable, unsupervised method. Our method may serve as a foundation for future mechanistic interpretability work, which we hope will enable greater model transparency and steerability.</span></span></td>
      <td>Robert Huben, Hoagy Cunningham, Logan Riggs Smith, Aidan Ewart, and Lee Sharkey</td>
      <td><a href="https://openreview.net/forum?id=F76bwRSLeK">link</a></td>
      <td>2024</td>
      <td>ICLR</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>"Style" as distinctiveness: the culture and ideology of linguistic differentiation</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Judith T. Irvine</td>
      <td><a href="https://doi.org/10.1017/CBO9780511613258.002">link</a></td>
      <td>2001</td>
      <td>Style and Sociolinguistic Variation, pages 21–43</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>The Million Authors Corpus: A Cross-Lingual and Cross-Domain Wikipedia Dataset for Authorship Verification</em><span class="tooltip">Authorship verification (AV) is a crucial task for applications like identity verification, plagiarism detection, and AI-generated text identification. However, datasets for training and evaluating AV models are primarily in English and primarily in a single domain. This precludes analysis of AV techniques for generalizability and can cause seemingly valid AV solutions to, in fact, rely on topic-based features rather than actual authorship features. To address this limitation, we introduce the Million Authors Corpus (), a novel dataset encompassing contributions from dozens of languages on Wikipedia. It includes only long and contiguous textual chunks taken from Wikipedia edits and links those texts to their authors. includes 60.08M textual chunks, contributed by 1.29M Wikipedia authors. It enables broad-scale cross-lingual and cross-domain AV evaluation to ensure accurate analysis of model capabilities that are not overly optimistic. We provide baseline evaluations using state-of-the-art AV models as well as information retrieval models that are not AV-specific in order to demonstrate ‘s unique cross-lingual and cross-domain ablation capabilities.</span></span></td>
      <td>Abraham Israeli, Shuai Liu, Jonathan May, and David Jurgens</td>
      <td><a href="https://doi.org/10.18653/v1/2025.findings-acl.1335">link</a></td>
      <td>2025</td>
      <td>Findings of ACL 2025, pages 25997–26017</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Style versus Content: A distinction without a (learnable) difference?</em><span class="tooltip">Textual style transfer involves modifying the style of a text while preserving its content. This assumes that it is possible to separate style from content. This paper investigates whether this separation is possible. We use sentiment transfer as our case study for style transfer analysis. Our experimental methodology frames style transfer as a multi-objective problem, balancing style shift with content preservation and fluency. Due to the lack of parallel data for style transfer we employ a variety of adversarial encoder-decoder networks in our experiments. Also, we use of a probing methodology to analyse how these models encode style-related features in their latent spaces. The results of our experiments which are further confirmed by a human evaluation reveal the inherent trade-off between the multiple style transfer objectives which indicates that style cannot be usefully separated from content within these style-transfer systems.</span></span></td>
      <td>Somayeh Jafaritazehjani, Gwénolé Lecorvé, Damien Lolive, and John Kelleher</td>
      <td><a href="https://doi.org/10.18653/v1/2020.coling-main.197">link</a></td>
      <td>2020</td>
      <td>COLING, pages 2169–2180</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Evaluating Style-Personalized Text Generation: Challenges and Directions</em><span class="tooltip">With the surge of large language models (LLMs) and their ability to produce customized output, style-personalized text generation--&quot;write like me&quot;--has become a rapidly growing area of interest. However, style personalization is highly specific, relative to every user, and depends strongly on the pragmatic context, which makes it uniquely challenging. Although prior research has introduced benchmarks and metrics for this area, they tend to be non-standardized and have known limitations (e.g., poor correlation with human subjects). LLMs have been found to not capture author-specific style well, it follows that the metrics themselves must be scrutinized carefully. In this work we critically examine the effectiveness of the most common metrics used in the field, such as BLEU, embeddings, and LLMs-as-judges. We evaluate these metrics using our proposed style discrimination benchmark, which spans eight diverse writing tasks across three evaluation settings: domain discrimination, authorship attribution, and LLM-generated personalized vs non-personalized discrimination. We find strong evidence that employing ensembles of diverse evaluation metrics consistently outperforms single-evaluator methods, and conclude by providing guidance on how to reliably assess style-personalized text generation.</span></span></td>
      <td>Anubhav Jangra, Bahareh Sarrafzadeh, Adrian de Wynter, Silviu Cucerzan, and Sujay Kumar Jauhar</td>
      <td><a href="https://doi.org/10.48550/arXiv.2508.06374">link</a></td>
      <td>2025</td>
      <td>arXiv preprint ArXiv:2508.06374</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Shakespearizing Modern Language Using Copy-Enriched Sequence to Sequence Models</em><span class="tooltip">Variations in writing styles are commonly used to adapt the content to a specific context, audience, or purpose. However, applying stylistic variations is still by and large a manual process, and there have been little efforts towards automating it. In this paper we explore automated methods to transform text from modern English to Shakespearean English using an end to end trainable neural model with pointers to enable copy action. To tackle limited amount of parallel data, we pre-train embeddings of words by leveraging external dictionaries mapping Shakespearean words to modern English words as well as additional text. Our methods are able to get a BLEU score of 31+, an improvement of ≈ 6 points above the strongest baseline. We publicly release our code to foster further research in this area.</span></span></td>
      <td>Harsh Jhamtani, Varun Gangal, Eduard Hovy, and Eric Nyberg</td>
      <td><a href="https://doi.org/10.18653/v1/W17-4902">link</a></td>
      <td>2017</td>
      <td>Workshop on Stylistic Variation, pages 10–19</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Mistral 7B</em><span class="tooltip">We introduce Mistral 7B v0.1, a 7-billion-parameter language model engineered for superior performance and efficiency. Mistral 7B outperforms Llama 2 13B across all evaluated benchmarks, and Llama 1 34B in reasoning, mathematics, and code generation. Our model leverages grouped-query attention (GQA) for faster inference, coupled with sliding window attention (SWA) to effectively handle sequences of arbitrary length with a reduced inference cost. We also provide a model fine-tuned to follow instructions, Mistral 7B -- Instruct, that surpasses the Llama 2 13B -- Chat model both on human and automated benchmarks. Our models are released under the Apache 2.0 license.</span></span></td>
      <td>Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier, Lélio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut Lavril, Thomas Wang, Timothée Lacroix, and William El Sayed</td>
      <td><a href="https://doi.org/10.48550/arXiv.2310.06825">link</a></td>
      <td>2023</td>
      <td>arXiv preprint ArXiv:2310.06825</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Deep learning for text style transfer: A survey</em><span class="tooltip">Abstract Text style transfer is an important task in natural language generation, which aims to control certain attributes in the generated text, such as politeness, emotion, humor, and many others. It has a long history in the field of natural language processing, and recently has re-gained significant attention thanks to the promising performance brought by deep neural models. In this article, we present a systematic survey of the research on neural text style transfer, spanning over 100 representative articles since the first neural text style transfer work in 2017. We discuss the task formulation, existing datasets and subtasks, evaluation, as well as the rich methodologies in the presence of parallel and non-parallel data. We also provide discussions on a variety of important topics regarding the future development of this task.1</span></span></td>
      <td>Di Jin, Zhijing Jin, Zhiting Hu, Olga Vechtomova, and Rada Mihalcea</td>
      <td><a href="https://doi.org/10.1162/coli_a_00426">link</a></td>
      <td>2022</td>
      <td>Computational Linguistics, 48(1):155–205</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Disentangled representation learning for non-parallel text style transfer</em><span class="tooltip">This paper tackles the problem of disentangling the latent representations of style and content in language models. We propose a simple yet effective approach, which incorporates auxiliary multi-task and adversarial objectives, for style prediction and bag-of-words prediction, respectively. We show, both qualitatively and quantitatively, that the style and content are indeed disentangled in the latent space. This disentangled latent representation learning can be applied to style transfer on non-parallel corpora. We achieve high performance in terms of transfer accuracy, content preservation, and language fluency, in comparison to various previous approaches.</span></span></td>
      <td>Vineet John, Lili Mou, Hareesh Bahuleyan, and Olga Vechtomova</td>
      <td><a href="https://doi.org/10.18653/v1/P19-1041">link</a></td>
      <td>2019</td>
      <td>ACL, pages 424–434</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Authorship attribution</em><span class="tooltip">Authorship attribution, the science of inferring characteristics of the author from the characteristics of documents written by that author, is a problem with a long history and a wide range of application. Recent work in “non-traditional” authorship attribution demonstrates the practicality of automatically analyzing documents based on authorial style, but the state of the art is confusing. Analyses are difficult to apply, little is known about type or rate of errors, and few “best practices” are available. In part because of this confusion, the field has perhaps had less uptake and general acceptance than is its due. This review surveys the history and present state of the discipline, presenting some comparative results when available. It shows, first, that the discipline is quite successful, even in difficult cases involving small documents in unfamiliar and less studied languages; it further analyzes the types of analysis and features used and tries to determine characteristics of well-performing systems, finally formulating these in a set of recommendations for best practices.</span></span></td>
      <td>Patrick Juola</td>
      <td><a href="https://doi.org/10.1561/1500000005">link</a></td>
      <td>2006</td>
      <td>Foundations and Trends in Information Retrieval, 1(3):233–334</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>JGAAP 4.0–A revised authorship attribution tool</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Patrick Juola, John Noecker Jr., Mike Ryan, and Sandy Speer</td>
      <td><a href="https://github.com/evllabs/JGAAP">link</a></td>
      <td>2009</td>
      <td>Digital Humanities</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>(male, bachelor) and (female, Ph.D) have different connotations: Parallelly annotated stylistic language dataset with multiple personas</em><span class="tooltip">Stylistic variation in text needs to be studied with different aspects including the writer’s personal traits, interpersonal relations, rhetoric, and more. Despite recent attempts on computational modeling of the variation, the lack of parallel corpora of style language makes it difficult to systematically control the stylistic change as well as evaluate such models. We release PASTEL, the parallel and annotated stylistic language dataset, that contains ~41K parallel sentences (8.3K parallel stories) annotated across different personas. Each persona has different styles in conjunction: gender, age, country, political view, education, ethnic, and time-of-writing. The dataset is collected from human annotators with solid control of input denotation: not only preserving original meaning between text, but promoting stylistic diversity to annotators. We test the dataset on two interesting applications of style language, where PASTEL helps design appropriate experiment and evaluation. First, in predicting a target style (e.g., male or female in gender) given a text, multiple styles of PASTEL make other external style variables controlled (or fixed), which is a more accurate experimental design. Second, a simple supervised model with our parallel text outperforms the unsupervised models using nonparallel text in style transfer. Our dataset is publicly available.</span></span></td>
      <td>Dongyeop Kang, Varun Gangal, and Eduard Hovy</td>
      <td><a href="https://doi.org/10.18653/v1/D19-1179">link</a></td>
      <td>2019</td>
      <td>EMNLP-IJCNLP, pages 1696–1706</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Style is NOT a single variable: Case Studies for Cross-Stylistic Language Understanding</em><span class="tooltip">Every natural text is written in some style. Style is formed by a complex combination of different stylistic factors, including formality markers, emotions, metaphors, etc. One cannot form a complete understanding of a text without considering these factors. The factors combine and co-vary in complex ways to form styles. Studying the nature of the covarying combinations sheds light on stylistic language in general, sometimes called cross-style language understanding. This paper provides the benchmark corpus (XSLUE) that combines existing datasets and collects a new one for sentence-level cross-style language understanding and evaluation. The benchmark contains text in 15 different styles under the proposed four theoretical groupings: figurative, personal, affective, and interpersonal groups. For valid evaluation, we collect an additional diagnostic set by annotating all 15 styles on the same text. Using XSLUE, we propose three interesting cross-style applications in classification, correlation, and generation. First, our proposed cross-style classifier trained with multiple styles together helps improve overall classification performance against individually-trained style classifiers. Second, our study shows that some styles are highly dependent on each other in human-written text. Finally, we find that combinations of some contradictive styles likely generate stylistically less appropriate text. We believe our benchmark and case studies help explore interesting future directions for cross-style research. The preprocessed datasets and code are publicly available.</span></span></td>
      <td>Dongyeop Kang and Eduard Hovy</td>
      <td><a href="https://doi.org/10.18653/v1/2021.acl-long.185">link</a></td>
      <td>2021</td>
      <td>ACL-IJCNLP, pages 2376–2387</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Function words in authorship attribution. from black magic to theory?</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Mike Kestemont</td>
      <td><a href="https://doi.org/10.3115/v1/W14-0908">link</a></td>
      <td>2014</td>
      <td>CLFL, pages 59–66</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>A deep metric learning approach to account linking</em><span class="tooltip">We consider the task of linking social media accounts that belong to the same author in an automated fashion on the basis of the content and meta-data of the corresponding document streams. We focus on learning an embedding that maps variable-sized samples of user activity–ranging from single posts to entire months of activity–to a vector space, where samples by the same author map to nearby points. Our approach does not require human-annotated data for training purposes, which allows us to leverage large amounts of social media content. The proposed model outperforms several competitive baselines under a novel evaluation framework modeled after established recognition benchmarks in other domains. Our method achieves high linking accuracy, even with small samples from accounts not seen at training time, a prerequisite for practical applications of the proposed linking framework.</span></span></td>
      <td>Aleem Khan, Elizabeth Fleming, Noah Schofield, Marcus Bishop, and Nicholas Andrews</td>
      <td><a href="https://doi.org/10.18653/v1/2021.naacl-main.415">link</a></td>
      <td>2021</td>
      <td>NAACL, pages 5275–5287</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Learning to generate text in arbitrary writing styles</em><span class="tooltip">Prior work in style-controlled text generation has focused on tasks such as emulating the style of prolific literary authors, producing formal or informal text, and mitigating toxicity of generated text. Plentiful demonstrations of these styles are available, and as a result modern language models are often able to emulate them, either via prompting or discriminative control. However, in applications such as writing assistants, it is desirable for language models to produce text in an author-specific style on the basis of a potentially small writing sample. For example, someone writing in a particular dialect may prefer writing suggestions that retain the same dialect. We find that instruction-tuned language models can struggle to reproduce author-specific style demonstrated in a prompt. Instead, we propose to guide a language model to generate text in a target style using contrastively-trained representations that capture stylometric features. Our approach (StyleMC) combines an author-adapted language model with sequence-level inference to improve stylistic consistency, and is found to be effective in a variety of conditions, including unconditional generation and style transfer. Additionally, we find that the proposed approach can serve as an effective anonymization method, by editing a document to mask authorship while preserving the original meaning</span></span></td>
      <td>Aleem Khan, Andrew Wang, Sophia Hager, and Nicholas Andrews</td>
      <td><a href="https://arxiv.org/abs/2312.17242">link</a></td>
      <td>2023</td>
      <td>arXiv:2312.17242</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Supervised contrastive learning</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Prannay Khosla, Piotr Teterwak, Chen Wang, Aaron Sarna, Yonglong Tian, Phillip Isola, Aaron Maschinot, Ce Liu, and Dilip Krishnan</td>
      <td><a href="https://proceedings.neurips.cc/paper_files/paper/2020/file/d89a66c7c80a29b1bdbab0f2a1a94af8-Paper.pdf">link</a></td>
      <td>2020</td>
      <td>NeurIPS, 33:18661–18673</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Leveraging Multilingual Training for Authorship Representation: Enhancing Generalization across Languages and Domains</em><span class="tooltip">Authorship representation (AR) learning, which models an author’s unique writing style, has demonstrated strong performance in authorship attribution tasks. However, prior research has primarily focused on monolingual settings—mostly in English—leaving the potential benefits of multilingual AR models underexplored. We introduce a novel method for multilingual AR learning that incorporates two key innovations: probabilistic content masking, which encourages the model to focus on stylistically indicative words rather than content-specific words, and language-aware batching, which improves contrastive learning by reducing cross-lingual interference. Our model is trained on over 4.5 million authors across 36 languages and 13 domains. It consistently outperforms monolingual baselines in 21 out of 22 non-English languages, achieving an average Recall@8 improvement of 4.85%, with a maximum gain of 15.91% in a single language. Furthermore, it exhibits stronger cross-lingual and cross-domain generalization compared to a monolingual model trained solely on English. Our analysis confirms the effectiveness of both proposed techniques, highlighting their critical roles in the model’s improved performance.</span></span></td>
      <td>Junghwan Kim, Haotian Zhang, and David Jurgens</td>
      <td><a href="https://aclanthology.org/2025.emnlp-main.1766/">link</a></td>
      <td>2025</td>
      <td>EMNLP, pages 34855–34880</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Working in Language and Law: A German Perspective</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Hannes Kniffka</td>
      <td><a href="https://books.google.com/books?id=tp2GDAAAQBAJ">link</a></td>
      <td>2007</td>
      <td>Palgrave Macmillan UK</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>What's in an embedding? analyzing word embeddings through multilingual evaluation</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Arne Köhn</td>
      <td><a href="https://doi.org/10.18653/v1/D15-1246">link</a></td>
      <td>2015</td>
      <td>EMNLP, pages 2067–2073</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Automatically categorizing written texts by author gender</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Moshe Koppel, Shlomo Argamon, and Anat Rachel Shimoni</td>
      <td><a href="https://doi.org/10.1093/llc/17.4.401">link</a></td>
      <td>2002</td>
      <td>Literary and Linguistic Computing, 17(4):401–412</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Stylometric detection of ai-generated text in twitter timelines</em><span class="tooltip">Recent advancements in pre-trained language models have enabled convenient methods for generating human-like text at a large scale. Though these generation capabilities hold great potential for breakthrough applications, it can also be a tool for an adversary to generate misinformation. In particular, social media platforms like Twitter are highly susceptible to AI-generated misinformation. A potential threat scenario is when an adversary hijacks a credible user account and incorporates a natural language generator to generate misinformation. Such threats necessitate automated detectors for AI-generated tweets in a given user&#x27;s Twitter timeline. However, tweets are inherently short, thus making it difficult for current state-of-the-art pre-trained language model-based detectors to accurately detect at what point the AI starts to generate tweets in a given Twitter timeline. In this paper, we present a novel algorithm using stylometric signals to aid detecting AI-generated tweets. We propose models corresponding to quantifying stylistic changes in human and AI tweets in two related tasks: Task 1 - discriminate between human and AI-generated tweets, and Task 2 - detect if and when an AI starts to generate tweets in a given Twitter timeline. Our extensive experiments demonstrate that the stylometric features are effective in augmenting the state-of-the-art AI-generated text detectors.</span></span></td>
      <td>Tharindu Kumarage, Joshua Garland, Amrita Bhattacharjee, Kirill Trapeznikov, Scott Ruston, and Huan Liu</td>
      <td><a href="https://arxiv.org/abs/2303.03697">link</a></td>
      <td>2023</td>
      <td>arXiv:2303.03697</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Sociolinguistic Patterns</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>William Labov</td>
      <td>-</td>
      <td>1972</td>
      <td>University of Pennsylvania Press</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>The Social Stratification of English in New York City, 2nd edition</em><span class="tooltip">One of the first accounts of social variation in language, this groundbreaking study founded the discipline of sociolinguistics, providing the model on which thousands of studies have been based. In this second edition, Labov looks back on forty years of sociolinguistic research, bringing the reader up to date on its methods, findings and achievements. In over thirty pages of new material, he explores the unforeseen implications of his earlier work, addresses the political issues involved, and evaluates the success of newer approaches to sociolinguistic investigation. In doing so, he reveals the outstanding accomplishments of sociolinguistics since his original study, which laid the foundations for studying language variation, introduced the crucial concept of the linguistic variable, and showed how variation across age groups is an indicator of language change. Bringing Labov&#x27;s pioneering study into the 21st century, this classic volume will remain the benchmark in the field for years to come.</span></span></td>
      <td>William Labov</td>
      <td><a href="https://doi.org/10.1017/CBO9780511618208">link</a></td>
      <td>2006</td>
      <td>Cambridge University Press</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Tulu 3: Pushing Frontiers in Open Language Model Post-Training</em><span class="tooltip">Language model post-training is applied to refine behaviors and unlock new skills across a wide range of recent language models, but open recipes for applying these techniques lag behind proprietary ones. The underlying training data and recipes for post-training are simultaneously the most important pieces of the puzzle and the portion with the least transparency. To bridge this gap, we introduce Tulu 3, a family of fully-open state-of-the-art post-trained models, alongside its data, code, and training recipes, serving as a comprehensive guide for modern post-training techniques. Tulu 3, which builds on Llama 3.1 base models, achieves results surpassing the instruct versions of Llama 3.1, Qwen 2.5, Mistral, and even closed models such as GPT-4o-mini and Claude 3.5-Haiku. The training algorithms for our models include supervised finetuning (SFT), Direct Preference Optimization (DPO), and a novel method we call Reinforcement Learning with Verifiable Rewards (RLVR). With Tulu 3, we introduce a multi-task evaluation scheme for post-training recipes with development and unseen evaluations, standard benchmark implementations, and substantial decontamination of existing open datasets on said benchmarks. We conclude with analysis and discussion of training methods that did not reliably improve performance. In addition to the Tulu 3 model weights and demo, we release the complete recipe -- including datasets for diverse core skills, a robust toolkit for data curation and evaluation, the training code and infrastructure, and, most importantly, a detailed report for reproducing and further adapting the Tulu 3 approach to more domains.</span></span></td>
      <td>Team Tulu, Nathan Lambert, Jacob Morrison, Valentina Pyatkin, et al.</td>
      <td><a href="https://doi.org/10.48550/arXiv.2411.15124">link</a></td>
      <td>2025</td>
      <td>arXiv preprint ArXiv:2411.15124</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Where does the sociolinguistic variable stop?</em><span class="tooltip">In 1972 Labov described the basic sociolinguistic question as the one ‘posed by the need to understand why anyone says anything’ (1972:207). Clearly the aim is very different from that of specifying the form of a grammar that generates all and only the well-formed sentences of a language. The goal is a theory of utterances. Moreover, the ‘why’ question can also be read as ‘what for’. What does anyone say anything for? I think we can safely say that this question places sociolinguistic analysis in a functional framework. If sociolinguistics looks for answers to the ‘why’ of saying something, it is seeking functional explanations.</span></span></td>
      <td>Beatriz R. Lavandera</td>
      <td><a href="https://doi.org/10.1017/S0047404500005510">link</a></td>
      <td>1978</td>
      <td>Language in Society, 7(2):171–192</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>LFTK: Handcrafted Features in Computational Linguistics</em><span class="tooltip">Past research has identified a rich set of handcrafted linguistic features that can potentially assist various tasks. However, their extensive number makes it difficult to effectively select and utilize existing handcrafted features. Coupled with the problem of inconsistent implementation across research works, there has been no categorization scheme or generally-accepted feature names. This creates unwanted confusion. Also, no actively-maintained open-source library extracts a wide variety of handcrafted features. The current handcrafted feature extraction practices have several inefficiencies, and a researcher often has to build such an extraction system from the ground up. We collect and categorize more than 220 popular handcrafted features grounded on past literature. Then, we conduct a correlation analysis study on several task-specific datasets and report the potential use cases of each feature. Lastly, we devise a multilingual handcrafted linguistic feature extraction system in a systematically expandable manner. We open-source our system to give the community a rich set of pre-implemented handcrafted features.</span></span></td>
      <td>Bruce W. Lee and Jason Lee</td>
      <td><a href="https://doi.org/10.18653/v1/2023.bea-1.1">link</a></td>
      <td>2023</td>
      <td>BEA 2023, pages 1–19</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Diverse Demonstrations Improve In-context Compositional Generalization</em><span class="tooltip">In-context learning has shown great success in i.i.d semantic parsing splits, where the training and test sets are drawn from the same distribution. In this setup, models are typically prompted with demonstrations that are similar to the input utterance. However, in the setup of compositional generalization, where models are tested on outputs with structures that are absent from the training set, selecting similar demonstrations is insufficient, as often no example will be similar enough to the input. In this work, we propose a method to select diverse demonstrations that aims to collectively cover all of the structures required in the output program, in order to encourage the model to generalize to new structures from these demonstrations. We empirically show that combining diverse demonstrations with in-context learning substantially improves performance across three compositional generalization semantic parsing datasets in the pure in-context learning setup and when combined with finetuning.</span></span></td>
      <td>Itay Levy, Ben Bogin, and Jonathan Berant</td>
      <td><a href="https://doi.org/10.18653/v1/2023.acl-long.78">link</a></td>
      <td>2023</td>
      <td>ACL, pages 1401–1422</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>TextBugger: Generating Adversarial Text Against Real-world Applications</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Jinfeng Li, Shouling Ji, Tianyu Du, Bo Li, and Ting Wang</td>
      <td><a href="https://doi.org/10.14722/ndss.2019.23138">link</a></td>
      <td>2019</td>
      <td>NDSS</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Towards robust and privacy-preserving text representations</em><span class="tooltip">Written text often provides sufficient clues to identify the author, their gender, age, and other important attributes. Consequently, the authorship of training and evaluation corpora can have unforeseen impacts, including differing model performance for different user groups, as well as privacy implications. In this paper, we propose an approach to explicitly obscure important author characteristics at training time, such that representations learned are invariant to these attributes. Evaluating on two tasks, we show that this leads to increased privacy in the learned representations, as well as more robust models to varying evaluation conditions, including out-of-domain corpora.</span></span></td>
      <td>Yitong Li, Timothy Baldwin, and Trevor Cohn</td>
      <td><a href="https://doi.org/10.18653/v1/P18-2005">link</a></td>
      <td>2018</td>
      <td>ACL, pages 25–30</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Textbooks Are All You Need II: phi-1.5 technical report</em><span class="tooltip">We continue the investigation into the power of smaller Transformer-based language models as initiated by \textbf{TinyStories} -- a 10 million parameter model that can produce coherent English -- and the follow-up work on \textbf{phi-1}, a 1.3 billion parameter model with Python coding performance close to the state-of-the-art. The latter work proposed to use existing Large Language Models (LLMs) to generate ``textbook quality&quot; data as a way to enhance the learning process compared to traditional web data. We follow the ``Textbooks Are All You Need&quot; approach, focusing this time on common sense reasoning in natural language, and create a new 1.3 billion parameter model named \textbf{phi-1.5}, with performance on natural language tasks comparable to models 5x larger, and surpassing most non-frontier LLMs on more complex reasoning tasks such as grade-school mathematics and basic coding. More generally, \textbf{phi-1.5} exhibits many of the traits of much larger LLMs, both good -- such as the ability to ``think step by step&quot; or perform some rudimentary in-context learning -- and bad, including hallucinations and the potential for toxic and biased generations -- encouragingly though, we are seeing improvement on that front thanks to the absence of web data. We open-source \textbf{phi-1.5} to promote further research on these urgent topics.</span></span></td>
      <td>Yuanzhi Li, Sébastien Bubeck, Ronen Eldan, Allie Del Giorno, Suriya Gunasekar, and Yin Tat Lee</td>
      <td><a href="https://doi.org/10.48550/arXiv.2309.05463">link</a></td>
      <td>2023</td>
      <td>arXiv preprint ArXiv:2309.05463</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>GPT detectors are biased against non-native English writers</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Weixin Liang, Mert Yuksekgonul, Yining Mao, Eric Wu, and James Zou</td>
      <td><a href="https://doi.org/10.1016/j.patter.2023.100779">link</a></td>
      <td>2023</td>
      <td>Patterns, 4(7):100779</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Let's Verify Step by Step</em><span class="tooltip">In recent years, large language models have greatly improved in their ability to perform complex multi-step reasoning. However, even state-of-the-art models still regularly produce logical mistakes. To train more reliable models, we can turn either to outcome supervision, which provides feedback for a final result, or process supervision, which provides feedback for each intermediate reasoning step. Given the importance of training reliable models, and given the high cost of human feedback, it is important to carefully compare the both methods. Recent work has already begun this comparison, but many questions still remain. We conduct our own investigation, finding that process supervision significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset. Our process-supervised model solves 78% of problems from a representative subset of the MATH test set. Additionally, we show that active learning significantly improves the efficacy of process supervision. To support related research, we also release PRM800K, the complete dataset of 800,000 step-level human feedback labels used to train our best reward model.</span></span></td>
      <td>Hunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe</td>
      <td><a href="https://openreview.net/forum?id=v8L0pN6EOi">link</a></td>
      <td>2023</td>
      <td>ICLR</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Style over Substance: Distilled Language Models Reason Via Stylistic Replication</em><span class="tooltip">Specialized reasoning language models (RLMs) have demonstrated that scaling test-time computation through detailed reasoning traces significantly enhances performance. Although these traces effectively facilitate knowledge distillation into smaller, instruction-tuned models, the precise nature of transferred reasoning remains unclear. In this study, we investigate to what extent distilled models internalize replicated stylistic patterns during reasoning. To this end, we systematically analyze reasoning traces, identifying structural and lexical patterns that characterize successful reasoning. We then introduce two new datasets -- a dataset of emergent reasoning traces and a synthetic dataset explicitly constructed to replicate these stylistic patterns -- to precisely examine their influence on distilled models&#x27; reasoning capabilities. We find that models trained on the synthetic traces achieve comparable performance, indicating that distilled reasoning abilities rely significantly on surface-level patterns. Surprisingly, we observe an increase in performance even when the synthetic traces are altered to lead to the wrong answer. Our findings highlight how stylistic patterns can be leveraged to efficiently enhance LM reasoning across diverse model families.</span></span></td>
      <td>Philip Lippmann and Jie Yang</td>
      <td><a href="https://arxiv.org/abs/2504.01738v3">link</a></td>
      <td>2025</td>
      <td>arXiv</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Anonymisation models for text data: State of the art, challenges and future directions</em><span class="tooltip">This position paper investigates the problem of automated text anonymisation, which is a prerequisite for secure sharing of documents containing sensitive information about individuals. We summarise the key concepts behind text anonymisation and provide a review of current approaches. Anonymisation methods have so far been developed in two fields with little mutual interaction, namely natural language processing and privacy-preserving data publishing. Based on a case study, we outline the benefits and limitations of these approaches and discuss a number of open challenges, such as (1) how to account for multiple types of semantic inferences, (2) how to strike a balance between disclosure risk and data utility and (3) how to evaluate the quality of the resulting anonymisation. We lay out a case for moving beyond sequence labelling models and incorporate explicit measures of disclosure risk into the text anonymisation process.</span></span></td>
      <td>Pierre Lison, Ildikó Pilán, David Sanchez, Montserrat Batet, and Lilja Øvrelid</td>
      <td><a href="https://doi.org/10.18653/v1/2021.acl-long.323">link</a></td>
      <td>2021</td>
      <td>ACL-IJCNLP, pages 4188–4203</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Enct5: A framework for fine-tuning t5 as non-autoregressive models</em><span class="tooltip">Pre-trained encoder-decoder transformer architectures have become increasingly popular recently with the advent of T5 models. T5 has also become more favorable over other architectures like BERT due to the amount of data that it is pre-trained on, increased scale of model parameter sizes and easy applicability to a diverse set of tasks due to the generative nature of the model. While being able to generalize to a wide variety of tasks, it is not clear that encoder-decoder architectures are the most efficient for fine-tuning tasks that don&#x27;t require auto-regressive decoding. In this work, we study fine-tuning pre-trained encoder-decoder models for tasks such as classification, multi-label classification, and structured prediction. We propose \textbf{EncT5}, a framework for these problems, and illustrate instantiations for these tasks. Our experiment results show that EncT5 has advantages over T5 such as efficiency and usability out performs BERT when evaluated on publicly available pre-trained checkpoints.</span></span></td>
      <td>Frederick Liu, Terry Huang, Shihang Lyu, Siamak Shakeri, Hongkun Yu, and Jing Li</td>
      <td><a href="https://arxiv.org/abs/2110.08426">link</a></td>
      <td>2022</td>
      <td>arXiv:2110.08426</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>A Survey of Personalized Large Language Models: Progress and Future Directions</em><span class="tooltip">Large Language Models (LLMs) excel in handling general knowledge tasks, yet they struggle with user-specific personalization, such as understanding individual emotions, writing styles, and preferences. Personalized Large Language Models (PLLMs) tackle these challenges by leveraging individual user data, such as user profiles, historical dialogues, content, and interactions, to deliver responses that are contextually relevant and tailored to each user&#x27;s specific needs. This is a highly valuable research topic, as PLLMs can significantly enhance user satisfaction and have broad applications in conversational agents, recommendation systems, emotion recognition, medical assistants, and more. This survey reviews recent advancements in PLLMs from three technical perspectives: prompting for personalized context (input level), finetuning for personalized adapters (model level), and alignment for personalized preferences (objective level). To provide deeper insights, we also discuss current limitations and outline several promising directions for future research. Updated information about this survey can be found at the https://github.com/JiahongLiu21/Awesome-Personalized-Large-Language-Models.</span></span></td>
      <td>Jiahong Liu, Zexuan Qiu, Zhongyang Li, Quanyu Dai, Wenhao Yu, Jieming Zhu, Minda Hu, Menglin Yang, Tat-Seng Chua, Irwin King</td>
      <td><a href="https://doi.org/10.48550/arXiv.2502.11528">link</a></td>
      <td>2025</td>
      <td>arXiv preprint ArXiv:2502.11528</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>RECAP: Retrieval-enhanced context-aware prefix encoder for personalized dialogue response generation</em><span class="tooltip">Endowing chatbots with a consistent persona is essential to an engaging conversation, yet it remains an unresolved challenge. In this work, we propose a new retrieval-enhanced approach for personalized response generation. Specifically, we design a hierarchical transformer retriever trained on dialogue domain data to perform personalized retrieval and a context-aware prefix encoder that fuses the retrieved information to the decoder more effectively. Extensive experiments on a real-world dataset demonstrate the effectiveness of our model at generating more fluent and personalized responses. We quantitatively evaluate our model’s performance under a suite of human and automatic metrics and find it to be superior compared to state-of-the-art baselines on English Reddit conversations.</span></span></td>
      <td>Shuai Liu, Hyundong Cho, Marjorie Freedman, Xuezhe Ma, and Jonathan May</td>
      <td><a href="https://doi.org/10.18653/v1/2023.acl-long.468">link</a></td>
      <td>2023</td>
      <td>ACL, pages 8404–8419</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>More than words: The influence of affective content and linguistic style matches in online reviews on conversion rates</em><span class="tooltip">Customers increasingly rely on other consumers&#x27; reviews to make purchase decisions online. New insights into the customer review phenomenon can be derived from studying the semantic content and style properties of verbatim customer reviews to examine their influence on online retail sites&#x27; conversion rates. The authors employ text mining to extract changes in affective content and linguistic style properties of customer book reviews on Amazon.com . A dynamic panel data model reveals that the influence of positive affective content on conversion rates is asymmetrical, such that greater increases in positive affective content in customer reviews have a smaller effect on subsequent increases in conversion rate. No such tapering-off effect occurs for changes in negative affective content in reviews. Furthermore, positive changes in affective cues and increasing congruence with the product interest group&#x27;s typical linguistic style directly and conjointly increase conversion rates. These findings suggest that managers should identify and promote the most influential reviews in a given product category, provide instructions to stimulate reviewers to write powerful reviews, and adapt the style of their own editorial reviews to the relevant product category.</span></span></td>
      <td>Stephan Ludwig, Ko de Ruyter, Max Friedman, Elisabeth Constantin Brüggen, Martin Wetzels, and Gerard Pfann</td>
      <td><a href="https://doi.org/10.1509/jm.11.0560">link</a></td>
      <td>2013</td>
      <td>Journal of Marketing, 77(1):87–103</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Politeness transfer: A tag and generate approach</em><span class="tooltip">This paper introduces a new task of politeness transfer which involves converting non-polite sentences to polite sentences while preserving the meaning. We also provide a dataset of more than 1.39 instances automatically labeled for politeness to encourage benchmark evaluations on this new task. We design a tag and generate pipeline that identifies stylistic attributes and subsequently generates a sentence in the target style while preserving most of the source content. For politeness as well as five other transfer tasks, our model outperforms the state-of-the-art methods on automatic metrics for content preservation, with a comparable or better performance on style transfer accuracy. Additionally, our model surpasses existing methods on human evaluations for grammaticality, meaning preservation and transfer accuracy across all the six style transfer tasks. The data and code is located at &lt;a href=https://github.com/tag-and-generate class=acl-markup-url&gt;https://github.com/tag-and-generate&lt;/a&gt;.</span></span></td>
      <td>Aman Madaan, Amrith Setlur, Tanmay Parekh, Barnabas Poczos, Graham Neubig, Yiming Yang, Ruslan Salakhutdinov, Alan W Black, and Shrimai Prabhumoye</td>
      <td><a href="https://doi.org/10.18653/v1/2020.acl-main.169">link</a></td>
      <td>2020</td>
      <td>ACL, pages 1869–1881</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Jointly learning author and annotated character n-gram embeddings: A case study in literary text</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Suraj Maharjan, Deepthi Mave, Prasha Shrestha, Manuel Montes, Fabio A. González, and Thamar Solorio</td>
      <td><a href="https://doi.org/10.26615/978-954-452-056-4_080">link</a></td>
      <td>2019</td>
      <td>RANLP 2019, pages 684–692</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Rephrasing the Web: A Recipe for Compute and Data-Efficient Language Modeling</em><span class="tooltip">Large language models are trained on massive scrapes of the web, which are often unstructured, noisy, and poorly phrased. Current scaling laws show that learning from such data requires an abundance of both compute and data, which grows with the size of the model being trained. This is infeasible both because of the large compute costs and duration associated with pre-training, and the impending scarcity of high-quality data on the web. In this work, we propose Web Rephrase Augmented Pre-training ($\textbf{WRAP}$) that uses an off-the-shelf instruction-tuned model prompted to paraphrase documents on the web in specific styles such as &quot;like Wikipedia&quot; or in &quot;question-answer format&quot; to jointly pre-train LLMs on real and synthetic rephrases. First, we show that using WRAP on the C4 dataset, which is naturally noisy, speeds up pre-training by $\sim3x$. At the same pre-training compute budget, it improves perplexity by more than 10% on average across different subsets of the Pile, and improves zero-shot question answer accuracy across 13 tasks by more than 2%. Second, we investigate the impact of the re-phrasing style on the performance of the model, offering insights into how the composition of the training data can impact the performance of LLMs in OOD settings. Our gains are attributed to the fact that re-phrased synthetic data has higher utility than just real data because it (i) incorporates style diversity that closely reflects downstream evaluation style, and (ii) has higher &#x27;quality&#x27; than web-scraped data.</span></span></td>
      <td>Pratyush Maini, Skyler Seto, He Bai, David Grangier, Yizhe Zhang, and Navdeep Jaitly</td>
      <td><a href="https://doi.org/10.48550/arXiv.2401.16380">link</a></td>
      <td>2024</td>
      <td>arXiv preprint ArXiv:2401.16380</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Counterfactual augmentation for robust authorship representation learning</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Hieu Man and Thien Huu Nguyen</td>
      <td><a href="https://doi.org/10.1145/3626772.3657956">link</a></td>
      <td>2024</td>
      <td>SIGIR '24, pages 2347–2351</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Language technologies as if people mattered: Centering communities in language technology development</em><span class="tooltip">In this position paper we argue that researchers interested in language and/or language technologies should attend to challenges of linguistic and algorithmic injustice together with language communities. We put forward that this can be done by drawing together diverse scholarly and experiential insights, building strong interdisciplinary teams, and paying close attention to the wider social, cultural and historical contexts of both language communities and the technologies we aim to develop.</span></span></td>
      <td>Nina Markl, Lauren Hall-Lew, and Catherine Lai</td>
      <td><a href="https://aclanthology.org/2024.lrec-main.881/">link</a></td>
      <td>2024</td>
      <td>LREC-COLING 2024, pages 10085–10099</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Umap: Uniform manifold approximation and projection for dimension reduction</em><span class="tooltip">UMAP (Uniform Manifold Approximation and Projection) is a novel manifold learning technique for dimension reduction. UMAP is constructed from a theoretical framework based in Riemannian geometry and algebraic topology. The result is a practical scalable algorithm that applies to real world data. The UMAP algorithm is competitive with t-SNE for visualization quality, and arguably preserves more of the global structure with superior run time performance. Furthermore, UMAP has no computational restrictions on embedding dimension, making it viable as a general purpose dimension reduction technique for machine learning.</span></span></td>
      <td>Leland McInnes, John Healy, and James Melville</td>
      <td><a href="https://arxiv.org/abs/1802.03426">link</a></td>
      <td>2020</td>
      <td>arXiv:1802.03426</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Introducing Sociolinguistics</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Miriam Meyerhoff</td>
      <td><a href="https://doi.org/10.4324/9780203966709">link</a></td>
      <td>2006</td>
      <td>Routledge</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Linguistic profiling of a neural language model</em><span class="tooltip">In this paper we investigate the linguistic knowledge learned by a Neural Language Model (NLM) before and after a fine-tuning process and how this knowledge affects its predictions during several classification problems. We use a wide set of probing tasks, each of which corresponds to a distinct sentence-level feature extracted from different levels of linguistic annotation. We show that BERT is able to encode a wide range of linguistic characteristics, but it tends to lose this information when trained on specific downstream tasks. We also find that BERT’s capacity to encode different kind of linguistic properties has a positive influence on its predictions: the more it stores readable linguistic information of a sentence, the higher will be its capacity of predicting the expected label assigned to that sentence.</span></span></td>
      <td>Alessio Miaschi, Dominique Brunato, Felice Dell'Orletta, and Giulia Venturi</td>
      <td><a href="https://doi.org/10.18653/v1/2020.coling-main.65">link</a></td>
      <td>2020</td>
      <td>COLING, pages 745–756</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Stranger than paradigms word embedding benchmarks don't align with morphology</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Timothee Mickus and Maria Copot</td>
      <td><a href="https://aclanthology.org/2024.scil-1.17/">link</a></td>
      <td>2024</td>
      <td>SCiL 2024, pages 173–189</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Investigating topic influence in authorship attribution</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>George K Mikros and Eleni K Argiri</td>
      <td><a href="https://ceur-ws.org/Vol-276/paper5.pdf">link</a></td>
      <td>2007</td>
      <td>SIGIR'07 Workshop</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>The signature stylometric system</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Peter Millican</td>
      <td><a href="https://www.philocomp.net/texts/signature.htm">link</a></td>
      <td>2003</td>
      <td>Software documentation, University of Oxford</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>State of what art? a call for multi-prompt LLM evaluation</em><span class="tooltip">Abstract Recent advances in LLMs have led to an abundance of evaluation benchmarks, which typically rely on a single instruction template per task. We create a large-scale collection of instruction paraphrases and comprehensively analyze the brittleness introduced by single-prompt evaluations across 6.5M instances, involving 20 different LLMs and 39 tasks from 3 benchmarks. We find that different instruction templates lead to very different performance, both absolute and relative. Instead, we propose a set of diverse metrics on multiple instruction paraphrases, specifically tailored for different use cases (e.g., LLM vs. downstream development), ensuring a more reliable and meaningful assessment of LLM capabilities. We show that our metrics provide new insights into the strengths and limitations of current LLMs.</span></span></td>
      <td>Moran Mizrahi, Guy Kaplan, Dan Malkin, Rotem Dror, Dafna Shahaf, and Gabriel Stanovsky</td>
      <td><a href="https://doi.org/10.1162/tacl_a_00681">link</a></td>
      <td>2024</td>
      <td>TACL, 12:933–949</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Inference in an authorship problem: A comparative study of discrimination methods applied to the authorship of the disputed federalist papers</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Frederick Mosteller and David L. Wallace</td>
      <td><a href="https://doi.org/10.1080/01621459.1963.10500849">link</a></td>
      <td>1963</td>
      <td>JASA, 58(302):275–309</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>MTEB: Massive Text Embedding Benchmark</em><span class="tooltip">Text embeddings are commonly evaluated on a small set of datasets from a single task not covering their possible applications to other tasks. It is unclear whether state-of-the-art embeddings on semantic textual similarity (STS) can be equally well applied to other tasks like clustering or reranking. This makes progress in the field difficult to track, as various models are constantly being proposed without proper evaluation. To solve this problem, we introduce the Massive Text Embedding Benchmark (MTEB). MTEB spans 8 embedding tasks covering a total of 58 datasets and 112 languages. Through the benchmarking of 33 models on MTEB, we establish the most comprehensive benchmark of text embeddings todate. We find that no particular text embedding method dominates across all tasks. This suggests that the field has yet to converge on a universal text embedding method and scale it up sufficiently to provide state-of-theart results on all embedding tasks. MTEB comes with open-source code and a public leaderboard at &lt;a href=https://github.com/embeddings-benchmark/mteb class=acl-markup-url&gt;https://github.com/embeddings-benchmark/mteb&lt;/a&gt;.</span></span></td>
      <td>Niklas Muennighoff, Nouamane Tazi, Loic Magne, and Nils Reimers</td>
      <td><a href="https://doi.org/10.18653/v1/2023.eacl-main.148">link</a></td>
      <td>2023</td>
      <td>EACL, pages 2014–2037</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>s1: Simple test-time scaling</em><span class="tooltip">Test-time scaling is a promising new approach to language modeling that uses extra test-time compute to improve performance. Recently, OpenAI&#x27;s o1 model showed this capability but did not publicly share its methodology, leading to many replication efforts. We seek the simplest approach to achieve test-time scaling and strong reasoning performance. First, we curate a small dataset s1K of 1,000 questions paired with reasoning traces relying on three criteria we validate through ablations: difficulty, diversity, and quality. Second, we develop budget forcing to control test-time compute by forcefully terminating the model&#x27;s thinking process or lengthening it by appending &quot;Wait&quot; multiple times to the model&#x27;s generation when it tries to end. This can lead the model to double-check its answer, often fixing incorrect reasoning steps. After supervised finetuning the Qwen2.5-32B-Instruct language model on s1K and equipping it with budget forcing, our model s1-32B exceeds o1-preview on competition math questions by up to 27% (MATH and AIME24). Further, scaling s1-32B with budget forcing allows extrapolating beyond its performance without test-time intervention: from 50% to 57% on AIME24. Our model, data, and code are open-source at https://github.com/simplescaling/s1</span></span></td>
      <td>Niklas Muennighoff, Zitong Yang, Weijia Shi, Xiang Lisa Li, Li Fei-Fei, Hannaneh Hajishirzi, Luke Zettlemoyer, Percy Liang, Emmanuel Candes, and Tatsunori Hashimoto</td>
      <td><a href="https://doi.org/10.48550/arXiv.2501.19393">link</a></td>
      <td>2025</td>
      <td>EMNLP, pages 20286–20332</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Does your style engage? linguistic styles of influencers and digital consumer engagement on youtube</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Ana Cristina Munaro, Renato Hübner Barcelos, Eliane Cristine Francisco Maffezzolli, João Pedro Santos Rodrigues, and Emerson Cabrera Paraiso</td>
      <td><a href="https://doi.org/10.1016/j.chb.2024.108217">link</a></td>
      <td>2024</td>
      <td>Computers in Human Behavior, 156(C)</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Surveying stylometry techniques and applications</em><span class="tooltip">The analysis of authorial style, termed stylometry, assumes that style is quantifiably measurable for evaluation of distinctive qualities. Stylometry research has yielded several methods and tools over the past 200 years to handle a variety of challenging cases. This survey reviews several articles within five prominent subtasks: authorship attribution, authorship verification, authorship profiling, stylochronometry, and adversarial stylometry. Discussions on datasets, features, experimental techniques, and recent approaches are provided. Further, a current research challenge lies in the inability of authorship analysis techniques to scale to a large number of authors with few text samples. Here, we perform an extensive performance analysis on a corpus of 1,000 authors to investigate authorship attribution, verification, and clustering using 14 algorithms from the literature. Finally, several remaining research challenges are discussed, along with descriptions of various open-source and commercial software that may be useful for stylometry subtasks.</span></span></td>
      <td>Tempestt Neal, Kalaivani Sundararajan, Aneez Fatima, Yiming Yan, Yingfei Xiang, and Damon Woodard</td>
      <td><a href="https://doi.org/10.1145/3132039">link</a></td>
      <td>2017</td>
      <td>ACM Computing Surveys, 50(6):86</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Collaborative growth: When large language models meet sociolinguistics</em><span class="tooltip">ABSTRACT Large Language Models (LLMs) have dramatically transformed the AI landscape. They can produce remarkable fluent text and exhibit a range of natural language understanding and generation capabilities. This article explores how LLMs might be used for sociolinguistic research and, conversely, how sociolinguistics can contribute to the development of LLMs. It argues that both areas of research will benefit from a thoughtful, engaging collaboration. Sociolinguists are not merely end users of LLMs; they have a crucial role to play in the development of LLMs.</span></span></td>
      <td>Dong Nguyen</td>
      <td><a href="https://doi.org/10.1111/lnc3.70010">link</a></td>
      <td>2025</td>
      <td>Language and Linguistics Compass, 19(2):e70010</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Computational sociolinguistics: A Survey</em><span class="tooltip">Language is a social phenomenon and variation is inherent to its social nature. Recently, there has been a surge of interest within the computational linguistics (CL) community in the social dimension of language. In this article we present a survey of the emerging field of “computational sociolinguistics” that reflects this increased interest. We aim to provide a comprehensive overview of CL research on sociolinguistic themes, featuring topics such as the relation between language and social identity, language use in social interaction, and multilingual communication. Moreover, we demonstrate the potential for synergy between the research communities involved, by showing how the large-scale data-driven methods that are widely used in CL can complement existing sociolinguistic studies, and how sociolinguistics can inform and challenge the methods and assumptions used in CL studies. We hope to convey the possible benefits of a closer collaboration between the two communities and conclude with a discussion of open challenges.</span></span></td>
      <td>Dong Nguyen, A. Seza Doğruöz, Carolyn P. Rosé, and Franciska de Jong</td>
      <td><a href="https://doi.org/10.1162/COLI_a_00258">link</a></td>
      <td>2016</td>
      <td>Computational Linguistics, 42(3):537–593</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>"How old do you think I am?" A study of language and age in Twitter</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Dong Nguyen, Rilana Gravel, Dolf Trieschnigg, and Theo Meder</td>
      <td><a href="https://ojs.aaai.org/index.php/ICWSM/article/view/14381">link</a></td>
      <td>2013</td>
      <td>ICWSM, pages 439–448</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Do word embeddings capture spelling variation?</em><span class="tooltip">Analyses of word embeddings have primarily focused on semantic and syntactic properties. However, word embeddings have the potential to encode other properties as well. In this paper, we propose a new perspective on the analysis of word embeddings by focusing on spelling variation. In social media, spelling variation is abundant and often socially meaningful. Here, we analyze word embeddings trained on Twitter and Reddit data. We present three analyses using pairs of word forms covering seven types of spelling variation in English. Taken together, our results show that word embeddings encode spelling variation patterns of various types to some extent, even embeddings trained using the skipgram model which does not take spelling into account. Our results also suggest a link between the intentionality of the variation and the distance of the non-conventional spellings to their conventional spellings.</span></span></td>
      <td>Dong Nguyen and Jack Grieve</td>
      <td><a href="https://doi.org/10.18653/v1/2020.coling-main.75">link</a></td>
      <td>2020</td>
      <td>COLING, pages 870–881</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>We Need to Measure Data Diversity in NLP – Better and Broader</em><span class="tooltip">Although diversity in NLP datasets has received growing attention, the question of how to measure it remains largely underexplored. This opinion paper examines the conceptual and methodological challenges of measuring data diversity and argues that interdisciplinary perspectives are essential for developing more fine-grained and valid measures.</span></span></td>
      <td>Dong Nguyen and Esther Ploeger</td>
      <td><a href="https://doi.org/10.48550/arXiv.2505.20264">link</a></td>
      <td>2025</td>
      <td>arXiv preprint ArXiv:2505.20264</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>On learning and representing social meaning in NLP: a sociolinguistic perspective</em><span class="tooltip">The field of NLP has made substantial progress in building meaning representations. However, an important aspect of linguistic meaning, social meaning, has been largely overlooked. We introduce the concept of social meaning to NLP and discuss how insights from sociolinguistics can inform work on representation learning in NLP. We also identify key challenges for this new line of research.</span></span></td>
      <td>Dong Nguyen, Laura Rosseel, and Jack Grieve</td>
      <td><a href="https://doi.org/10.18653/v1/2021.naacl-main.50">link</a></td>
      <td>2021</td>
      <td>NAACL, pages 603–612</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>The Multi-Dimensional Analysis Tagger</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Andrea Nini</td>
      <td><a href="https://sites.google.com/site/multidimensionaltagger/about?authuser=0">link</a></td>
      <td>2019</td>
      <td>Multi-Dimensional Analysis: Research Methods and Current Issues</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>A Theory of Linguistic Individuality for Authorship Analysis</em><span class="tooltip">This Element examines progress in research and practice in forensic authorship analysis. It describes the existing research base and examines what makes an authorship analysis more or less reliable. Further to this, the author describes the recent history of forensic science and the scientific revolution brought about by the invention of DNA evidence. They chart the rise of three major changes in forensic science – the recognition of contextual bias in analysts, the need for validation studies and shift in logic of providing identification evidence. This Element addresses the idea of progress in forensic authorship analysis in terms of these three issues with regard to new knowledge about the nature of authorship and methods in stylistics and stylometry. The author proposes that the focus needs to shift to validation of protocols for approaching case questions, rather than on validation of systems or general approaches. This title is also available as Open Access on Cambridge Core.</span></span></td>
      <td>Andrea Nini</td>
      <td><a href="https://doi.org/10.1017/9781108974714">link</a></td>
      <td>2023</td>
      <td>Cambridge University Press</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>A study of style in machine translation: Controlling the formality of machine translation output</em><span class="tooltip">Stylistic variations of language, such as formality, carry speakers’ intention beyond literal meaning and should be conveyed adequately in translation. We propose to use lexical formality models to control the formality level of machine translation output. We demonstrate the effectiveness of our approach in empirical evaluations, as measured by automatic metrics and human assessments.</span></span></td>
      <td>Xing Niu, Marianna Martindale, and Marine Carpuat</td>
      <td><a href="https://doi.org/10.18653/v1/D17-1299">link</a></td>
      <td>2017</td>
      <td>EMNLP, pages 2814–2819</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Multi-task neural models for translating between styles within and across languages</em><span class="tooltip">Generating natural language requires conveying content in an appropriate style. We explore two related tasks on generating text of varying formality: monolingual formality transfer and formality-sensitive machine translation. We propose to solve these tasks jointly using multi-task learning, and show that our models achieve state-of-the-art performance for formality transfer and are able to perform formality-sensitive translation without being explicitly trained on style-annotated translation examples.</span></span></td>
      <td>Xing Niu, Sudha Rao, and Marine Carpuat</td>
      <td><a href="https://aclanthology.org/C18-1086/">link</a></td>
      <td>2018</td>
      <td>COLING, pages 1008–1021</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>2 OLMo 2 Furious</em><span class="tooltip">We present OLMo 2, the next generation of our fully open language models. OLMo 2 includes a family of dense autoregressive language models at 7B, 13B and 32B scales with fully released artifacts -- model weights, full training data, training code and recipes, training logs and thousands of intermediate checkpoints. In this work, we describe our modified model architecture and training recipe, focusing on techniques for achieving better training stability and improved per-token efficiency. Our updated pretraining data mixture introduces a new, specialized data mix called Dolmino Mix 1124, which significantly improves model capabilities across many downstream task benchmarks when introduced via late-stage curriculum training (i.e. specialized data during the annealing phase of pretraining). Finally, we incorporate best practices from Tülu 3 to develop OLMo 2-Instruct, focusing on permissive data and extending our final-stage reinforcement learning with verifiable rewards (RLVR). Our OLMo 2 base models sit at the Pareto frontier of performance to training compute, often matching or outperforming open-weight only models like Llama 3.1, Qwen 2.5, and Gemma 2 while using fewer FLOPs and with fully transparent training data, code, and recipe. Our fully open OLMo 2-Instruct models are competitive with open-weight only models of comparable size and even some proprietary models like GPT-3.5 Turbo and GPT 4o Mini.</span></span></td>
      <td>Team OLMo, Pete Walsh, Luca Soldaini, et al.</td>
      <td><a href="https://doi.org/10.48550/arXiv.2501.00656">link</a></td>
      <td>2025</td>
      <td>arXiv preprint ArXiv:2501.00656</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Linguistic style and crowdfunding success among social and commercial entrepreneurs</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Annaleena Parhankangas and Maija Renko</td>
      <td><a href="https://doi.org/10.1016/j.jbusvent.2016.11.001">link</a></td>
      <td>2017</td>
      <td>Journal of Business Venturing, 32(2):215–236</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Learning interpretable style embeddings via prompting LLMs</em><span class="tooltip">Style representation learning builds content-independent representations of author style in text. To date, no large dataset of texts with stylometric annotations on a wide range of style dimensions has been compiled, perhaps because the linguistic expertise to perform such annotation would be prohibitively expensive. Therefore, current style representation approaches make use of unsupervised neural methods to disentangle style from content to create style vectors. These approaches, however, result in uninterpretable representations, complicating their usage in downstream applications like authorship attribution where auditing and explainability is critical. In this work, we use prompting to perform stylometry on a large number of texts to generate a synthetic stylometry dataset. We use this synthetic data to then train human-interpretable style representations we call LISA embeddings. We release our synthetic dataset (StyleGenome) and our interpretable style embedding model (LISA) as resources.</span></span></td>
      <td>Ajay Patel, Delip Rao, Ansh Kothary, Kathleen McKeown, and Chris Callison-Burch</td>
      <td><a href="https://doi.org/10.18653/v1/2023.findings-emnlp.1020">link</a></td>
      <td>2023</td>
      <td>Findings of EMNLP 2023, pages 15270–15290</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>StyleDistance: Stronger content-independent style embeddings with synthetic parallel examples</em><span class="tooltip">Style representations aim to embed texts with similar writing styles closely and texts with different styles far apart, regardless of content. However, the contrastive triplets often used for training these representations may vary in both style and content, leading to potential content leakage in the representations. We introduce StyleDistance, a novel approach to training stronger content-independent style embeddings. We use a large language model to create a synthetic dataset of near-exact paraphrases with controlled style variations, and produce positive and negative examples across 40 distinct style features for precise contrastive learning. We assess the quality of our synthetic data and embeddings through human and automatic evaluations. StyleDistance enhances the content-independence of style embeddings, which generalize to real-world benchmarks and outperform leading style representations in downstream applications.</span></span></td>
      <td>Ajay Patel, Jiacheng Zhu, Justin Qiu, Zachary Horvitz, Marianna Apidianaki, Kathleen McKeown, and Chris Callison-Burch</td>
      <td><a href="https://doi.org/10.18653/v1/2025.naacl-long.436">link</a></td>
      <td>2025</td>
      <td>NAACL, pages 8662–8685</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Language independent authorship attribution using character level language models</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Fuchun Peng, Dale Schuurmans, Shaojun Wang, and Vlado Keselj</td>
      <td><a href="https://doi.org/10.3115/1067807.1067843">link</a></td>
      <td>2003</td>
      <td>EACL, pages 267–274</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>The Development and Psychometric Properties of LIWC2015</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>James W. Pennebaker, Ryan L. Boyd, Kayla Jordan, and Kate Blackburn</td>
      <td><a href="https://doi.org/10.15781/T29G6Z">link</a></td>
      <td>2015</td>
      <td>University of Texas at Austin</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>JSAN–The Integrated JStylo and Anonymouth Package</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Drexel University PSAL</td>
      <td><a href="https://github.com/psal/jstylo">link</a></td>
      <td>2013</td>
      <td>Drexel University</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Mind the style of text! adversarial and backdoor attacks based on text style transfer</em><span class="tooltip">Definition generation, which aims to automatically generate dictionary definitions for words, has recently been proposed to assist the construction of dictionaries and help people understand unfamiliar texts. However, previous works hardly consider explicitly modeling the “components” of definitions, leading to under-specific generation results. In this paper, we propose ESD, namely Explicit Semantic Decomposition for definition Generation, which explicitly decomposes the meaning of words into semantic components, and models them with discrete latent variables for definition generation. Experimental results show that achieves top results on WordNet and Oxford benchmarks, outperforming strong previous baselines.</span></span></td>
      <td>Fanchao Qi, Yangyi Chen, Xurui Zhang, Mukai Li, Zhiyuan Liu, and Maosong Sun</td>
      <td><a href="https://doi.org/10.18653/v1/2020.acl-main.65">link</a></td>
      <td>2021</td>
      <td>EMNLP, pages 4569–4580</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>mStyleDistance: Multilingual style embeddings and their evaluation</em><span class="tooltip">Style embeddings are useful for stylistic analysis and style transfer, yet they only exist for English. We introduce Multilingual StyleDistance (mStyleDistance), a method that can generate style embeddings in new languages using synthetic data and a contrastive loss. We create style embeddings in nine languages and a multilingual STEL-or-Content benchmark (Wegmann et al., 2022) that serves to assess their quality. We also employ our embeddings in an authorship verification task involving different languages. Our results show that mStyleDistance embeddings outperform existing style embeddings on these benchmarks and generalize well to unseen features and languages. We make our models and datasets publicly available.</span></span></td>
      <td>Justin Qiu, Jiacheng Zhu, Ajay Patel, Marianna Apidianaki, and Chris Callison-Burch</td>
      <td><a href="https://doi.org/10.18653/v1/2025.findings-acl.869">link</a></td>
      <td>2025</td>
      <td>Findings of ACL 2025, pages 16917–16931</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Personalized machine translation: Preserving original author traits</em><span class="tooltip">The language that we produce reflects our personality, and various personal and demographic characteristics can be detected in natural language texts. We focus on one particular personal trait of the author, gender, and study how it is manifested in original texts and in translations. We show that author’s gender has a powerful, clear signal in originals texts, but this signal is obfuscated in human and machine translation. We then propose simple domain-adaptation techniques that help retain the original gender traits in the translation, without harming the quality of the translation, thereby creating more personalized machine translation systems.</span></span></td>
      <td>Ella Rabinovich, Raj Nath Patel, Shachar Mirkin, Lucia Specia, and Shuly Wintner</td>
      <td><a href="https://aclanthology.org/E17-1101/">link</a></td>
      <td>2017</td>
      <td>EACL, pages 1074–1084</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Overview of the author profiling task at PAN 2013</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Francisco Rangel, Paolo Rosso, Moshe Koppel, Efstathios Stamatatos, and Giacomo Inches</td>
      <td><a href="https://ceur-ws.org/Vol-1179/CLEF2013wn-PAN-RangelEt2013.pdf">link</a></td>
      <td>2013</td>
      <td>CLEF</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Dear sir or madam, may I introduce the GYAFC dataset: Corpus, benchmarks and metrics for formality style transfer</em><span class="tooltip">Style transfer is the task of automatically transforming a piece of text in one particular style into another. A major barrier to progress in this field has been a lack of training and evaluation datasets, as well as benchmarks and automatic metrics. In this work, we create the largest corpus for a particular stylistic transfer (formality) and show that techniques from the machine translation community can serve as strong baselines for future work. We also discuss challenges of using automatic metrics.</span></span></td>
      <td>Sudha Rao and Joel Tetreault</td>
      <td><a href="https://doi.org/10.18653/v1/N18-1012">link</a></td>
      <td>2018</td>
      <td>NAACL, pages 129–140</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>A recipe for arbitrary text style transfer with large language models</em><span class="tooltip">In this paper, we leverage large language models (LLMs) to perform zero-shot text style transfer. We present a prompting method that we call augmented zero-shot learning, which frames style transfer as a sentence rewriting task and requires only a natural language instruction, without model fine-tuning or exemplars in the target style. Augmented zero-shot learning is simple and demonstrates promising results not just on standard style transfer tasks such as sentiment, but also on arbitrary transformations such as ‘make this melodramatic’ or ‘insert a metaphor.’</span></span></td>
      <td>Emily Reif, Daphne Ippolito, Ann Yuan, Andy Coenen, Chris Callison-Burch, and Jason Wei</td>
      <td><a href="https://doi.org/10.18653/v1/2022.acl-short.94">link</a></td>
      <td>2022</td>
      <td>ACL, pages 837–848</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Addressee- and topic-influenced style shift: A quantitative sociolinguistic study</em><span class="tooltip">Abstract This chapter is a study of addressee-and topic-influenced style shift in language, within the framework of quantitative or “variationist” sociolinguistics. The first section is written from a theoretical, history-of-science perspective; we begin by contrasting the taxonomic, polydimensional approach of sociolinguists like Hymes (1972) and Halliday (1978) with the empirical, unidimensional approach of Labov (1966:90-135, 1972a:70-109), for whom styles were ordered on a single dimension, involving attention paid to speech. We suggest that the neglect of style within the American variationist school from the 1970s onward was due in part to methodological and theoretical difficulties with this approach. As we note, an alternative unidimensional approach, considering style as audience accommodation (Giles and Powesland 1975, Bell 1984), is more promising, but although several quantitative studies within this framework have been made over the past decade and a half, most of them were done outside the United States, primarily in Britain.</span></span></td>
      <td>John R. Rickford and Faye McNair-Knox</td>
      <td><a href="https://doi.org/10.1093/oso/9780195083644.003.0011">link</a></td>
      <td>1994</td>
      <td>Sociolinguistic Perspectives on Register, pages 235–276</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Few-shot detection of machine-generated text using style representations</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Rafael Rivera Soto, Kailin Koch, Aleem Khan, Barry Y. Chen, Marcus Bishop, and Nicholas Andrews</td>
      <td><a href="https://iclr.cc/virtual/2024/poster/18293">link</a></td>
      <td>2024</td>
      <td>ICLR</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Learning universal authorship representations</em><span class="tooltip">Determining whether two documents were composed by the same author, also known as authorship verification, has traditionally been tackled using statistical methods. Recently, authorship representations learned using neural networks have been found to outperform alternatives, particularly in large-scale settings involving hundreds of thousands of authors. But do such representations learned in a particular domain transfer to other domains? Or are these representations inherently entangled with domain-specific features? To study these questions, we conduct the first large-scale study of cross-domain transfer for authorship verification considering zero-shot transfers involving three disparate domains: Amazon reviews, fanfiction short stories, and Reddit comments. We find that although a surprising degree of transfer is possible between certain domains, it is not so successful between others. We examine properties of these domains that influence generalization and propose simple but effective methods to improve transfer.</span></span></td>
      <td>Rafael Rivera Soto, Olivia Elizabeth Miano, Juanita Ordonez, Barry Y. Chen, Aleem Khan, Marcus Bishop, and Nicholas Andrews</td>
      <td><a href="https://aclanthology.org/2021.emnlp-main.70/">link</a></td>
      <td>2021</td>
      <td>EMNLP, main paper</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>My LLM might Mimic AAE - But When Should It?</em><span class="tooltip">We examine the representation of African American English (AAE) in large language models (LLMs), exploring (a) the perceptions Black Americans have of how effective these technologies are at producing authentic AAE, and (b) in what contexts Black Americans find this desirable. Through both a survey of Black Americans (&lt;span class=tex-math&gt;n=</span></span></td>
      <td>Sandra Camille Sandoval, Christabel Acquaye, Kwesi Adu Cobbina, Mohammad Nayeem Teli, and Hal Daumé Iii</td>
      <td><a href="https://doi.org/10.18653/v1/2025.naacl-long.273">link</a></td>
      <td>2025</td>
      <td>NAACL, pages 5277–5302</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Topic-regularized authorship representation learning</em><span class="tooltip">Authorship attribution is a task that aims to identify the author of a given piece of writing. We aim to develop a generalized solution that can handle a large number of texts from authors and topics unavailable in training data. Previous studies have proposed strategies to address only either unseen authors or unseen topics. Authorship representation learning has been shown to work in open-set environments with a large number of unseen authors but has not been explicitly designed for cross-topic environments at the same time. To handle a large number of unseen authors and topics, we propose Authorship Representation Regularization (ARR), a distillation framework that creates authorship representation with reduced reliance on topic-specific information. To assess the performance of our framework, we also propose a cross-topic-open-set evaluation method. Our proposed method has improved performances in the cross-topic-open set setup over baselines in 4 out of 6 cases.</span></span></td>
      <td>Jitkapat Sawatphol, Nonthakit Chaiwong, Can Udomcharoenchaikit, and Sarana Nutanong</td>
      <td><a href="https://doi.org/10.18653/v1/2022.emnlp-main.70">link</a></td>
      <td>2022</td>
      <td>EMNLP, pages 1076–1082</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Addressing Topic Leakage in Cross-Topic Evaluation for Authorship Verification</em><span class="tooltip">Abstract Authorship verification (AV) aims to identify whether a pair of texts has the same author. We address the challenge of evaluating AV models’ robustness against topic shifts. The conventional evaluation assumes minimal topic overlap between training and test data. However, we argue that there can still be topic leakage in test data, causing misleading model performance and unstable rankings. To address this, we propose an evaluation method called Heterogeneity-Informed Topic Sampling (HITS), which creates a smaller dataset with a heterogeneously distributed topic set. Our experimental results demonstrate that HITS-sampled datasets yield a more stable ranking of models across random seeds and evaluation splits. Our contributions include: 1. An analysis of causes and effects of topic leakage; 2. A demonstration of the HITS in reducing the effects of topic leakage; and 3. The Robust Authorship Verification bENchmark (RAVEN) that allows topic shortcut test to uncover AV models’ reliance on topic-specific features.</span></span></td>
      <td>Jitkapat Sawatphol, Can Udomcharoenchaikit, and Sarana Nutanong</td>
      <td><a href="https://doi.org/10.1162/tacl_a_00709">link</a></td>
      <td>2024</td>
      <td>TACL, 12:1363–1377</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>MATCHED: Multimodal Authorship-Attribution To Combat Human Trafficking in Escort-Advertisement Data</em><span class="tooltip">Human trafficking (HT) remains a critical issue, with traffickers increasingly leveraging online escort advertisements to advertise victims anonymously. Existing detection methods, including text-based Authorship Attribution (AA), overlook the multimodal nature of these ads, which combine text and images. To bridge this gap, we introduce MATCHED, a multimodal AA dataset comprising 27,619 unique text descriptions and 55,115 unique images sourced from Backpage across seven U.S. cities in four geographic regions. This study extensively benchmarks text-only, vision-only, and multimodal baselines for vendor identification and verification tasks, employing multitask (joint) training objectives that achieve superior classification and retrieval performance on in-sample and out-of-data distribution datasets. The results demonstrate that while text remains the dominant modality, integrating visual features adds stylistic cues that enrich model performance. Moreover, text-image alignment strategies like CLIP and BLIP2 struggle due to low semantic overlap and vague connections between the modalities of escort ads, with end-to-end multimodal training proving more robust. Our findings emphasize the potential of multimodal AA to combat HT, providing Law Enforcement Agencies with robust tools to link advertisements and disrupt trafficking networks.</span></span></td>
      <td>Vageesh Kumar Saxena, Benjamin Ashpole, Gijs Van Dijck, and Gerasimos Spanakis</td>
      <td><a href="https://doi.org/10.18653/v1/2025.findings-acl.225">link</a></td>
      <td>2025</td>
      <td>Findings of ACL 2025, pages 4334–4373</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Frequent-words analysis for forensic speaker comparison</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Eleni-Konstantina Sergidou, Nelleke Scheijen, Jeannette Leegwater, Tina Cambier-Langeveld, and Wauter Bosma</td>
      <td><a href="https://doi.org/10.1016/j.specom.2023.03.010">link</a></td>
      <td>2023</td>
      <td>Speech Communication, 150:1–8</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>The power of words: Driving online consumer engagement in Fintech</em><span class="tooltip">Purpose This study aims to explore the role of the linguistic style used in the brand-posted social media content on consumer engagement in the Fintech domain. Design/methodology/approach A total of 3,286 tweets (registering nearly 1.35 million impressions) published by 10 leading Fintech unicorns in India were extracted using the Twitter API. The Linguistic Inquiry and Word Count (LIWC) dictionary was used to analyse the linguistic characteristics of the shared tweets. Negative Binomial Regression (NBR) was used for testing the hypotheses. Findings This study finds that using drive words and cognitive language increases consumer engagement with Fintech messages via the central route of information processing. Further, affective words and conversational language drive consumer engagement through the peripheral route of information processing. Research limitations/implications The study extends the literature on brand engagement by unveiling the effect of linguistic features used to design social media messages. Practical implications The study provides guidance to social media marketers of Fintech brands regarding what content strategies best enhance consumer engagement. The linguistic style to improve online consumer engagement (OCE) is detailed. Originality/value The study’s findings contribute to the growing stream of Fintech literature by exploring the role of linguistic style on consumer engagement in social media communication. The study’s findings indicate the relevance of the dual processing mechanism of elaboration likelihood model (ELM) as an explanatory theory for evaluating consumer engagement with messages posted by Fintech brands.</span></span></td>
      <td>R.V. ShabbirHusain, Atul Arun Pathak, Shabana Chandrasekaran, and Balamurugan Annamalai</td>
      <td><a href="https://doi.org/10.1108/IJBM-11-2022-0519">link</a></td>
      <td>2023</td>
      <td>International Journal of Bank Marketing, 42(2):331–355</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Style transfer from non-parallel text by cross-alignment</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Tianxiao Shen, Tao Lei, Regina Barzilay, and Tommi Jaakkola</td>
      <td><a href="https://papers.nips.cc/paper/2017/file/2d2c8394eac7e579e59bf81f513fbd6d-Paper.pdf">link</a></td>
      <td>2017</td>
      <td>NIPS'17, pages 6833–6844</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Does string-based neural MT learn source syntax?</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Xing Shi, Inkit Padhi, and Kevin Knight</td>
      <td><a href="https://doi.org/10.18653/v1/D16-1159">link</a></td>
      <td>2016</td>
      <td>EMNLP, pages 1526–1534</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Personalized author obfuscation with large language models</em><span class="tooltip">In this paper, we investigate the efficacy of large language models (LLMs) in obfuscating authorship by paraphrasing and altering writing styles. Rather than adopting a holistic approach that evaluates performance across the entire dataset, we focus on user-wise performance to analyze how obfuscation effectiveness varies across individual authors. While LLMs are generally effective, we observe a bimodal distribution of efficacy, with performance varying significantly across users. To address this, we propose a personalized prompting method that outperforms standard prompting techniques and partially mitigates the bimodality issue.</span></span></td>
      <td>Mohammad Shokri, Sarah Ita Levitan, and Rivka Levitan</td>
      <td><a href="https://arxiv.org/abs/2505.12090">link</a></td>
      <td>2025</td>
      <td>arXiv preprint arXiv:2505.12090</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>A survey of modern authorship attribution methods</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Efstathios Stamatatos</td>
      <td><a href="https://dl.acm.org/doi/10.5555/1527090.1527102">link</a></td>
      <td>2009</td>
      <td>JASIST, 60(3):538–556</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Masking topic-related information to enhance authorship attribution</em><span class="tooltip">Authorship attribution attempts to reveal the authors of documents. In recent years, research in this field has grown rapidly. However, the performance of state‐of‐the‐art methods is heavily affected when text of known authorship and texts under investigation differ in topic and/or genre. So far, it is not clear how to quantify the personal style of authors in a way that is not affected by topic shifts or genre variations. In this paper, a set of text distortion methods are used attempting to mask topic‐related information. These methods transform the input texts into a more topic‐neutral form while maintaining the structure of documents associated with the personal style of the author. Using a controlled corpus that includes a fine‐grained range of topics and genres it is demonstrated how the proposed approach can be combined with existing authorship attribution methods to enhance their performance in very challenging tasks, especially in cross‐topic attribution. We also examine cross‐genre attribution and the most challenging, yet realistic, cross‐topic‐and‐genre attribution scenarios and show how the proposed techniques should be tuned to enhance performance in these tasks. Finally, we demonstrate that there are important differences in attribution effectiveness when either conversational genres, nonconversational genres, or a mix of them are considered.</span></span></td>
      <td>Efstathios Stamatatos</td>
      <td><a href="https://doi.org/10.1002/asi.23968">link</a></td>
      <td>2017</td>
      <td>JASIST, 69(3):461–473</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Multi-label style change detection by solving a binary classification problem</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Eivind Strøm</td>
      <td><a href="https://downloads.webis.de/pan/publications/papers/strom_2021.pdf">link</a></td>
      <td>2021</td>
      <td>CLEF 2021, pages 2146–2157</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Dialect-robust evaluation of generated text</em><span class="tooltip">Text generation metrics that are not robust to dialect variation make it impossible to tell how well systems perform for many groups of users, and can even penalize systems for producing text in lower-resource dialects. In this paper, we introduce a suite of methods to assess whether metrics are dialect robust. These methods show that state-of-the-art metrics are not dialect robust: they often prioritize dialect similarity over semantics, preferring outputs that are semantically incorrect over outputs that match the semantics of the reference but contain dialect differences. As a step towards dialect-robust metrics for text generation, we propose NANO, which introduces regional and language information to the metric’s pretraining. NANO significantly improves dialect robustness while preserving the correlation between automated metrics and human ratings. It also enables a more ambitious approach to evaluation, dialect awareness, in which system outputs are scored by both semantic match to the reference and appropriateness in any specified dialect.</span></span></td>
      <td>Jiao Sun, Thibault Sellam, Elizabeth Clark, Tu Vu, Timothy Dozat, Dan Garrette, Aditya Siddhant, Jacob Eisenstein, and Sebastian Gehrmann</td>
      <td><a href="https://doi.org/10.18653/v1/2023.acl-long.331">link</a></td>
      <td>2023</td>
      <td>ACL, pages 6010–6028</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Idiosyncrasies in large language models</em><span class="tooltip">In this work, we unveil and study idiosyncrasies in Large Language Models (LLMs) -- unique patterns in their outputs that can be used to distinguish the models. To do so, we consider a simple classification task: given a particular text output, the objective is to predict the source LLM that generates the text. We evaluate this synthetic task across various groups of LLMs and find that simply fine-tuning text embedding models on LLM-generated texts yields excellent classification accuracy. Notably, we achieve 97.1% accuracy on held-out validation data in the five-way classification problem involving ChatGPT, Claude, Grok, Gemini, and DeepSeek. Our further investigation reveals that these idiosyncrasies are rooted in word-level distributions. These patterns persist even when the texts are rewritten, translated, or summarized by an external LLM, suggesting that they are also encoded in the semantic content. Additionally, we leverage LLM as judges to generate detailed, open-ended descriptions of each model&#x27;s idiosyncrasies. Finally, we discuss the broader implications of our findings, including training on synthetic data, inferring model similarity, and robust evaluation of LLMs. Code is available at https://github.com/locuslab/llm-idiosyncrasies.</span></span></td>
      <td>Mingjie Sun, Yida Yin, Zhiqiu Xu, J. Zico Kolter, and Zhuang Liu</td>
      <td><a href="https://arxiv.org/abs/2502.12150">link</a></td>
      <td>2025</td>
      <td>arXiv:2502.12150</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Unsupervised neural text simplification</em><span class="tooltip">The paper presents a first attempt towards unsupervised neural text simplification that relies only on unlabeled text corpora. The core framework is composed of a shared encoder and a pair of attentional-decoders, crucially assisted by discrimination-based losses and denoising. The framework is trained using unlabeled text collected from en-Wikipedia dump. Our analysis (both quantitative and qualitative involving human evaluators) on public test data shows that the proposed model can perform text-simplification at both lexical and syntactic levels, competitive to existing supervised methods. It also outperforms viable unsupervised baselines. Adding a few labeled pairs helps improve the performance further.</span></span></td>
      <td>Sai Surya, Abhijit Mishra, Anirban Laha, Parag Jain, and Karthik Sankaranarayanan</td>
      <td><a href="https://aclanthology.org/P19-1198/">link</a></td>
      <td>2019</td>
      <td>ACL, pages 2058–2068</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>What do you learn from context? Probing for sentence structure in contextualized word representations</em><span class="tooltip">Contextualized representation models such as ELMo (Peters et al., 2018a) and BERT (Devlin et al., 2018) have recently achieved state-of-the-art results on a diverse array of downstream NLP tasks. Building on recent token-level probing work, we introduce a novel edge probing task design and construct a broad suite of sub-sentence tasks derived from the traditional structured NLP pipeline. We probe word-level contextual representations from four recent models and investigate how they encode sentence structure across a range of syntactic, semantic, local, and long-range phenomena. We find that existing models trained on language modeling and translation produce strong representations for syntactic phenomena, but only offer comparably small improvements on semantic tasks over a non-contextual baseline.</span></span></td>
      <td>Ian Tenney, Patrick Xia, Berlin Chen, Alex Wang, Adam Poliak, R. Thomas McCoy, Najoung Kim, Benjamin Van Durme, Samuel R. Bowman, Dipanjan Das, and Ellie Pavlick</td>
      <td><a href="https://openreview.net/forum?id=SJzSgnRcKX">link</a></td>
      <td>2018</td>
      <td>ICLR</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Writing Style Author Embedding Evaluation</em><span class="tooltip">Learning authors representations from their textual productions is now widely used to solve multiple downstream tasks, such as classification, link prediction or user recommendation. Author embedding methods are often built on top of either Doc2Vec (Mikolov et al. 2014) or the Transformer architecture (Devlin et al. 2019). Evaluating the quality of these embeddings and what they capture is a difficult task. Most articles use either classification accuracy or authorship attribution, which does not clearly measure the quality of the representation space, if it really captures what it has been built for. In this paper, we propose a novel evaluation framework of author embedding methods based on the writing style. It allows to quantify if the embedding space effectively captures a set of stylistic features, chosen to be the best proxy of an author writing style. This approach gives less importance to the topics conveyed by the documents. It turns out that recent models are mostly driven by the inner semantic of authors’ production. They are outperformed by simple baselines, based on state-of-the-art pretrained sentence embedding models, on several linguistic axes. These baselines can grasp complex linguistic phenomena and writing style more efficiently, paving the way for designing new style-driven author embedding models.</span></span></td>
      <td>Enzo Terreau, Antoine Gourru, and Julien Velcin</td>
      <td><a href="https://doi.org/10.18653/v1/2021.eval4nlp-1.9">link</a></td>
      <td>2021</td>
      <td>Evaluation and Comparison of NLP Systems Workshop, pages 84–93</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>StAyaL | Multilingual Style Transfer</em><span class="tooltip">Stylistic text generation plays a vital role in enhancing communication by reflecting the nuances of individual expression. This paper presents a novel approach for generating text in a specific speaker&#x27;s style across different languages. We show that by leveraging only 100 lines of text, an individuals unique style can be captured as a high-dimensional embedding, which can be used for both text generation and stylistic translation. This methodology breaks down the language barrier by transferring the style of a speaker between languages. The paper is structured into three main phases: augmenting the speaker&#x27;s data with stylistically consistent external sources, separating style from content using machine learning and deep learning techniques, and generating an abstract style profile by mean pooling the learned embeddings. The proposed approach is shown to be topic-agnostic, with test accuracy and F1 scores of 74.9% and 0.75, respectively. The results demonstrate the potential of the style profile for multilingual communication, paving the way for further applications in personalized content generation and cross-linguistic stylistic transfer.</span></span></td>
      <td>Karishma Thakrar, Katrina Lawrence, and Kyle Howard</td>
      <td><a href="https://arxiv.org/abs/2501.11639">link</a></td>
      <td>2025</td>
      <td>arXiv:2501.11639</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Reddust: A large reusable dataset of reddit user traits</em><span class="tooltip">Cognate words, defined as words in different languages which derive from a common etymon, can be useful for language learners, who can leverage the orthographical similarity of cognates to more easily understand a text in a foreign language. Deceptive cognates, or false friends, do not share the same meaning anymore; these can be instead deceiving and detrimental for language acquisition or text understanding in a foreign language. We use an automatic method of detecting false friends from a set of cognates, in a fully unsupervised fashion, based on cross-lingual word embeddings. We implement our method for English and five Romance languages, including a low-resource language (Romanian), and evaluate it against two different gold standards. The method can be extended easily to any language pair, requiring only large monolingual corpora for the involved languages and a small bilingual dictionary for the pair. We additionally propose a measure of “falseness” of a false friends pair. We publish freely the database of false friends in the six languages, along with the falseness scores for each cognate pair. The resource is the largest of the kind that we are aware of, both in terms of languages covered and number of word pairs.</span></span></td>
      <td>Anna Tigunova, Paramita Mirza, Andrew Yates, and Gerhard Weikum</td>
      <td><a href="https://aclanthology.org/2020.lrec-1.367/">link</a></td>
      <td>2020</td>
      <td>LREC, pages 6118–6126</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>HANSEN: Human and AI spoken text benchmark for authorship analysis</em><span class="tooltip">&lt;span class=tex-math&gt;&lt;span class=fst-italic&gt;Authorship Analysis</span></span></td>
      <td>Nafis Tripto, Adaku Uchendu, Thai Le, Mattia Setzu, Fosca Giannotti, and Dongwon Lee</td>
      <td><a href="https://doi.org/10.18653/v1/2023.findings-emnlp.916">link</a></td>
      <td>2023</td>
      <td>Findings of EMNLP 2023, pages 13706–13724</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Research Methods: The Essential Knowledge Base</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>William M. K. Trochim, James P. Donnelly, and Kanika Arora</td>
      <td><a href="https://www.cengage.com/c/research-methods-the-essential-knowledge-base-2e-trochim/">link</a></td>
      <td>2015</td>
      <td>Cengage Learning</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Persona-Augmented Benchmarking: Evaluating LLMs Across Diverse Writing Styles</em><span class="tooltip">Current benchmarks for evaluating Large Language Models (LLMs) often do not exhibit enough writing style diversity, with many adhering primarily to standardized conventions. Such benchmarks do not fully capture the rich variety of communication patterns exhibited by humans. Thus, it is possible that LLMs, which are optimized on these benchmarks, may demonstrate brittle performance when faced with &quot;non-standard&quot; input. In this work, we test this hypothesis by rewriting evaluation prompts using persona-based LLM prompting, a low-cost method to emulate diverse writing styles. Our results show that, even with identical semantic content, variations in writing style and prompt formatting significantly impact the estimated performance of the LLM under evaluation. Notably, we identify distinct writing styles that consistently trigger either low or high performance across a range of models and tasks, irrespective of model family, size, and recency. Our work offers a scalable approach to augment existing benchmarks, improving the external validity of the assessments they provide for measuring LLM performance across linguistic variations.</span></span></td>
      <td>Kimberly Le Truong, Riccardo Fogliato, Hoda Heidari, and Zhiwei Steven Wu</td>
      <td><a href="https://doi.org/10.48550/arXiv.2507.22168">link</a></td>
      <td>2025</td>
      <td>arXiv preprint ArXiv:2507.22168</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Authorship attribution for neural text generation</em><span class="tooltip">In recent years, the task of generating realistic short and long texts have made tremendous advancements. In particular, several recently proposed neural network-based language models have demonstrated their astonishing capabilities to generate texts that are challenging to distinguish from human-written texts with the naked eye. Despite many benefits and utilities of such neural methods, in some applications, being able to tell the “author” of a text in question becomes critically important. In this work, in the context of this Turing Test, we investigate the so-called authorship attribution problem in three versions: (1) given two texts T1 and T2, are both generated by the same method or not? (2) is the given text T written by a human or machine? (3) given a text T and k candidate neural methods, can we single out the method (among k alternatives) that generated T? Against one humanwritten and eight machine-generated texts (i.e., CTRL, GPT, GPT2, GROVER, XLM, XLNET, PPLM, FAIR), we empirically experiment with the performance of various models in three problems. By and large, we find that most generators still generate texts significantly different from human-written ones, thereby making three problems easier to solve. However, the qualities of texts generated by GPT2, GROVER, and FAIR are better, often confusing machine classifiers in solving three problems. All codes and datasets of our experiments are available at: &lt;a href=https://bit.ly/ class=acl-markup-url&gt;https://bit.ly/&lt;/a&gt; 302zWdz</span></span></td>
      <td>Adaku Uchendu, Thai Le, Kai Shu, and Dongwon Lee</td>
      <td><a href="https://doi.org/10.18653/v1/2020.emnlp-main.673">link</a></td>
      <td>2020</td>
      <td>EMNLP, pages 8384–8395</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Paraphrase types elicit prompt engineering capabilities</em><span class="tooltip">Much of the success of modern language models depends on finding a suitable prompt to instruct the model. Until now, it has been largely unknown how variations in the linguistic expression of prompts affect these models. This study systematically and empirically evaluates which linguistic features influence models through paraphrase types, i.e., different linguistic changes at particular positions. We measure behavioral changes for five models across 120 tasks and six families of paraphrases (i.e., morphology, syntax, lexicon, lexico-syntax, discourse, and others). We also control for other prompt engineering factors (e.g., prompt length, lexical diversity, and proximity to training data). Our results show a potential for language models to improve tasks when their prompts are adapted in specific paraphrase types (e.g., 6.7% median gain in Mixtral 8x7B; 5.5% in LLaMA 3 8B). In particular, changes in morphology and lexicon, i.e., the vocabulary used, showed promise in improving prompts. These findings contribute to developing more robust language models capable of handling variability in linguistic expression.</span></span></td>
      <td>Jan Philip Wahle, Terry Ruas, Yang Xu, and Bela Gipp</td>
      <td><a href="https://doi.org/10.18653/v1/2024.emnlp-main.617">link</a></td>
      <td>2024</td>
      <td>EMNLP, pages 11004–11033</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Can authorship representation learning capture stylistic features?</em><span class="tooltip">Abstract Automatically disentangling an author’s style from the content of their writing is a longstanding and possibly insurmountable problem in computational linguistics. At the same time, the availability of large text corpora furnished with author labels has recently enabled learning authorship representations in a purely data-driven manner for authorship attribution, a task that ostensibly depends to a greater extent on encoding writing style than encoding content. However, success on this surrogate task does not ensure that such representations capture writing style since authorship could also be correlated with other latent variables, such as topic. In an effort to better understand the nature of the information these representations convey, and specifically to validate the hypothesis that they chiefly encode writing style, we systematically probe these representations through a series of targeted experiments. The results of these experiments suggest that representations learned for the surrogate authorship prediction task are indeed sensitive to writing style. As a consequence, authorship representations may be expected to be robust to certain kinds of data shift, such as topic drift over time. Additionally, our findings may open the door to downstream applications that require stylistic representations, such as style transfer.</span></span></td>
      <td>Andrew Wang, Cristina Aggazzotti, Rebecca Kotula, Rafael Rivera Soto, Marcus Bishop, and Nicholas Andrews</td>
      <td><a href="https://doi.org/10.1162/tacl_a_00610">link</a></td>
      <td>2023</td>
      <td>TACL, 11:1416–1431</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Feature vector difference based neural network and logistic regression models for authorship verification</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Janith Weerasinghe and Rachel Greenstadt</td>
      <td><a href="https://ceur-ws.org/Vol-2696/paper_125.pdf">link</a></td>
      <td>2020</td>
      <td>PAN at CLEF 2020, 2695</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Does it capture STEL? a modular, similarity-based linguistic style evaluation framework</em><span class="tooltip">Style is an integral part of natural language. However, evaluation methods for style measures are rare, often task-specific and usually do not control for content. We propose the modular, fine-grained and content-controlled similarity-based STyle EvaLuation framework (STEL) to test the performance of any model that can compare two sentences on style. We illustrate STEL with two general dimensions of style (formal/informal and simple/complex) as well as two specific characteristics of style (contrac’tion and numb3r substitution). We find that BERT-based methods outperform simple versions of commonly used style measures like 3-grams, punctuation frequency and LIWC-based approaches. We invite the addition of further tasks and task instances to STEL and hope to facilitate the improvement of style-sensitive measures.</span></span></td>
      <td>Anna Wegmann and Dong Nguyen</td>
      <td><a href="https://doi.org/10.18653/v1/2021.emnlp-main.569">link</a></td>
      <td>2021</td>
      <td>EMNLP, pages 7109–7130</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Tokenization is sensitive to language variation</em><span class="tooltip">Variation in language is ubiquitous and often systematically linked to regional, social, and contextual factors. Tokenizers split texts into smaller units and might behave differently for less common linguistic forms. This might affect downstream LLM performance differently on two types of tasks: Tasks where the model should be robust to language variation (e.g., for semantic tasks like NLI, labels do not depend on whether a text uses British or American spelling) and tasks where the model should be sensitive to language variation (e.g., for form-based tasks like authorship verification, labels depend on whether a text uses British or American spelling). We pre-train BERT base models with the popular Byte-Pair Encoding algorithm to investigate how key tokenization design choices impact the performance of downstream models: the corpus used to train the tokenizer, the pre-tokenizer and the vocabulary size. We find that the best tokenizer varies on the two task types and that the pre-tokenizer has the biggest overall impact on performance. Further, we introduce a new approach to estimate tokenizer impact on downstream LLM performance, showing substantial improvement over metrics like Rényi efficiency. We encourage more work on language variation and its relation to tokenizers and thus LLM performance.</span></span></td>
      <td>Anna Wegmann, Dong Nguyen, and David Jurgens</td>
      <td><a href="https://doi.org/10.18653/v1/2025.findings-acl.572">link</a></td>
      <td>2025</td>
      <td>Findings of ACL 2025, pages 10958–10983</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Same Author or Just Same Topic? Towards Content-Independent Style Representations</em><span class="tooltip">Linguistic style is an integral component of language. Recent advances in the development of style representations have increasingly used training objectives from authorship verification (AV)”:” Do two texts have the same author? The assumption underlying the AV training task (same author approximates same writing style) enables self-supervised and, thus, extensive training. However, a good performance on the AV task does not ensure good “general-purpose” style representations. For example, as the same author might typically write about certain topics, representations trained on AV might also encode content information instead of style alone. We introduce a variation of the AV training task that controls for content using conversation or domain labels. We evaluate whether known style dimensions are represented and preferred over content information through an original variation to the recently proposed STEL framework. We find that representations trained by controlling for conversation are better than representations trained with domain or no content control at representing style independent from content.</span></span></td>
      <td>Anna Wegmann, Marijn Schraagen, and Dong Nguyen</td>
      <td><a href="https://doi.org/10.18653/v1/2022.repl4nlp-1.26">link</a></td>
      <td>2022</td>
      <td>RepL4NLP Workshop, pages 249–268</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Constraints on the agentless passive</em><span class="tooltip">This paper is a quantitative study of the factors that determine the selection of passive constructions over active ones by English speakers. By examining a large body of passives used in spontaneous speech, together with the sentences that show an opposing choice, we are able to throw light on the crucial question of which syntactic and which semantic features of the environment act to constrain the choice and whether syntactic or semantic factors predominate in this case. In the course of the analysis, we will also have something to say about the social factors that have been reported to determine the use of the passive.</span></span></td>
      <td>E. Judith Weiner and William Labov</td>
      <td><a href="https://doi.org/10.1017/S0022226700007441">link</a></td>
      <td>1983</td>
      <td>Journal of Linguistics, 19(1):29–58</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Disentangling style factors from speaker representations</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Jennifer Williams and Simon King</td>
      <td><a href="https://doi.org/10.21437/Interspeech.2019-2605">link</a></td>
      <td>2019</td>
      <td>Interspeech, pages 3945–3949</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Style over substance: Evaluation biases for large language models</em><span class="tooltip">As large language models (LLMs) continue to advance, accurately and comprehensively evaluating their performance becomes increasingly challenging. Ranking the relative performance of LLMs based on Elo ratings, according to human or LLM judgment, is gaining more popularity. However, the extent to which humans and LLMs are capable evaluators remains uncertain. This study investigates the behavior of crowd-sourced and expert annotators, as well as LLMs, when comparing outputs from different models. To achieve this, we curate a dataset of intentionally flawed, machine-generated answers. Our findings reveal a concerning bias in the evaluation process, as answers with factual errors are rated more favorably than answers that are too short or contained grammatical errors. To address this issue, we propose independently evaluating machine-generated text across multiple dimensions, rather than merging all the evaluation aspects into a single score. We instantiate this idea with the Elo rating system, resulting in the Multi-Elo Rating System (MERS). Empirical results from our study reveal that this proposed approach significantly enhances the quality of LLM-based evaluations, particularly in terms of factual accuracy. However, there is no significant improvement in crowd-sourced evaluations, indicating the need for further investigation.</span></span></td>
      <td>Minghao Wu and Alham Fikri Aji</td>
      <td><a href="https://aclanthology.org/2025.coling-main.21/">link</a></td>
      <td>2025</td>
      <td>COLING, pages 297–312</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Out-of-distribution generalization in natural language processing: Past, present, and future</em><span class="tooltip">Machine learning (ML) systems in natural language processing (NLP) face significant challenges in generalizing to out-of-distribution (OOD) data, where the test distribution differs from the training data distribution. This poses important questions about the robustness of NLP models and their high accuracy, which may be artificially inflated due to their underlying sensitivity to systematic biases. Despite these challenges, there is a lack of comprehensive surveys on the generalization challenge from an OOD perspective in natural language understanding. Therefore, this paper aims to fill this gap by presenting the first comprehensive review of recent progress, methods, and evaluations on this topic. We further discuss the challenges involved and potential future research directions. By providing convenient access to existing work, we hope this survey will encourage future research in this area.</span></span></td>
      <td>Linyi Yang, Yaoxian Song, Xuan Ren, Chenyang Lyu, Yidong Wang, Jingming Zhuo, Lingqiao Liu, Jindong Wang, Jennifer Foster, and Yue Zhang</td>
      <td><a href="https://doi.org/10.18653/v1/2023.emnlp-main.276">link</a></td>
      <td>2023</td>
      <td>EMNLP, pages 4533–4559</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>A Survey of Controllable Text Generation Using Transformer-based Pre-trained Language Models</em><span class="tooltip">Controllable Text Generation (CTG) is an emerging area in the field of natural language generation (NLG). It is regarded as crucial for the development of advanced text generation technologies that better meet the specific constraints in practical applications. In recent years, methods using large-scale pre-trained language models (PLMs), in particular the widely used Transformer-based PLMs, have become a new paradigm of NLG, allowing generation of more diverse and fluent text. However, due to the limited level of interpretability of deep neural networks, the controllability of these methods needs to be guaranteed. To this end, controllable text generation using Transformer-based PLMs has become a rapidly growing yet challenging new research hotspot. A diverse range of approaches have emerged in the past 3 to 4 years, targeting different CTG tasks that require different types of controlled constraints. In this article, we present a systematic critical review on the common tasks, main approaches, and evaluation methods in this area. Finally, we discuss the challenges that the field is facing, and put forward various promising future directions. To the best of our knowledge, this is the first survey article to summarize the state-of-the-art CTG techniques from the perspective of Transformer-based PLMs. We hope it can help researchers and practitioners in the related fields to quickly track the academic and technological frontier, providing them with a landscape of the area and a roadmap for future research.</span></span></td>
      <td>Hanqing Zhang, Haolin Song, Shaoyu Li, Ming Zhou, and Dawei Song</td>
      <td><a href="https://doi.org/10.1145/3617680">link</a></td>
      <td>2023</td>
      <td>ACM Computing Surveys, 56(3):64:1–64:37</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Personalized Text Generation with Contrastive Activation Steering</em><span class="tooltip">Personalized text generation aims to infer users’ writing style preferences from their historical texts and generate outputs that faithfully reflect these stylistic characteristics. Existing solutions primarily adopt two paradigms: retrieval-augmented generation (RAG) and parameter-efficient fine-tuning (PEFT). While these approaches have advanced the field, they suffer from two critical limitations: (1) the entanglement of content semantics and stylistic patterns in historical texts impedes accurate modeling of user-specific writing preferences; and (2) scalability challenges arising from both RAG’s inference latency by retrieval operations and PEFT’s parameter storage requirements for per user model. To overcome these limitations, we propose StyleVector, a training-free framework that disentangles and represents personalized writing style as a vector in LLM’s activation space, enabling style-steered generation during inference without requiring costly retrieval or parameter storage. Comprehensive experiments demonstrate that our framework achieves a significant 8% relative improvement in personalized generation while reducing storage requirements by 1700 &lt;span class=tex-math&gt;×</span></span></td>
      <td>Jinghao Zhang, Yuting Liu, Wenjie Wang, Qiang Liu, Shu Wu, Liang Wang, and Tat-Seng Chua</td>
      <td><a href="https://doi.org/10.18653/v1/2025.acl-long.353">link</a></td>
      <td>2025</td>
      <td>ACL, pages 7128–7141</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>How Well Do Text Embedding Models Understand Syntax?</em><span class="tooltip">Text embedding models have significantly contributed to advancements in natural language processing by adeptly capturing semantic properties of textual data. However, the ability of these models to generalize across a wide range of syntactic contexts remains under-explored. In this paper, we first develop an evaluation set, named SR, to scrutinize the capability for syntax understanding of text embedding models from two crucial syntactic aspects: Structural heuristics, and Relational understanding among concepts, as revealed by the performance gaps in previous studies. Our findings reveal that existing text embedding models have not sufficiently addressed these syntactic understanding challenges, and such ineffectiveness becomes even more apparent when evaluated against existing benchmark datasets. Furthermore, we conduct rigorous analysis to unearth factors that lead to such limitations and examine why previous evaluations fail to detect such ineffectiveness. Lastly, we propose strategies to augment the generalization ability of text embedding models in diverse syntactic scenarios. This study serves to highlight the hurdles associated with syntactic generalization and provides pragmatic guidance for boosting model performance across varied syntactic contexts.</span></span></td>
      <td>Yan Zhang, Zhaopeng Feng, Zhiyang Teng, Zuozhu Liu, and Haizhou Li</td>
      <td><a href="https://doi.org/10.18653/v1/2023.findings-emnlp.650">link</a></td>
      <td>2023</td>
      <td>Findings of EMNLP 2023, pages 9717–9728</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Personalization of Large Language Models: A Survey</em><span class="tooltip">Personalization of Large Language Models (LLMs) has recently become increasingly important with a wide range of applications. Despite the importance and recent progress, most existing works on personalized LLMs have focused either entirely on (a) personalized text generation or (b) leveraging LLMs for personalization-related downstream applications, such as recommendation systems. In this work, we bridge the gap between these two separate main directions for the first time by introducing a taxonomy for personalized LLM usage and summarizing the key differences and challenges. We provide a formalization of the foundations of personalized LLMs that consolidates and expands notions of personalization of LLMs, defining and discussing novel facets of personalization, usage, and desiderata of personalized LLMs. We then unify the literature across these diverse fields and usage scenarios by proposing systematic taxonomies for the granularity of personalization, personalization techniques, datasets, evaluation methods, and applications of personalized LLMs. Finally, we highlight challenges and important open problems that remain to be addressed. By unifying and surveying recent research using the proposed taxonomies, we aim to provide a clear guide to the existing literature and different facets of personalization in LLMs, empowering both researchers and practitioners.</span></span></td>
      <td>Zhehao Zhang, Ryan A. Rossi, Branislav Kveton, Yijia Shao, Diyi Yang, Hamed Zamani, Franck Dernoncourt, Joe Barrow, Tong Yu, Sungchul Kim, Ruiyi Zhang, Jiuxiang Gu, Tyler Derr, Hongjie Chen, Junda Wu, Xiang Chen, Zichao Wang, Subrata Mitra, Nedim Lipka, Nesreen K. Ahmed, and Yu Wang</td>
      <td><a href="https://openreview.net/forum?id=tf6A9EYMo6">link</a></td>
      <td>2025</td>
      <td>Transactions on Machine Learning Research</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Unmasking style sensitivity: A causal analysis of bias evaluation instability in large language models</em><span class="tooltip">Natural language processing applications are increasingly prevalent, but social biases in their outputs remain a critical challenge. While various bias evaluation methods have been proposed, these assessments show unexpected instability when input texts undergo minor stylistic changes. This paper conducts a comprehensive analysis of how different style transformations impact bias evaluation results across multiple language models and bias types using causal inference techniques. Our findings reveal that formality transformations significantly affect bias scores, with informal style showing substantial bias reductions (up to 8.33% in LLaMA-2-13B). We identify appearance bias, sexual orientation bias, and religious bias as most susceptible to style changes, with variations exceeding 20%. Larger models demonstrate greater sensitivity to stylistic variations, with bias measurements fluctuating up to 3.1% more than in smaller models. These results highlight critical limitations in current bias evaluation methods and emphasize the need for reliable and fair assessments of language models.</span></span></td>
      <td>Jiaxu Zhao, Meng Fang, Kun Zhang, and Mykola Pechenizkiy</td>
      <td><a href="https://doi.org/10.18653/v1/2025.acl-long.796">link</a></td>
      <td>2025</td>
      <td>ACL, pages 16314–16338</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Disentangled sequence to sequence learning for compositional generalization</em><span class="tooltip">There is mounting evidence that existing neural network models, in particular the very popular sequence-to-sequence architecture, struggle to systematically generalize to unseen compositions of seen components. We demonstrate that one of the reasons hindering compositional generalization relates to representations being entangled. We propose an extension to sequence-to-sequence models which encourage disentanglement by adaptively re-encoding (at each time step) the source input. Specifically, we condition the source representations on the newly decoded target context which makes it easier for the encoder to exploit specialized information for each prediction rather than capturing it all in a single forward pass. Experimental results on semantic parsing and machine translation empirically show that our proposal delivers more disentangled representations and better generalization.</span></span></td>
      <td>Hao Zheng and Mirella Lapata</td>
      <td><a href="https://doi.org/10.18653/v1/2022.acl-long.293">link</a></td>
      <td>2022</td>
      <td>ACL, pages 4256–4268</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Idiosyncratic but not Arbitrary: Learning Idiolects in Online Registers Reveals Distinctive yet Consistent Individual Styles</em><span class="tooltip">An individual’s variation in writing style is often a function of both social and personal attributes. While structured social variation has been extensively studied, e.g., gender based variation, far less is known about how to characterize individual styles due to their idiosyncratic nature. We introduce a new approach to studying idiolects through a massive cross-author comparison to identify and encode stylistic features. The neural model achieves strong performance at authorship identification on short texts and through an analogy-based probing task, showing that the learned representations exhibit surprising regularities that encode qualitative and quantitative shifts of idiolectal styles. Through text perturbation, we quantify the relative contributions of different linguistic elements to idiolectal variation. Furthermore, we provide a description of idiolects through measuring inter- and intra-author variation, showing that variation in idiolects is often distinctive yet consistent.</span></span></td>
      <td>Jian Zhu and David Jurgens</td>
      <td><a href="https://doi.org/10.18653/v1/2021.emnlp-main.25">link</a></td>
      <td>2021</td>
      <td>EMNLP, pages 279–297</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>StyleFlow: Disentangle latent representations via normalizing flow for unsupervised text style transfer</em><span class="tooltip">Unsupervised text style transfer aims to modify the style of a sentence while preserving its content without parallel corpora. Existing approaches attempt to separate content from style, but some words contain both content and style information. It makes them difficult to disentangle, where unsatisfactory disentanglement results in the loss of the content information or the target style. To address this issue, researchers adopted a “cycle reconstruction” mechanism to maintain content information, but it is still hard to achieve satisfactory content preservation due to incomplete disentanglement. In this paper, we propose a new disentanglement-based method, StyleFlow, which effectively avoids the loss of contents through a better cycle reconstruction via a reversible encoder. The reversible encoder is a normalizing flow that can not only produce output given input but also infer the exact input given the output reversely. We design a stack of attention-aware coupling layers, where each layer is reversible and adopts the attention mechanism to improve the content-style disentanglement. Moreover, we propose a data augmentation method based on normalizing flow to enhance the training data. Our experiments on sentiment transfer and formality transfer tasks show that StyleFlow outperforms strong baselines on both content preservation and style transfer.</span></span></td>
      <td>Kangchen Zhu, Zhiliang Tian, Jingyu Wei, Ruifeng Luo, Yiping Song, and Xiaoguang Mao</td>
      <td><a href="https://aclanthology.org/2024.lrec-main.1336/">link</a></td>
      <td>2024</td>
      <td>LREC-COLING 2024, pages 15384–15397</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Trans self-identification and the language of neoliberal selfhood: Agency, power, and the limits of monologic discourse</em><span class="tooltip">Abstract Sociocultural linguists share with transgender communities a strong interest in the power of individuals to assert agency over linguistic patterns. For trans people, a key principle of activism is gender self-determination , which treats each individual as the ultimate authority on their own gender identity. This article explores some of the ways gender self-determination and self-identification surface in transgender people’s linguistic practices. Three particular manifestations are highlighted: gendered identity labels, third person pronouns, and body part terminology. The observations offered on these subjects are based on a series of ethnographic projects carried out from 2006–2016 in transgender communities across several metropolitan areas in the United States and in online spaces frequented by trans people. However, the analysis goes beyond mere description by treating this kind of individualized linguistic agency as the product of cultural practice rather than an asocial given. Such a perspective introduces questions concerning why this form of agency arose in the time and place that it has. This article frames gender self-identification as an enactment of neoliberal personhood, in which individuals are framed as the driver of their destiny. What the ideology of neoliberal agency obscures, however, is that agency is not an equally distributed resource.</span></span></td>
      <td>Lal Zimman</td>
      <td><a href="https://doi.org/doi:10.1515/ijsl-2018-2016">link</a></td>
      <td>2019</td>
      <td>IJSL, 2019(256):147–175</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>An ensemble-rich multi-aspect approach for robust style change detection</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Dimitrina Zlatkova, Daniel Kopev, Kristiyan Mitov, Atanas Atanasov, Momchil Hardalov, Ivan Koychev, and Preslav Nakov</td>
      <td><a href="https://downloads.webis.de/publications/papers/zlatkova_2018.pdf">link</a></td>
      <td>2018</td>
      <td>PAN at CLEF-2018</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Style change detection with feed-forward neural networks</em><span class="tooltip">PLACEHOLDER</span></span></td>
      <td>Chaoyuan Zuo, Yu Zhao, and Ritwik Banerjee</td>
      <td><a href="https://ceur-ws.org/Vol-2380/paper_229.pdf">link</a></td>
      <td>2019</td>
      <td>PAN at CLEF 2019, 93</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>A Multi-Dimensional Analysis of English Tweets by Chinese and American Automotive Companies</em><span class="tooltip">Abstract: </span>While multi-dimensional (MD) analysis is a widely used method for register analysis, it receives limited attention in studies of corporate tweets, especially from a cross-cultural perspective. This study conducts a full MD analysis on an English-language corpus of tweets from three automotive manufacturers per country in China and the United States. It aims to interpret the communicative functions behind the statistical co-occurrence patterns of linguistic features in these automotive corporate tweets, and to examine cross-cultural similarities and differences in these patterns. The results reveal two interpretable sets of co-occurring features, labelled as: (1) corporate self-promotional narrative versus addressee-focused interaction and (2) affective versus volitional interaction. Although both dimensions are found in Chinese and American subcorpora, Chinese automotive companies slightly favor self-promotional narrative and affective interaction, whereas American automotive companies comparatively display addressee-focused and volitional interaction. The observed differences may relate to the variations in national culture and economic conditions. This study offers sector-specific insights into the co-occurrence patterns of linguistic features in corporate social media communication and contributes to research in applied linguistics and corporate media discourse.</span></td>
      <td>Yilin Xu, Eric Friginal, and Chunyu Hu</td>
      <td><a href="https://doi.org/10.1111/ijal.70132">link</a></td>
      <td>2026</td>
      <td>International Journal of Applied Linguistics</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Forming and authorship profile through n-gram tracing</em><span class="tooltip">Abstract: </span>In forensic linguistics, authorship profiles have become an important tool for identifying and characterizing individuals based on their writing style and authorship attribution. This study employed N-gram tracing, a corpus linguistics mixed computational method that investigates recurring patterns of sequences of words or characters in text. By analyzing WhatsApp (WA) messages extracted from case evidence, this study examines how N-gram patterns can reveal specific linguistic features associated with author identity. The dataset consists of personal texts and microblogs containing approximately 2.1 tokens. To ensure data integrity, the text was cleaned of non-traditional elements such as hyperlinks and media files during a preprocessing phase. N-grams on both character and word level, including N1-N5, were extracted and examined for diversity, frequency, distribution, and contextual usage patterns. To discern stylistic consistency across texts attributed to a particular individual, a machine learning model was used to calculate the similarity index and evaluate these linguistic fingerprints. Initial results suggest that certain N-gram patterns, such as orthographic selection and lexical choice, are highly indicative of individual influence. Profiling is also enhanced with linguistic markers such as abbreviations, code-switching, and unique styles present in informal communication. This study demonstrates that N-gram tracing is not only effective in identifying authorship but can also provide information on demographic and psychological features such as age, gender, and communication preferences. The fields of forensic linguistics and computational authorship analysis benefit from this study as it provides a robust and scalable technique for profiling authors based on real-world data. Furthermore, it highlights the ramifications in the legal context, emphasizing the potential for N-gram search to aid investigations where digital communication is critical. Extending the analysis to multilingual data and integrating semantic-level profiling to improve accuracy are future steps.</span></td>
      <td>Devi Ambarwati Puspitasari</td>
      <td><a href="https://doi.org/10.51817/kimli.v2025i.145">link</a></td>
      <td>2026</td>
      <td>Kongres Internasional Masyarakat Linguistik Indonesia, 2025</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Grammar as a behavioral biometric: using cognitively motivated grammar models for authorship verification</em><span class="tooltip">Abstract: </span>Authorship Verification (AV) is a key area of research in digital text forensics, which addresses the fundamental question of whether two texts were written by the same person. Numerous computational approaches have been proposed over the last two decades in an attempt to address this challenge. However, existing AV methods often suffer from high complexity, low explainability, and especially from a lack of clear scientific justification. We propose a simpler method based on modeling the grammar of an author following Cognitive Linguistics principles. These models are used to calculate λG (LambdaG): the ratio of the likelihoods of a document given the candidate’s grammar versus given a reference population’s grammar. Our empirical evaluation, conducted on 12 datasets and compared against seven baseline methods, demonstrates that LambdaG achieves superior performance, including against several neural network-based AV methods. LambdaG is also robust to small variations in the composition of the reference population and provides interpretable visualizations, enhancing its explainability. We argue that its effectiveness is due to the method’s compatibility with Cognitive Linguistics theories, predicting that a person’s grammar is a behavioral biometric.</span></td>
      <td>Andrea Nini, Oren Halvani, Lukas Graner, Sophie Titze, Valerio Gherardi, and Shunichi Ishihara 
</td>
      <td><a href=" https://doi.org/10.1057/s41599-025-06340-3">link</a></td>
      <td>2026</td>
      <td>Humanities and Social Sciences Communications 13(455)</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Multi-Task Classification of Hebrew News Articles: A Comparative Study of Classical ML and BERT Models in a Morphologically Rich, Low-Resource Setting</em><span class="tooltip">Abstract: </span>The automated classification of Hebrew, a morphologically rich language (MRL), presents unique challenges, particularly when high-quality labeled data are scarce. This study investigates the interplay between handcrafted feature engineering and transformer-based representations in a low-resource news classification setting (n = 306). We evaluate a multi-task classification across four distinct dimensions: domain, sentiment, gender, and source. Our methodology employs an extensive feature space of 2149 stylistic and content-based attributes, optimized through a systematic Hill-Climbing selection process. We contrast five classical machine learning architectures with five BERT-based models, integrating five oversampling strategies to mitigate class imbalance. The results reveal that in scenarios of extreme data scarcity, the performance gap between deep learning and optimized classical ML becomes marginal, with stylistic features providing critical stability and interpretability. This study contributes a curated Hebrew news dataset and establishes a robust benchmark, demonstrating that linguistically aware feature engineering remains a vital component for MRL processing when large-scale fine-tuning is impractical.</span></td>
      <td>Yaakov HaCohen-Kerner, Eyal Seckbach, and Dan Bouhnik</td>
      <td><a href="https://doi.org/10.3390/app16083907">link</a></td>
      <td>2026</td>
      <td>Appl. Sci. 16(8): 3907</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>A stylometric approach for author attribution system using neural network and machine learning classifiers</em><span class="tooltip">Abstract: </span>The paper discusses few methods of author attribution system in Bengali literature through stylometric approach. Our goal is to examine whether it is possible to identify the actual writers of some unknown Bangla documents by using a machine learning algorithm and artificial neural network. Two voting systems are also generated by the algorithms and how it varies from the result of classification models is discussed here too. We have made a corpus collecting articles of eight political writers. Firstly, we have selected some effective style markers based on statistical analysis of extracted features. Then multilayer feedforward neural network and SVM classification model are used to build an attribution system. Later, two voting systems are created by MLP classifier and SVM classification. By doing experiment and comparison, voting system gives much better result and works in more effective way for our research than the classification models.</span></td>
      <td>Anika Samiha Hossain, Nazia Akter, and MD. Saiful Islam</td>
      <td><a href="https://doi.org/10.1145/3377049.3377079">link</a></td>
      <td>2020</td>
      <td>ICCA '20: Proceedings of the International Conference on Computing Advancements 22: 1 - 7</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Robust stylometric analysis and author attribution based on tones and rimes</em><span class="tooltip">Abstract: </span>In this article, we propose an innovative and robust approach to stylometric analysis without annotation and leveraging lexical and sub-lexical information. In particular, we propose to leverage the phonological information of tones and rimes in Mandarin Chinese automatically extracted from unannotated texts. The texts from different authors were represented by tones, tone motifs, and word length motifs as well as rimes and rime motifs. Support vector machines and random forests were used to establish the text classification model for authorship attribution. From the results of the experiments, we conclude that the combination of bigrams of rimes, word-final rimes, and segment-final rimes can discriminate the texts from different authors effectively when using random forests to establish the classification model. This robust approach can in principle be applied to other languages with established phonological inventory of onset and rimes.</span></td>
      <td>Renkui Hou and Chu-Ren Huang</td>
      <td><a href="https://doi.org/10.1017/S135132491900010X">link</a></td>
      <td>2019</td>
      <td>Natural Language Engineering 26(1): 49-71</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Authorship Attribution for a Resource Poor Language—Urdu</em><span class="tooltip">Abstract: </span> Authorship attribution refers to examining the writing style of authors to determine the likelihood of the original author of a document from a given set of potential authors. Due to the wide range of authorship attribution applications, a plethora of studies have been conducted for various Western, as well as Asian, languages. However, authorship attribution research in the Urdu language has just begun, although Urdu is widely acknowledged as a prominent South Asian language. Furthermore, the existing studies on authorship attribution in Urdu have addressed a considerably easier problem of having less than 20 candidate authors, which is far from the real-world settings. Therefore, the findings from these studies may not be applicable to the real-world settings. To that end, we have made three key contributions: First, we have developed a large authorship attribution corpus for Urdu, which is a low-resource language. The corpus is composed of over 2.6 million tokens and 21,938 news articles by 94 authors, which makes it a closer substitute to the real-world settings. Second, we have analyzed hundreds of stylometry features used in the literature to identify 194 features that are applicable to the Urdu language and developed a taxonomy of these features. Finally, we have performed 66 experiments using two heterogeneous datasets to evaluate the effectiveness of four traditional and three deep learning techniques. The experimental results show the following: (a) Our developed corpus is many folds larger than the existing corpora, and it is more challenging than its counterparts for the authorship attribution task, and (b) Convolutional Neutral Networks is the most effective technique, as it achieved a nearly perfect F1 score of 0.989 for an existing corpus and 0.910 for our newly developed corpus.</span></td>
      <td>Zulqarnain Nazir, Khurram Shahzad, Muhammad Kamran Malik, Waheed Anwar, Imran Sarwar Bajwa, and Khawar Mehmood</td>
      <td><a href="https://doi.org/10.1145/348706">link</a></td>
      <td>2021</td>
      <td>Transactions on Asian and Low-Resource Language Information Processing, Volume 21, Issue 3, No. 44: 1-23</td>
    </tr>
    <tr>
      <td><span class="has-tooltip"><em>Authorship Attribution of The Golden Lotus Based on Text Classification Methods</em><span class="tooltip">Abstract: </span>In this paper, we explore the authorship attribution of The Golden Lotus using the traditional machine learning method of text classification. There are four candidate authors: Shizhen Wang, Wei Xu, Kaixian Li and Zhideng Wang. We choose The Golden Lotus's poems and four candidate authors' poems as data set. According to the characteristics of Chinese ancient poem, we choose Chinese character, rhyme, genre and overlapped word as features. We use six supervised machine learning algorithms, including Logistic Regression, Random Forests, Decision Tree and Naive Bayes, SVM and KNN classifiers respectively for text binary classification and multi-classification. According to two experiments results, the style of writing of Wei Xu's poems is the most similar to that of The Golden Lotus. It is proved that among four authors, Wei Xu most likely be the author of The Golden Lotus.</span></td>
      <td>Xuemei Tang, Shichen Liang, and Zhiying Liu</td>
      <td><a href="https://doi.org/10.1145/3319921.3319958">link</a></td>
      <td>2019</td>
      <td>ICIAI '19: Proceedings of the 2019 3rd International Conference on Innovation in Artificial Intelligence: 69-72</td>
    </tr>
  </tbody>
</table>


<link rel="stylesheet" href="../assets/tablesort.css">

<script src="https://unpkg.com/tablesort@5.6.0/dist/tablesort.min.js"></script>
<script src="../assets/sort-tables.js"></script>
