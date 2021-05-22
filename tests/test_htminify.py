from htminify import minify


def test_the_space_between_html_tags_is_stripped():
    html = "<html>           </html>"
    minified_html = "<html></html>"

    assert minified_html == minify(html)


def test_newlines_between_html_tags_is_stripped():
    html = """<html>           
    
    
            </html>"""
    minified_html = "<html></html>"

    assert minified_html == minify(html)


def test_all_comments_are_stripped():
    html = """<html><!---A comment that shall not be there---></html>"""
    minified_html = "<html></html>"

    assert minified_html == minify(html)


def test_extra_newline_inside_html_tags_is_stripped():
    html = """<button class="navbar-toggler" type="button" 
    id="hamburger_menu" 
    data-toggle="collapse" 
    data-target="#navbarNav">"""
    minified_html = """<button class="navbar-toggler" type="button" id="hamburger_menu" data-toggle="collapse" data-target="#navbarNav">"""

    assert minified_html == minify(html)


def test_extra_space_inside_html_tags_is_stripped():
    html = """<button class="navbar-toggler"      data-target="#navbarNav">"""
    minified_html = """<button class="navbar-toggler" data-target="#navbarNav">"""
    
    assert minified_html == minify(html)

def test_code_blocks_are_not_affected():
    # note <code> print("foo") </code> == <code>print("foo")</code>
    # Htminify strips white space after ">" and white space before "<"
    html = """<code>def protected():
        
        print("Ha ha I am safe from the minifier")</code>"""
    assert html == minify(html)

def test_pre_blocks_are_not_affected():
    html = """<pre>def protected():
        
        print("Ha ha I am safe from the minifier")</pre>"""

    assert html == minify(html)

def test_textarea_blocks_are_not_affected():
    html = """<textarea>some text

    some more text</textarea>"""

    assert html == minify(html)

def test_newlines_between_html_tags_with_text_is_stripped():
    html = """<p>Some random text
    
    
    Some more random text</p>"""
    minified_html = """<p>Some random text Some more random text</p>"""
    assert minified_html == minify(html)

def test_nested_code_blocks_are_protected():
    html = """<p>Some random text
    <code>def protected():
        
        print("Ha ha I am safe from the minifier") </code>
    
    Some more random text</p>"""
    minified_html = """<p>Some random text<code>def protected():
        
        print("Ha ha I am safe from the minifier") </code>Some more random text</p>"""
    assert minified_html == minify(html)

def test_regex_is_not_case_sensitive():
    html = """<P>Some random text
    <CODE>def protected():
        
        print("Ha ha I am safe from the minifier")
        print("blah blah") </CODE>
    
    Some more random text </P>"""
    minified_html = """<P>Some random text<CODE>def protected():
        
        print("Ha ha I am safe from the minifier")
        print("blah blah") </CODE>Some more random text </P>"""
    assert minified_html == minify(html)


def test_javascript_inside_script_tags_is_minified():
    html = """<script>function myFunction(p1, p2) {
                        return p1 * p2;   
                    }           
    
    
            </script>"""
    minified_html = """<script>function myFunction(p1, p2) { return p1 * p2; } </script>"""

    assert minified_html == minify(html)