import os
from openai import OpenAI
from .config import Config, logger

class OpenAIProcessor:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def generate_html(self, article_content: str):
        prompt = (
            "Generate the content to be placed between <body> and </body> tags in an HTML document. "
            "Follow these guidelines:\n"
            "- Use appropriate HTML tags to structure the content (e.g., <article>, <section>, <header>, <footer>, etc.).\n"
            "- Identify places where images should be included and use the <img> tag with the attribute src='image_placeholder.jpg'.\n"
            "- Add a descriptive and detailed alt attribute to each <img> tag, providing a comprehensive description of the image. "
            "The alt text must always be in English, regardless of the language of the article content. For example, "
            "'A close-up of hands planting seeds in a freshly tilled garden bed, surrounded by green plants, gardening tools, and rich brown soil.'\n"
            "- Place captions for images using the <figcaption> tag inside <figure> elements. Captions should always match the language of the article content.\n"
            "- Do not include any CSS or JavaScript in the output.\n"
            "- Only return the content meant to be placed inside <body>, excluding the <body> opening and closing tags.\n"
            "- Ensure the output is clean, valid HTML and adheres to W3C standards.\n"
            "- Do not include any markdown syntax, such as ```HTML or ```.\n"
            "\n"
            "The content of the article is provided below:\n\n"
            f"{article_content}"
        )

        try:
            # Użycie klienta OpenAI do wywołania modelu
            response = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are an assistant specializing in generating clean, structured, and valid HTML.",
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=Config.OPENAI_ENGINE,
                max_tokens=Config.MAX_TOKENS,
                temperature=Config.TEMPERATURE,
            )

            # Pobranie danych z odpowiedzi
            token_usage = response.usage.total_tokens if response.usage else 0
            if not response.choices or len(response.choices) == 0:
                raise ValueError("No response in 'choices'.")

            content = response.choices[0].message.content.strip()
            logger.info("Tokens used: %d", token_usage)

            return content, token_usage

        except Exception as e:
            logger.error("Error during communication with OpenAI: %s", e)
            raise
