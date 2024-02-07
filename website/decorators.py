from functools import wraps
from flask_login import current_user
from flask import abort

def role_required(*roles):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated or not any(role.name in roles for role in current_user.roles):
                return abort(403)  # Forbidden access
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper