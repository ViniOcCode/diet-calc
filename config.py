import os
import secrets

class Config:
    # Configure SECRET_KEY in production. The random fallback keeps local
    # development usable without committing a reusable secret to the repo.
    SECRET_KEY = os.environ.get("SECRET_KEY") or secrets.token_hex(32)
