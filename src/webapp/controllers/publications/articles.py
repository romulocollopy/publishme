from sanic import Blueprint
from webapp.app import App
from publishme.publications.use_cases.articles import ArticleDetailUseCase

bp = Blueprint('publications.articles')
app = App.build()


@bp.route('/@<username:\w+>/<article_slug:[\w-]+>/')
async def article_detail(request, username, article_slug):
    use_case = ArticleDetailUseCase(username, article_slug)
    context = use_case.execute()
    return app.template_engine.render(
        'publications/articles/article_detail.html',
        request, **context
    )
