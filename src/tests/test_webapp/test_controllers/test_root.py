import unittest
from webapp.app import App as WebApp


class HelloWorldTestCase(unittest.TestCase):

    def setUp(self):
        app = WebApp.build()
        self.url = app.router.get_path_by_name('hello-world')
        self.engine = app.engine

    def test_200(self):
        request, response = self.engine.test_client.get(self.url)
        self.assertEqual(200, response.status)
        self.assertEqual('{"hello":"world"}', response.text)
