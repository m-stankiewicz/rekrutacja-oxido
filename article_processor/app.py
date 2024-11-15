
from .file_manager import FileManager
from .openai_processor import OpenAIProcessor
from .config import Config, logger

class ArticleProcessorApp:
    def __init__(self):
        self.file_manager = FileManager()
        self.openai_processor = OpenAIProcessor(api_key=Config.OPENAI_API_KEY)

    def process_article(self):
        logger.info("Rozpoczęto przetwarzanie artykułu.")
        try:
            article_content = self.file_manager.read_file(Config.INPUT_FILE)
            logger.info("Wczytano plik wejściowy: %s", Config.INPUT_FILE)
            html_content, token_usage = self.openai_processor.generate_html(article_content)
            logger.info("Wygenerowano kod HTML. Zużyto tokenów: %d", token_usage)
            self.file_manager.write_file(Config.OUTPUT_FILE, html_content)
            logger.info("Zapisano kod HTML do pliku: %s", Config.OUTPUT_FILE)
        except FileNotFoundError as e:
            logger.error("Nie znaleziono pliku: %s", e)
        except PermissionError as e:
            logger.error("Brak dostępu do pliku: %s", e)
        except Exception as e:
            logger.error("Wystąpił nieoczekiwany błąd: %s", e)
