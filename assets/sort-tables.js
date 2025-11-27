// Wire up [Tablesort](https://github.com/tristen/tablesort) on all tables.
// Requires tablesort.min.js to be loaded before this script.

(function () {
  function initTableSort() {
    if (typeof Tablesort !== "function") {
      // Tablesort library not loaded; do nothing gracefully.
      return;
    }

    const tables = document.querySelectorAll("table");
    tables.forEach((table) => {
      // Initialize Tablesort for this table
      new Tablesort(table);

      // Initial sort: first column ascending so users see it's sortable
      const firstHeader = table.querySelector("thead th");
      if (firstHeader) {
        firstHeader.click();
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initTableSort);
  } else {
    initTableSort();
  }
})();
