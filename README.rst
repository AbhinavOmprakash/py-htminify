HTMinify
========
A lightweight HTML minifier for Python web frameworks.

Installation
------------
with pip 

.. code-block:: bash
    $ pip install htminify

    

With pipenv

.. code-block:: bash
    $ pipenv install htminify


With poetry

.. code-block:: bash
    $ poetry add htminify


Usage
-----
*Django*
Just add it to the bottom of your middleware like this.

.. code-block:: Python
    MIDDLEWARE = [
            #... all your other middleware
            'htminify.dj_middleware.StripWhitespaceMiddleware',
            ]


Additional settings

By default the minification only occurs when `DEBUG = False`. 
If you want to override this behavior and have minification during development.
And `ALWAYS_MINIFY = True` to settings.py 

.. code-block:: Python
    # settings.py
    ALWAYS_MINIFY = True

