from sanic import Blueprint
from webapp.app import App

bp = Blueprint(__name__)
app = App.build()


@bp.route('/')
async def hello_world(request):
    return app.template_engine.render('index.html', request)
