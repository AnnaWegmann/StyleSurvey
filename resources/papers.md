## Papers and works from the Style Survey

*This is a stub. We welcome contributions to collect relevant style papers that are not mentioned in our survey.*

This page is intended to list the references from the Style Survey paper as a **sortable, searchable table**, and to provide simple visualizations over that list.

To filter the table, start typing in the search box below; click any column header to sort (uses [`tablesort`](https://github.com/tristen/tablesort)).

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
      <td><em>Example: Learning Invariant Representations of Social Media Users</em></td>
      <td>Noa A. et al.</td>
      <td><a href="https://github.com/noa/iur">link</a></td>
      <td>2020</td>
      <td>ACL</td>
    </tr>
  </tbody>
</table>

> **Note:** To include *all* references from the PDF, it’s easiest to export them as BibTeX and generate this table automatically. See `scripts/build-papers-table.py` for a starting point you can adapt to your own BibTeX file.

## Venue distribution

The bar chart below is computed directly from the **Venue** column of the table above.

<div style="width: 100%; max-width: 900px; height: 400px;">
  <canvas id="venue-chart"></canvas>
</div>

## Citation network (optional)

You can optionally provide a citation graph (e.g., which referenced papers cite each other) as JSON.
The visualization below expects a JSON payload of the form:

```json
{
  "nodes": [
    { "id": "Wegmann2025", "label": "Wegmann et al. 2025" }
  ],
  "links": [
    { "source": "Wegmann2025", "target": "Zhu2021" }
  ]
}
```

Paste such a JSON structure into the `<script id="citation-data">` block and it will be rendered automatically.

<div
  id="citation-network"
  style="width: 100%; max-width: 900px; height: 500px; border: 1px solid #ddd; margin-top: 1rem;"
></div>

<script type="application/json" id="citation-data">
{
  "nodes": [],
  "links": []
}
</script>

<link rel="stylesheet" href="../assets/tablesort.css">

<script src="https://unpkg.com/tablesort@5.6.0/dist/tablesort.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="../assets/sort-tables.js"></script>
<script src="../assets/papers-visualizations.js"></script>
