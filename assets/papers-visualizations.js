(function () {
  function buildVenueChart() {
    // Prefer the explicit papers table if present, otherwise fall back to
    // the first table on the page.
    const table =
      document.querySelector("#papers-table") ||
      document.querySelector("table");
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

  function init() {
    buildVenueChart();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();



