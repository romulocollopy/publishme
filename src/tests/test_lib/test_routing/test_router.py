from unittest import TestCase, mock

from lib.routing.router import Router
from lib.routing.url import Url


def hello_world(request):
    pass


class RouterTestCase(TestCase):

    def setUp(self):
        Router._instance = None
        self.routes = (
            Url('/popcorn', hello_world, path_name="hello-world"),
        )
        self.engine = mock.Mock()
        self.router = Router(routes=self.routes, engine=self.engine)

    def test_instantiate(self):
        self.assertIsInstance(self.router, Router)

    def test_build(self):
        self.router.__class__._instance = None
        router = Router.build(routes=self.routes, engine=self.engine)
        self.assertIsInstance(router, Router)

    def test_get_controler_by_path_name(self):
        controller = self.router.get_controler_by_path_name('hello-world')
        self.assertEqual(hello_world, controller)

    def test_get_path_by_name(self):
        path = self.router.get_path_by_name('hello-world')
        self.assertEqual('/popcorn', path)

    def test_set_routes(self):
        self.assertEqual(self.routes, self.router._routes)

    def test_set_engine(self):
        self.assertEqual(self.engine, self.router.engine)

    def test_load_routes(self):
        calls = [mock.call(p, f) for f, p, pn in self.routes]
        self.router.engine.add_route.assert_has_calls(calls)
        for f, p, pn in self.routes:
            self.assertEqual(
                self.router.routes[pn], (f, p)
            )

    def tearDown(self):
        self.router.__class__._instance = None
