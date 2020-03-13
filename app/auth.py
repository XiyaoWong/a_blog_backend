from flask import request
from flask import current_app
from flask_restful import abort
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired


def generate_token():
    s = Serializer(
        current_app.config["SECRET_KEY"],
        expires_in=eval(current_app.config["TOKEN_EXPIRES_IN"])
    )
    token = s.dumps("welcome")
    return token


def get_token():
    if 'Authorization' in request.headers:
        try:
            token_type, token = request.headers['Authorization'].split(None, 1)
        except ValueError:
            token_type = token = None
    else:
        token_type = token = None

    return token_type, token


def validate_token(token):
    s = Serializer(
        current_app.config["SECRET_KEY"],
        expires_in=eval(current_app.config["TOKEN_EXPIRES_IN"])
    )
    try:
        return s.loads(token)
    except (BadSignature, SignatureExpired):
        return False


def auth_required(f):
    def wrapper(*args, **kwargs):
        token_type, token = get_token()
        if request.method != "OPTIONS":
            if token_type is None or token_type.lower() != "bearer":
                abort(401, message="The token type must be bearer!")
            if token is None:
                abort(401, message="The token is missing!")
            if not validate_token(token):
                abort(401, message="Invalid token!")
        return f(*args, **kwargs)
    return wrapper
