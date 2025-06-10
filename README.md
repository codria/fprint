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

## 🔧 Installation


You can install directly from this GitHub repository:

```bash
pip install git+https://github.com/sleepingHimazin/fprint.git
```

## Usage

```python
from fprint import fprint

fprint("apple", "banana", row_width=10, fc="yellow", bc="#333333")
fprint("centered text", row_width=20, centering=True)
fprint("with line info", show_lineno=True)
```
