from sanic import Blueprint
from webapp.app import App

bp = Blueprint('publications.articles')
app = App.build()


@bp.route('/@<username:\w+>/<article_slug:[\w-]+>/')
async def article_detail(request, username, article_slug):
    return app.template_engine.render(
        'publications/articles/article_detail.html',
        request
    )
