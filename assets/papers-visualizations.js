(function () {
  function buildVenueChart() {
    const table = document.querySelector("#papers-table");
    const canvas = document.getElementById("venue-chart");
    if (!table || !canvas || typeof Chart === "undefined") return;

    const tbody = table.tBodies[0] || table;
    const rows = Array.from(tbody.querySelectorAll("tr"));

    const counts = {};
    rows.forEach((row) => {
      const cells = row.cells;
      if (!cells || cells.length < 5) return;
      const venue = cells[4].textContent.trim();
      if (!venue) return;
      counts[venue] = (counts[venue] || 0) + 1;
    });

    const labels = Object.keys(counts);
    const data = labels.map((k) => counts[k]);

    if (!labels.length) return;

    const ctx = canvas.getContext("2d");
    // eslint-disable-next-line no-undef
    new Chart(ctx, {
      type: "bar",
      data: {
        labels,
        datasets: [
          {
            label: "Number of papers",
            data,
            backgroundColor: "rgba(54, 162, 235, 0.5)",
            borderColor: "rgba(54, 162, 235, 1)",
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: {
            ticks: { autoSkip: false, maxRotation: 60, minRotation: 30 },
          },
          y: {
            beginAtZero: true,
            precision: 0,
          },
        },
        plugins: {
          legend: {
            display: false,
          },
        },
      },
    });
  }

  function buildCitationNetwork() {
    const container = document.getElementById("citation-network");
    const dataEl = document.getElementById("citation-data");
    if (!container || !dataEl || typeof d3 === "undefined") return;

    let payload;
    try {
      const text = dataEl.textContent.trim();
      if (!text) return;
      payload = JSON.parse(text);
    } catch (e) {
      console.error("Failed to parse citation-data JSON", e);
      return;
    }

    const nodes = payload.nodes || [];
    const links = payload.links || [];
    if (!nodes.length || !links.length) return;

    const width = container.clientWidth || 800;
    const height = container.clientHeight || 500;

    const svg = d3
      .select(container)
      .append("svg")
      .attr("width", width)
      .attr("height", height);

    const link = svg
      .append("g")
      .attr("stroke", "#aaa")
      .attr("stroke-width", 1)
      .selectAll("line")
      .data(links)
      .enter()
      .append("line");

    const node = svg
      .append("g")
      .attr("stroke", "#fff")
      .attr("stroke-width", 1.5)
      .selectAll("circle")
      .data(nodes)
      .enter()
      .append("circle")
      .attr("r", 5)
      .attr("fill", "#1f77b4")
      .call(
        d3
          .drag()
          .on("start", dragstarted)
          .on("drag", dragged)
          .on("end", dragended)
      );

    const labels = svg
      .append("g")
      .selectAll("text")
      .data(nodes)
      .enter()
      .append("text")
      .attr("font-size", 10)
      .attr("dx", 8)
      .attr("dy", "0.31em")
      .text((d) => d.label || d.id);

    const simulation = d3
      .forceSimulation(nodes)
      .force(
        "link",
        d3
          .forceLink(links)
          .id((d) => d.id)
          .distance(80)
      )
      .force("charge", d3.forceManyBody().strength(-150))
      .force("center", d3.forceCenter(width / 2, height / 2));

    simulation.on("tick", () => {
      link
        .attr("x1", (d) => d.source.x)
        .attr("y1", (d) => d.source.y)
        .attr("x2", (d) => d.target.x)
        .attr("y2", (d) => d.target.y);

      node.attr("cx", (d) => d.x).attr("cy", (d) => d.y);

      labels.attr("x", (d) => d.x).attr("y", (d) => d.y);
    });

    function dragstarted(event, d) {
      if (!event.active) simulation.alphaTarget(0.3).restart();
      d.fx = d.x;
      d.fy = d.y;
    }

    function dragged(event, d) {
      d.fx = event.x;
      d.fy = event.y;
    }

    function dragended(event, d) {
      if (!event.active) simulation.alphaTarget(0);
      d.fx = null;
      d.fy = null;
    }
  }

  function init() {
    buildVenueChart();
    buildCitationNetwork();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();


