import logging
import sys
from typing import List

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

# from databases import DatabaseURL
# from loguru import logger
# from starlette.config import Config
# from starlette.datastructures import CommaSeparatedStrings, Secret

# from core.logging import InterceptHandler

API_PREFIX = "/api"

# JWT_TOKEN_PREFIX = "Token"  # noqa: S105
VERSION = "0.0.0"

# SECRET_KEY = "99fad391cacbb4f17e7a4abdb683d1e4ed5ae3af76c631dec4a8b94d2e84cacf"
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRES_MINUTES = 30

config = Config(".env")

# DEBUG: bool = config("DEBUG", cast=bool, default=False)

DATABASE_URL = "postgres://finance_web:ditiseensecuurwachtwoordvoormij@localhost:5432/finance_web"
# MAX_CONNECTIONS_COUNT: int = config("MAX_CONNECTIONS_COUNT", cast=int, default=10)
# MIN_CONNECTIONS_COUNT: int = config("MIN_CONNECTIONS_COUNT", cast=int, default=10)

# SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret)

PROJECT_NAME: str = "expense tracker" # config("PROJECT_NAME", default="FastAPI example application")
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
)

# logging configuration

# LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
# LOGGERS = ("uvicorn.asgi", "uvicorn.access")

# logging.getLogger().handlers = [InterceptHandler()]
# for logger_name in LOGGERS:
#     logging_logger = logging.getLogger(logger_name)
#     logging_logger.handlers = [InterceptHandler(level=LOGGING_LEVEL)]

# logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
