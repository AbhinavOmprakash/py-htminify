"""TODO newline in paragraph tags """
import re

patterns=[
    r"(?<=>)\s*(?=<)", # For matching space and new line characters between HTML tags
    r"<!-*(.*)-*>", # for matching comments
]

def minify(html: str) -> str:
    for pattern in patterns:
        html = re.sub( pattern,'', html)

    return html
    