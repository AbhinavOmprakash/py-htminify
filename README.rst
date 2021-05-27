HTMinify
========

      .. image:: https://codecov.io/gh/AbhinavOmprakash/py-htminify/branch/Production/graph/badge.svg?token=0POQLYOEY5
    
A lightweight HTML minifier for *all* Python web frameworks and WSGI apps.

**This project is still in BETA**  

Features
________

* Using a web framework, like django, flask, and pyramid? We got you covered.
* Or you're feeling adventurous and you're building your own wsgi app? We got you covered there too. This will work with any program that complies with the WSGI specification
* Using an encoding that is not UTF-8? Just pass an argument, and we'll take it from there. 😉   
* Mixing Javascript and html? We'll try to minify that too, without judging you too much. (No promises though😜).

Installation
____________
With pip 

.. code-block:: bash

    $ pip install htminify

With poetry

.. code-block:: bash

    $ poetry add htminify


Usage
_____

**For Django**

The middleware goes in your ``wsgi.py`` file. An example ``wsgi.py`` will look like this.

.. code-block:: Python

    # wsgi.py
    import os

    from django.core.wsgi import get_wsgi_application
    from htminify.wsgi import StripWhitespaceMiddleware # add this!
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

    application = get_wsgi_application()
    application = StripWhitespaceMiddleware(application) # add this too!
    


**For Flask**

Flask provides access to its wsgi app, which you can pass as an argument to the middleware. 
You are essentially wrapping the middleware around the wsgi application.
An example flask file would be like this.

.. code-block:: Python

    # app.py
    from flask import Flask
    from htminify.wsgi import StripWhitespaceMiddleware # add this!

    app = Flask(__name__)
    app.wsgi_app = StripWhitespaceMiddleware(app.wsgi_app) # add this too!
    
    @app.route('/')
    def hello():
        return "Hello, world."

    if __name__=="__main__":
        app.run()


Note that we are wrapping the ``app.wsgi_app`` object and not the ``app`` object.

**For any other WSGI app.**


A similar procedure can be followed to integrate the middleware with other wsgi-Python web frameworks.
Just wrap the middleware around the wsgi app.

.. code-block:: Python

    # app.py
    from htminify.wsgi import StripWhitespaceMiddleware # add this!
    wsgi_app = StripWhitespaceMiddleware(wsgi_app) # wrap around 
    


Configuration
_____________

**if you don't want to minify when debug is true**

You can do something like this

.. code-block:: Python

    # app.py
    if not debug:
        wsgi_app = StripWhitespaceMiddleware(wsgi_app) 
    
**If you're using encoding other than UTF-8**

Pass the encoding-type to the middleware when wrapping the app.

.. code-block:: Python

    # app.py
    from htminify.wsgi import StripWhitespaceMiddleware # add this!
    wsgi_app = StripWhitespaceMiddleware(wsgi_app, "UTF-16") # pass the encoding


TODO
____

*New Features*

#. Minify Json content.
#. Add ASGI support.

*Documentation*

* Generate Documentation and push to read the docs.
* Add information for contributing.

*Testing*

* Improve test suite for wsgi middleware.
