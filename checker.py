from flask import session
from functools import wraps

def check_login_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func( *args, **kwargs )
        return "you are not logged in site"
    return wrapper