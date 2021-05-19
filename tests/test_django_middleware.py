
import sys
import unittest
from unittest.mock import Mock, patch, MagicMock, PropertyMock
import pytest
from helpers import construct_django_response

import htminify
# replace imported modules with mocks
sys.modules["django"] = MagicMock()
sys.modules["django.conf"] = MagicMock() 

#import dj after intercepting mocks
from htminify import dj

#store the mock object imported by dj for later access
mock_settings = dj.settings

middleware = dj.StripWhitespaceMiddleware()

def test_should_NOT_minify_when_debug_is_true_and_NOT_overridden():
    # modify the mock settings imported
    mock_settings.DEBUG = True
    mock_settings.ALWAYS_MINIFY = False
    
    original_response = construct_django_response()
    middleware_response = middleware.process_response(Mock(),construct_django_response())

    assert original_response.content == middleware_response.content

def test_should_minify_when_debug_is_false_and_NOT_overridden():
    mock_settings.DEBUG = False
    mock_settings.ALWAYS_MINIFY = False
    
    original_response = construct_django_response()
    middleware_response = middleware.process_response(Mock(),construct_django_response())

    assert original_response.content != middleware_response.content


# @pytest.mark.skip(reason="test fails even though the functionality works")

def test_should_minify_when_debug_is_true_and_IS_overridden():
    mock_settings.DEBUG = True
    mock_settings.ALWAYS_MINIFY = True

    original_response = construct_django_response()
    middleware_response = middleware.process_response(Mock(),construct_django_response())

    assert original_response.content != middleware_response.content


def test_should_not_throw_an_error_when_always_minify_is_not_defined():
    mock_settings.DEBUG = True
    del mock_settings.ALWAYS_MINIFY
    middleware_response = middleware.process_response(Mock(),construct_django_response())

    # test passes only if no exception is thrown

    