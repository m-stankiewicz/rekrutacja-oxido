from dotenv import load_dotenv
import os
import logging

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    INPUT_FILE = os.getenv("INPUT_FILE", "article.txt")
    OUTPUT_FILE = os.getenv("OUTPUT_FILE", "artykul.html")
    TEMPLATE_FILE = os.getenv("TEMPLATE_FILE", "szablon.html")
    COMPLETE_FILE = os.getenv("COMPLETE_FILE", "complete.html")
    OPENAI_ENGINE = os.getenv("OPENAI_ENGINE", "text-davinci-003")
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", 2000))
    LANGUAGE = os.getenv("LANGUAGE", "en")
    TIMEZONE = os.getenv("TIMEZONE", "UTC")
    LOG_FILE = os.getenv("LOG_FILE", "logs/project.log")  # Domyślnie logi w katalogu "logs"

    @staticmethod
    def validate():
        if not Config.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY nie został ustawiony w pliku .env.")
        if not Config.INPUT_FILE:
            raise ValueError("INPUT_FILE nie został ustawiony w pliku .env.")
        if not Config.OUTPUT_FILE:
            raise ValueError("OUTPUT_FILE nie został ustawiony w pliku .env.")
        if not Config.TEMPLATE_FILE:
            raise ValueError("TEMPLATE_FILE nie został ustawiony w pliku .env.")
        if not Config.COMPLETE_FILE:
            raise ValueError("COMPLETE_FILE nie został ustawiony w pliku .env.")

# Tworzenie katalogu na logi, jeśli nie istnieje
log_dir = os.path.dirname(Config.LOG_FILE)
os.makedirs(log_dir, exist_ok=True)

# Logger configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(Config.LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
