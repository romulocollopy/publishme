import decouple
from pathlib import Path

PROJECT_ROOT = Path(__file__).parents[2]
STATIC_ROOT = str(PROJECT_ROOT.parent / 'static')

env_repository = decouple.RepositoryIni(PROJECT_ROOT.parent / 'settings.ini')

config = decouple.Config(env_repository)

DEBUG = config('DEBUG', default=False, cast=bool)
PORT = decouple.config('PORT', default=500, cast=int)
