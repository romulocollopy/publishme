import unittest
from unittest import mock
from sanic import Sanic
from sanic_jinja2 import SanicJinja2
from webapp.app import App


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = App()

    def test_instantiate(self):
        app = App()
        self.assertIsInstance(app, App)

    def test_is_singleton(self):
        app = App()
        app2 = App()
        self.assertIs(app, app2)

    def test_uses_sanic_engine(self):
        self.assertIsInstance(self.app.engine, Sanic)

    def test_uses_SanicJinja2_template(self):
        self.assertIsInstance(self.app.template_engine, SanicJinja2)

    @mock.patch.object(App, 'setup')
    def test_run_setup_on_first_instantiation(self, mock_setup):
        self.app.destroy()
        App()
        mock_setup.assert_called_once_with()

    @mock.patch.object(App, 'setup')
    def test_does_not_setup_on_second_instantiation(self, mock_setup):
        self.app.destroy()
        App()
        mock_setup.assert_not_called()

    def tearDown(self):
        self.app.destroy()
