import decouple
from sanic import Sanic
from sanic_jinja2 import SanicJinja2
from webapp.controllers.root import bp as root_controller

env_repository = decouple.RepositoryIni('../settings.ini')
config = decouple.Config(env_repository)

DEBUG = config('DEBUG', cast=bool, default=False)
app = Sanic(__name__)
if DEBUG:
    app.static('/static', '../static')

jinja = SanicJinja2(app)
app.blueprint(root_controller)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=DEBUG)
