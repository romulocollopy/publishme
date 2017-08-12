import unittest
from webapp.app import app as webapp


class HelloWorldTestCase(unittest.TestCase):

    def setUp(self):
        app = webapp
        self.url = app.router.get_path_by_name('hello-world')
        self.engine = app.engine

    def test_200(self):
        request, response = self.engine.test_client.get(self.url)
        self.assertEqual(200, response.status)
        self.assertEqual('{"hello":"world"}', response.text)
