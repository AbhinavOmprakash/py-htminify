import re


def minify(html: str) -> str:
    """A function that strips extra white space in an HTML string"""

    for (expression, replacement) in patterns:
        html = re.sub(expression, replacement, html)

    return html

def _replace_space_inside_tag(match):
    # for replacing extra space characters In matched text
    return re.sub(r"(\s\s+)", " ", match.group(0))

patterns = [
    # Space characters refer to all characters denoted by r"\s"
    # for e.g tab, space, new line
    (r"(?<=>)\s*(?=<)", ""),  # For matching space characters between HTML tags
    (r"<!--*(.*?)--*>", ""),  # for matching comments
    (
        r"(?<=<)[\s\S]*?(?=>)",  #  For matching all text inside an HTML tag
        _replace_space_inside_tag,
    ),
    (  # this will prevent matching code inside <code|pre> tags nested inside <p> tags
        r"<\b(?!(code|pre|textarea)\b)\w+>[\s\S]*?<",  #  For matching text between tags
        _replace_space_inside_tag,                     # like <p> asdfawdf</p> but not Inside<code> </code>
    ),
    (
        r"</\w+>[\s\S]*?<",  #  For matching text between tags
        _replace_space_inside_tag,  # like <p> asdfawdf<p> but not Inside<code> </code>
    ),
]
