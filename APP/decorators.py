from functools import wraps
from flask import abort
from flask_login import current_user

from APP.utils import redirect_back


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # print(current_user.is_authenticated)
        # print(current_user.is_admin)
        if current_user.is_authenticated and current_user.is_admin:
            return f(*args, **kwargs)
        else:
            abort(404)

    return decorated_function
