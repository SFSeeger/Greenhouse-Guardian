import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(raise_error_if_not_found=False))

if os.environ.get("ENVIRONMENT") == "dev":
    from .dev import *
elif os.environ.get("ENVIRONMENT") == "prod":
    from .prod import *
else:
    from .base import *
