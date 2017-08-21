class ArticleDetailUseCase:

    def __init__(self, username, article_slug):
        pass

    def execute(self):
        return {
            'article': {
                'title': 'Article Title',
                'body': '<p>Article body.</p>'
            }
        }
