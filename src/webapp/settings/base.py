import decouple
from pathlib import Path

PROJECT_ROOT = Path(__file__).parents[2]
STATIC_ROOT = str(PROJECT_ROOT.parent / 'static')

DEBUG = decouple.config('DEBUG', default=False, cast=bool)
PORT = decouple.config('PORT', default=5000, cast=int)
