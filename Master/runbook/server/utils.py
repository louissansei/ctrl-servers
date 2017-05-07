#! /usr/bin/env python3

from flask import request


def require_json(func):
    """For use as a decorator on Flask resource methods to check that
    the Content-Type header has been set to json. If this header is
    not set correctly, Flask will raise an excpetion when
    request.get_json() is called.

    """
    def wrapper(*args, **kwargs):
        if not request.headers.get('Content-Type') == 'application/json':
            return "Content-Type header must be 'application/json'", 400
        else:
            return func(*args, **kwargs)
    return wrapper
