import unittest
from webapp.app import App


class HelloWorldTestCase(unittest.TestCase):

    def setUp(self):
        app = App.build()
        self.url = app.engine.url_for('root.index')
        self.engine = app.engine

    def test_200(self):
        request, response = self.engine.test_client.get(self.url)
        self.assertEqual(200, response.status)
        self.assertEqual('{"hello":"world"}', response.text)
