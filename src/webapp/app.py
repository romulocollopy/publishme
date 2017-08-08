from sanic import Sanic
from lib.routing.router import Router
from .routing.routes import routes


class App:

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
