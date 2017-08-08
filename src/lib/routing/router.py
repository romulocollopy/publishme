from lib.errors import ConfigurationError


class Router:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Router, cls).__new__(cls)
        return cls._instance

    def __init__(self, routes=None, engine=None):
        self.routes = dict()
        self.set_engine(engine)
        self.load_routes(routes)

    def set_engine(self, engine):
        if hasattr(self, 'engine') and engine:
            raise ConfigurationError('Cannot set engine in runtime')
        if engine:
            self.engine = engine

    def load_routes(self, routes):
        if hasattr(self, '_routes') and routes:
            raise ConfigurationError('Cannot set routes in runtime')
        if routes:
            self._routes = routes

        for path, function, path_name in self._routes:
            self.engine.add_route(function, path)
            self.routes[path_name] = (path, function)

    def get_controler_by_path_name(self, path_name):
        return self.routes[path_name][1]

    def get_path_by_name(self, path_name):
        return self.routes[path_name][0]

    @classmethod
    def build(cls, routes, engine):
        return cls(routes, engine)
