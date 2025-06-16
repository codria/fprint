# fprint


`fprint` is a highly customizable replacement for Python's built-in `print()` function.
It supports:

- Text and background color (named colors and HEX codes)
- Fixed-width table-style formatting
- Horizontal centering
- Proper support for full-width characters (e.g., Japanese)
- Bold text
- Line number display
- Indentation support

Ideal for scripts, CLI tools, and logs that need readable, structured, or visually enhanced output.

---

## Installation

You can install directly from this GitHub repository:

```bash
pip install git+https://github.com/codria/fprint.git
```

---

## Usage

```python
from fprint import fprint

fprint("apple", "banana", row_width=10, fc="yellow", bc="#333333")
fprint("centered text", row_width=20, centering=True)
fprint("with line info", show_lineno=True)
```

---

## Arguments

| Name         | Type     | Description                                             |
|--------------|----------|---------------------------------------------------------|
| \*args       | str(s)   | Strings to print                                        |
| indent       | int      | Indentation level (2 spaces per level)                 |
| fc           | str      | Foreground color (name or HEX)                         |
| bc           | str      | Background color (name or HEX)                         |
| bold         | bool     | Whether to print in bold                               |
| sep          | str      | Separator between args                                 |
| end          | str      | Ending character (default: `\n`)                       |
| row_width    | int/str  | Column width or `"auto"`                               |
| centering    | bool     | Center-align text                                      |
| show_lineno  | bool     | Show file and line number                              |


---

## Available Named Colors

```
black, white, red, green, blue, cyan, magenta, yellow
```
