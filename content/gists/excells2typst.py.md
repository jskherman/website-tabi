+++
title = "📋excells2typst.py"
description = "A Python script that converts a selected region in Microsoft Excel to a table in Typst."
date = 2024-05-11
draft = true
# authors = ["flaribbit"]

[taxonomies]
tags = ["python", "typst", "scripting", "ms excel", "data extraction"]

[extra]
# social_media_card = ""
+++

This is a Python script that converts a selected region of cells in Microsoft Excel to a table in Typst.

{% admonition(type="note", title="Attribution") %}
The code below was created by [**@flaribbit**](https://github.com/flaribbit) and was originally shared on the [Typst Discord server](https://discord.com/channels/1054443721975922748/1238666728888864869) on `2024-05-11`. The comments are not included in the original snippet and were added after the fact using [Meta's Llama 3 70B LLM](https://llama.meta.com/llama3/) for documentation.
{% end %}

{% admonition(type="warning", title="Disclaimer") %}
**Use the script below at your own risk**. The owner of the current website does not guarantee the accuracy of the code provided below (nor of any code provided on this website) and is not responsible for any damages that may arise from using the code. Please review the code and understand what it does before using it.

The owner of the current website does not also claim ownership of the code below. The code is rightfully owned by the original author, [**@flaribbit**](https://github.com/flaribbit).
The code is shared here for preservation and for educational purposes.
{% end %}

<!-- {# remote_text(src="@/gists/excells2typst.py.md/excells2typst.py") #} -->

```python
# Import the win32com.client module, which provides an interface to interact with Microsoft Office applications
import win32com.client

# Get the active Excel application object
excel = win32com.client.GetActiveObject("Excel.Application")

# Get the active workbook and sheet
wb = excel.ActiveWorkbook
sheet = wb.ActiveSheet

# Get the selected range of cells
selected = excel.Selection

# Get the number of columns in the selected range
columns = selected.Columns.Count

# Open a file to write the Typst table to
out = open("output.typ", "w", encoding="utf-8")

# Write the table header
out.write(f"#table(columns: {columns},")

# Iterate over each row in the selected range
for i in range(selected.Rows.Count):
    out.write("\n  ")
    # Iterate over each column in the selected range
    for j in range(selected.Columns.Count):
        # Get the current cell
        cell = selected.Cells(i + 1, j + 1)
        
        # Check if the cell is part of a merged range
        if cell.MergeCells:
            # Check if the cell is the top-left cell of the merged range
            is_top_left = cell.Address == cell.MergeArea.Cells(1, 1).Address
            if is_top_left:
                # Get the number of rows and columns in the merged range
                rows = cell.MergeArea.Rows.Count
                cols = cell.MergeArea.Columns.Count
                # Get the text value of the cell
                value = cell.Text
                # Write the table cell with rowspan and colspan attributes if necessary
                out.write("table.cell(")
                if rows > 1:
                    out.write(f"rowspan: {rows}, ")
                if cols > 1:
                    out.write(f"colspan: {cols}, ")
                # Remove the trailing comma and space
                out.seek(out.tell() - 2)
                out.write(f")[{value}], ")
            else:
                # If the cell is not the top-left cell of the merged range, skip it
                pass
        else:
            # If the cell is not part of a merged range, just write its text value
            value = cell.Text
            out.write(f"[{value}], ")

# Close the table and file
out.write("\n)\n")
out.close()
```

{% admonition(type="info") %}

A caveat: for cells that only have rowspans (no unit cells), they will not span the proper cell size (and produce a wrong output) in Typst because the row height is `auto`. A suggested workaround is by assigning a fixed height to the rows in the output table in Typst (e.g. `table(rows: 2em)`).

See [related GitHub discussion](https://github.com/typst/typst/discussions/4116).
{% end %}

