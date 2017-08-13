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

    def __init__(self, engine, template_engine_class):
        if self._loaded:
            return
        self._loaded = True
        self.engine = engine
        self.template_engine_class = template_engine_class
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

    @classmethod
    def build(cls, *args, **kwargs):
        engine = Sanic(__name__, *args, **kwargs)
        template_engine_class = SanicJinja2
        return cls(engine, template_engine_class)
