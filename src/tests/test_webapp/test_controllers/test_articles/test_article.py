import unittest
from unittest import mock
from webapp.app import App


class ArticleDetailTestCase(unittest.TestCase):

    def setUp(self):
        app = App()
        self.url = app.engine.url_for(
            'publications.articles.article_detail',
            author="roms",
            article_slug="gotta-catch-them-all"
        )
        self.engine = app.engine

    def test_200(self):
        request, response = self.engine.test_client.get(self.url)
        self.assertEqual(200, response.status)

    @mock.patch('webapp.controllers.publications.articles'
                '.ArticleDetailUseCase')
    def test_controller_calls_use_case(self, use_case):
        request, response = self.engine.test_client.get(self.url)
        use_case.assert_called_once_with('roms', 'gotta-catch-them-all')
        use_case().execute.assert_called_once_with()

    @mock.patch('webapp.controllers.publications.articles'
                '.ArticleDetailUseCase')
    def test_controller_content(self, use_case):
        title = "All the Single Ladies"
        use_case.return_value.execute.return_value = {
            'article': dict(title=title)
        }
        request, response = self.engine.test_client.get(self.url)
        self.assertIn(title, response.text)
