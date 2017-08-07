class Router:

    def __init__(self, routes, engine):
        self.engine = engine
        self._routes = routes
        self.routes = dict()

    def load_routes(self):
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
