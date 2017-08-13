from sanic import Blueprint

bp = Blueprint(__name__)


@bp.route('/')
async def index(request):
    from app import jinja
    return jinja.render(
        'index.html', request
    )
