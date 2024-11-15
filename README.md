
# Oxido Junior AI Developer Recruitment Task

Welcome to the submission for the Oxido Junior AI Developer recruitment task! This project involves building an application to process text articles using OpenAI's API, generating structured HTML content based on predefined guidelines.

---

## **Project Overview**

The application performs the following steps:
1. Reads a text file containing an article.
2. Processes the article content using a detailed prompt to generate HTML.
3. Generates well-structured HTML with:
   - Appropriate semantic tags.
   - Placeholder images (`<img>` with descriptive `alt` attributes).
   - Captions for images matching the article's language.
4. Saves the generated HTML in `artykul.html`.
5. Optionally, provides a preview template (`szablon.html`) for displaying the generated HTML.

---

## **Prompt Description**

The application uses a carefully crafted prompt to ensure high-quality HTML output. The prompt includes:
- Semantic HTML structure using tags like `<article>`, `<section>`, `<header>`, and `<footer>`.
- Image placeholders (`<img src="image_placeholder.jpg">`) with detailed and descriptive `alt` attributes always in English. Example:
  ```html
  <img src="image_placeholder.jpg" alt="A close-up of hands planting seeds in a freshly tilled garden bed, surrounded by green plants, gardening tools, and rich brown soil.">
  ```
- Captions for images in `<figcaption>` tags. The captions are generated in the language of the article.
- Exclusion of CSS or JavaScript in the generated HTML.
- Clean and valid HTML that adheres to W3C standards.

---

## **Files in the Repository**

### Tracked files
1. **`main.py`**  
   The main script that orchestrates the processing of the article, interaction with the OpenAI API, and saving the generated output.

2. **`config.py`**  
   Configuration file for handling environment variables and logging setup.

3. **`artykul.html`**  
   The final HTML generated from the article content.

4. **`szablon.html`** (optional)  
   A basic HTML template for previewing the generated content.

5. **`README.md`**  
   Documentation for the project.

6. **`.env.example`**  
   Template file for environment variables (excluding sensitive data).

### Ignored files (.gitignore)
- **`.env`**: Contains sensitive API keys and configuration.
- **`logs/`**: Directory for log files.
- **`__pycache__/`**: Directory for Python cache files.

---

## **Setup and Installation**

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with the following format (or use `.env.example`):
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   INPUT_FILE=article.txt
   OUTPUT_FILE=artykul.html
   TEMPLATE_FILE=szablon.html
   COMPLETE_FILE=complete.html
   OPENAI_ENGINE=text-davinci-003
   TEMPERATURE=0.7
   MAX_TOKENS=2000
   LANGUAGE=en
   TIMEZONE=UTC
   LOG_FILE=logs/project.log
   ```

4. Ensure the input article file (`article.txt`) is present in the root directory.

---

## **How to Run**

Run the application using the following command:
```bash
python main.py
```

---

## **Example Output**

### Generated HTML (stored in `artykul.html`):
```html
<article>
    <header>
        <h1>How to Grow a Garden</h1>
    </header>
    <section>
        <h2>1. Choose the Right Location</h2>
        <p>Make sure your garden gets plenty of sunlight and has good drainage.</p>
        <figure>
            <img src="image_placeholder.jpg" alt="A sunny backyard with a well-maintained garden bed surrounded by vibrant green grass and blooming flowers.">
            <figcaption>A sunny and well-drained garden location.</figcaption>
        </figure>
    </section>
    ...
</article>
```


## **Parser Functionality**

This project includes a parser functionality to generate a complete HTML file (`complete.html`) by merging the generated content with the provided template (`szablon.html`).

### **How to Use the Parser**

To use the parser and generate the complete HTML file:
1. Ensure the `szablon.html` file is present in the root directory.
2. Run the following command:
   ```bash
   python html_parser.py
   ```
3. The script will read the `szablon.html` and `artykul.html` files, insert the generated content into the `<body>` of the template, and save the result as `complete.html`.

The resulting `complete.html` can be opened in any web browser for preview.


---

## **Key Highlights**

- **AI Prompt Engineering:**  
  - Ensures alt attributes are always in English.  
  - Generates captions in the article's original language.
- **W3C-Compliant HTML:**  
  - Clean, structured, and valid output.  
- **Configurable Settings:**  
  - `.env` file allows easy configuration of API keys and file paths.

---

## **Acknowledgments**

Thank you for the opportunity to work on this challenge. I look forward to contributing to Oxido's mission of building AI-first solutions.
