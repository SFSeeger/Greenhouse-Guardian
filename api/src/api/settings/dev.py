from .base import *

ALLOWED_HOSTS = ["*"]
DEBUG = True

FILE_UPLOAD_PERMISSIONS = 0o644

EMAIL_HOST = "mailhog"
DEFAULT_FROM_EMAIL = "Greenhouse Guardian <sfseeger.de>"
EMAIL_PORT = 1025

STATIC_ROOT = "/static/"

CORS_ALLOW_ALL_ORIGINS = True
