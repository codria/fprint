# fprint

`fprint` is a custom Python print utility with:

- ✅ Indentation support
- ✅ Foreground and background color (HEX and name-based)
- ✅ Full-width character support
- ✅ Table-style formatting with fixed width
- ✅ Centering and truncation with `...`
- ✅ Source line info with `show_lineno=True`

## Usage

```python
from fprint import fprint

fprint("apple", "banana", raw_width=10, fc="yellow", bc="#333333")
fprint("centered text", raw_width=20, centering=True)
fprint("with line info", show_lineno=True)
