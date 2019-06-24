"""Application object is created on import and stored in :data:`app`."""

from .factory import create_app

app = create_app()
