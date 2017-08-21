from sanic import Blueprint
from webapp.app import App
from publishme.publications.use_cases.articles import ArticleDetailUseCase

bp = Blueprint('publications.articles')
app = App()


@bp.route('/~<author:\w+>/<article_slug:[\w-]+>/')
async def article_detail(request, author, article_slug):
    use_case = ArticleDetailUseCase(author, article_slug)
    context = use_case.execute()
    return app.template_engine.render(
        'publications/articles/article_detail.html',
        request, author=author, **context
    )
