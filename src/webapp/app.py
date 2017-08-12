from sanic import Sanic
from lib.routing.router import Router
from .routing.routes import routes


class App:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(App, cls).__new__(cls)
        return cls._instance

    def __init__(self, engine, router):
        self.engine = engine
        self.router = router

    def run(self, *args, **kwargs):
        self.engine.run(*args, **kwargs)

    @classmethod
    def build(cls, *args, **kwargs):
        engine = Sanic(*args, **kwargs)
        router = Router(routes, engine)
        return cls(engine, router)


app = App.build()
