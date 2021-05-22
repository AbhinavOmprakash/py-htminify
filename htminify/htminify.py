import re
import uuid



def minify(html: str) -> str:
    """A function that strips extra white space in an HTML string."""
    # protect tags like code|pre|textarea that are sensitive to whitespace
    # strip off whitespace
    # reintroduce the protected groups
    html = _protect_text(html)
    
    for (expression, replacement) in patterns:
        html = re.sub(expression, replacement, html, flags=re.IGNORECASE)
    
    html = _reintroduce_protected_text(html)
    
    return html


protected = {} # used to store the protected tags


def _protect_text(html):
    pre_text = re.findall(r"<pre>[\s\S]*?</pre>", html, re.IGNORECASE)
    code_text = re.findall(r"<code>[\s\S]*?</code>", html, re.IGNORECASE)
    text_area = re.findall(r"<textarea>[\s\S]*?</textarea>", html, re.IGNORECASE)

    for text_matches in [pre_text, code_text, text_area]:
        for match in text_matches:
            html = _substitute_with_hex_value(match, html)

    return html

def _substitute_with_hex_value(text_match, html):
    hex_id = uuid.uuid4().hex
    html = re.sub(re.escape(text_match), hex_id, html)
    protected[hex_id]=text_match
    return html
     
def _reintroduce_protected_text(html):
    for hex_id, protected_str in protected.items():
        html = re.sub(re.escape(hex_id), protected_str, html) 
    return html


def _replace_space_inside_tag(match):
    # for replacing extra space characters In matched text
    return re.sub(r"\s\s+", " ", match.group(0))

patterns = [
    # Space characters refer to all characters denoted by r"\s"
    # for e.g tab, space, new line
    (
        r"(?<=<)[\s\S]*?(?=>)",  #For matching all text inside an HTML tag < this text will be matched >
        _replace_space_inside_tag,
    ),
    (  
        r"(?<=>)[\s\S]*?(?=<)",  #  For matching text between tags
        _replace_space_inside_tag,  # like <p> asdfawdf</p> 
    ),
    (
        r"/>[\s\S]*?<", # for matching text in between <img/> text <tag>
        _replace_space_inside_tag
    ),
    (r"(?<=>)\s*(?=<)", ""),  # For matching space characters between HTML tags
    (r"<!--*(.*?)--*>", ""),  # for matching comments
    (r"^[\s]*(?=<)", ""), #stripping whitespace at the beginning of the file
]