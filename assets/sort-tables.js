// Shared client-side helpers for tables on the GitHub Pages site.
// - Sorting: uses [Tablesort](https://github.com/tristen/tablesort)
// - Optional filtering: any <input data-table-filter="#table-id"> will
//   filter rows in the referenced table by text match.

(function () {
  function initTableSort() {
    if (typeof Tablesort !== "function") {
      // Tablesort library not loaded; skip silently.
      return;
    }

    const tables = document.querySelectorAll("table");
    tables.forEach((table) => {
      new Tablesort(table);

      // Initial sort: first column ascending so users see it's sortable.
      const firstHeader = table.querySelector("thead th");
      if (firstHeader) {
        firstHeader.click();
      }
    });
  }

  function initTableFilters() {
    const filters = document.querySelectorAll("[data-table-filter]");
    filters.forEach((input) => {
      const selector = input.getAttribute("data-table-filter");

      function findTable() {
        if (selector) {
          const t = document.querySelector(selector);
          if (t) return t;
        }
        // Fallback: nearest table after the input
        let el = input.nextElementSibling;
        while (el) {
          if (el.tagName && el.tagName.toLowerCase() === "table") return el;
          el = el.nextElementSibling;
        }
        return null;
      }

      const table = findTable();
      if (!table) return;

      const tbody = table.tBodies[0] || table;

      input.addEventListener("input", function () {
        const query = this.value.trim().toLowerCase();
        // Split the query on whitespace; each token must be present in the row
        // (AND match). So e.g. "universal soto" matches a row whose text
        // contains both "universal" and "soto" in any order or position.
        const tokens = query ? query.split(/\s+/).filter(Boolean) : [];
        const rows = Array.from(tbody.querySelectorAll("tr"));

        rows.forEach((row) => {
          const text = row.textContent.toLowerCase();
          const match = tokens.length === 0 || tokens.every((t) => text.indexOf(t) !== -1);
          row.style.display = match ? "" : "none";
        });
      });
    });
  }

  function init() {
    initTableSort();
    initTableFilters();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
