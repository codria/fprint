from fprint import fprint

# Title
fprint(
    "Experiment Summary",
    row_width=31,   # 31 spaces + 2 separators = 33 characters
    centering=True,
    fc="white",
    bc="#333333",
    bold=True,
)

# Header
fprint(
    "Metric", "Value",
    row_width=15,   # 15 spaces * 2 columns + 3 separators = 33 characters
    fc="black",
    bc="yellow",
)

# Rows
fprint("Accuracy", "0.91", row_width=15, fc="cyan")
fprint("Time [s]", "11.8", row_width=15, fc="green", show_lineno=True)
