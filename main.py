
from article_processor.config import Config
from article_processor.app import ArticleProcessorApp

def main():
    Config.validate()
    app = ArticleProcessorApp()
    app.process_article()

if __name__ == "__main__":
    main()
