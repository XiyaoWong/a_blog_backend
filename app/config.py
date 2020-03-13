import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "a secret string")
    BUNDLE_ERRORS = True
    TOKEN_EXPIRES_IN = os.getenv("TOKEN_EXPIRES_IN")
