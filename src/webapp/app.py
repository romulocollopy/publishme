from sanic import Sanic
from sanic_jinja2 import SanicJinja2
from .settings import DEBUG, STATIC_ROOT


class App:
    _instance = None
    _loaded = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(App, cls).__new__(cls)
        return cls._instance

    def __init__(self, engine_class=None, template_engine_class=None):
        self.engine_class = engine_class or Sanic
        self.template_engine_class = template_engine_class or SanicJinja2
        if not self._loaded:
            self._loaded = True
            self.setup()

    def setup(self, *args, **kwargs):
        self.engine = self.engine_class(__name__, *args, **kwargs)
        self.load_template_engine()
        self.load_blueprints()
        self.load_static()

    def run(self, *args, **kwargs):
        self.engine.run(*args, **kwargs)

    def load_blueprints(self):
        from .controllers.root import bp as index
        from .controllers.publications.articles import bp as articles
        self.engine.blueprint(index)
        self.engine.blueprint(articles)

    def load_template_engine(self):
        self.template_engine = self.template_engine_class(self.engine)

    def load_static(self):
        if DEBUG:
            self.engine.static('/static', STATIC_ROOT)

    def destroy(self):
        self._instance = None
        self._loaded = False
        del self
