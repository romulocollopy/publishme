from sanic import Blueprint
from webapp.app import App

bp = Blueprint('root')
app = App()


@bp.route('/')
async def index(request):
    return app.template_engine.render('index.html', request)
