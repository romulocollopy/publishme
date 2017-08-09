from unittest import TestCase, mock

from lib.routing.router import Router
from lib.routing.url import Url


class RouterTestCase(TestCase):

    def setUp(self):

        def hello_world(request):
            pass

        self.routes = (
            Url('/', hello_world, path_name="hello-world"),
        )
        self.router = Router(routes=self.routes, engine=mock.Mock())

    def test_instantiate(self):
        self.assertIsInstance(self.router, Router)

    def tearDown(self):
        self.router.__class__._instance = None
