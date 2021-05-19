

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


def test_extra_newline_inside_html_tags_get_stripped():
    html = """<button class="navbar-toggler" type="button" 
    id="hamburger_menu" 
    data-toggle="collapse" 
    data-target="#navbarNav">"""
    minified_html = """<button class="navbar-toggler" type="button" id="hamburger_menu" data-toggle="collapse" data-target="#navbarNav">"""

    assert minified_html == minify(html)

def test_extra_space_inside_html_tags_get_stripped():
    html = """<button class="navbar-toggler"      data-target="#navbarNav">"""
    minified_html = """<button class="navbar-toggler" data-target="#navbarNav">"""
    assert minified_html == minify(html)


def test_code_blocks_are_not_affected():
    html = """<code>

    def protected():
        
        print("Ha ha I am safe from the minifier")

    </code>"""
    
    assert html == minify(html)


    