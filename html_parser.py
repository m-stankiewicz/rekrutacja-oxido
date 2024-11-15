
from article_processor.config import Config
from article_processor.file_manager import FileManager

class HTMLParser:
    def __init__(self):
        self.template_path = Config.TEMPLATE_FILE
        self.article_path = Config.OUTPUT_FILE
        self.output_path = Config.COMPLETE_FILE

    def parse(self):
        template_content = FileManager.read_file(self.template_path)
        article_content = FileManager.read_file(self.article_path)
        complete_content = template_content.replace(
            "<main>", f"<main>\n{article_content}\n"
        )
        FileManager.write_file(self.output_path, complete_content)

def main():
    parser = HTMLParser()
    parser.parse()

if __name__ == "__main__":
    main()
