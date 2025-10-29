import inspect
import sys
import re

import colorama
import wcwidth
from termcolor import colored

# colorama の初期化（Windows対策）
colorama.init()



#==================== 配色設定 ====================#
def hex_to_rgb(hex_color: str):
    """HEXカラー (#RRGGBB) を (R, G, B) のタプルに変換"""
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_ansi(r: int, g: int, b: int, is_bg: bool = False):
    """(R, G, B) を ANSI エスケープコードに変換"""
    code_type = 48 if is_bg else 38  # 文字色 (38) or 背景色 (48)
    return f"\033[{code_type};2;{r};{g};{b}m"

def apply_color(text: str, color: str, is_bg: bool = False) -> str:
    """色を適用（HEXコードまたは名前）"""
    if color in ["", "none"]:
        return text

    valid_colors = ['black', 'white', 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow']

    # HEXカラーの場合
    if re.match(r"^#([A-Fa-f0-9]{6})$", color):
        r, g, b = hex_to_rgb(color)
        return rgb_to_ansi(r, g, b, is_bg) + text

    # 色名の場合
    if color in valid_colors:
        color_type = f"on_{color}" if is_bg else color
        try:
            # termcolorはANSIコードを付けるだけなのでrepr不要
            return colored(text, color_type) if not is_bg else colored(text, on_color=color_type)
        except Exception:
            pass

    # 無効な色指定
    raise ValueError(f"Invalid color: '{color}'. Valid options are: {', '.join(valid_colors)}")



#==================== テーブル整形用 文字数設定 ====================#
def get_display_width(text: str) -> int:
    """文字列の表示幅を計算（全角文字を2文字分として扱う）"""
    return sum(wcwidth.wcwidth(c) if wcwidth.wcwidth(c) > 0 else 1 for c in text)

def pad_string(text: str, width: int, centering: bool = False) -> str:
    """指定幅に合わせてパディング（全角対応、センタリング対応）"""
    current_width = get_display_width(text)
    
    # 幅を超えた場合は「...」を末尾に追加
    if current_width > width:
        truncated_text = text
        while get_display_width(truncated_text + "...") > width:
            truncated_text = truncated_text[:-1]
        text = truncated_text + "..."
        
    padding = width - get_display_width(text)
    
    if centering:
        left_padding = padding // 2
        right_padding = padding - left_padding
        return " " * left_padding + text + " " * right_padding
    else:
        return text + " " * max(padding, 0)


#==================== 本体 ====================#
def fprint(
            *args,
            indent: int = 0,
            fc: str = "none",
            bc: str = "none",
            bold: bool = False,
            sep: str = " ",
            end: str = "\n",
            row_width = 0,
            centering: bool = False,
            show_lineno: bool = False
        ):
    """
    コンソールに色付きでテーブル形式または通常の文字列を出力するカスタム関数。

    引数:
    * args: 出力したい文字列を指定する。print関数の引数を渡すことができる。
    * indent: 出力時のインデントの深さ。1ならスペース2個、2ならスペース4個とインデントされる。
    * fc: 文字色。文字色を指定するための色名またはHEXカラーコード（例："red"、"#ff00ff"）。
    * bc: 背景色。背景色を指定するための色名またはHEXカラーコード（例："yellow"、"#00ff00"）。
    * bold: Trueにすると文字列が太字になる。
    * sep: 各文字列の区切り文字。デフォルトは空白（" "）。
    * end: 出力の最後に付ける文字列。デフォルトは改行（"\\n"）。
    * row_width: "auto"/整数値。出力文字列の横幅を指定する。テーブル形式で、指定幅を超える場合は「...」に置換される。
    * centering: Trueにすると、文字列が指定幅内で水平センタリングされる。
    * show_lineno: printが記述されたモジュールと行番号が表示される。
     
    使用例:
    * fprint("apple", "banana", "cherry", row_width=10, fc="cyan", bc="black")
    * fprint("これは長い文字列ですが...", "短い文字列", row_width=10, fc="yellow", bc="#333333")
    * fprint("センタリング", row_width=20, centering=True)

    指定可能色名:
    * black, white, red, green, blue, cyan, magenta, yellow
    """
    indent_spaces = " " * (indent * 2)

    if row_width == "auto":
        # 最長の文字列に合わせて row_width を自動で調整
        row_width = max(get_display_width(str(arg)) for arg in args)

    if row_width > 0:
        formatted_args = [pad_string(str(arg), row_width, centering) for arg in args]
        text = "|" + "|".join(formatted_args) + "|"
        # text = "| " + " | ".join(formatted_args) + " |"
    else:
        text = sep.join(map(str, args))

    # 色設定
    text = apply_color(apply_color(text, fc), bc, is_bg=True)
    
    if bold:
        text = "\033[1m" + text

    if show_lineno:
        caller_frame = inspect.currentframe().f_back
        file_path = caller_frame.f_code.co_filename  # ファイルのフルパス
        line_number = caller_frame.f_lineno
        line_info = apply_color(apply_color(f'\t\t(File "{file_path}", line {line_number})', "#333333"), "#181818", is_bg=True)
        text += line_info

    sys.stdout.write(indent_spaces + text + "\033[0m" + end)


#==================== テスト ====================#
if __name__=="__main__":
    fprint("row 1", "row 2", "row 3", row_width=10, fc="#000000", bc="#777777", centering=True)
    fprint("apple", "banana", "cherry", row_width=10, fc="cyan", bc="black")
    fprint("これは長い文字列ですが...", "短い文字列", row_width=10, fc="yellow", bc="#333333", bold=True)
    fprint("センタリング", row_width=20, centering=True)
    fprint("太字の文字", fc="red", bold=True)
    fprint("インデント2", indent=2)
    fprint("インデント2, ライン番号表示", indent=2, show_lineno=True)
    fprint("fc:black, bc:white, インデント2, ライン番号表示", indent=2, fc="black", bc="white", show_lineno=True)
    fprint("fc:18, bc:33, インデント2, ライン番号表示", indent=2, fc="#181818", bc="#333333", show_lineno=True)
    fprint("fc:white, インデント2, ライン番号表示", indent=2, fc="white", show_lineno=True)
    fprint("fc:black, インデント2, ライン番号表示", indent=2, fc="black", show_lineno=True)
    fprint("bc:white, インデント2, ライン番号表示", indent=2, bc="white", show_lineno=True)
    fprint("bc:black, インデント2, ライン番号表示", indent=2, bc="black", show_lineno=True)
