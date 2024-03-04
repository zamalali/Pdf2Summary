# Advanced NLP PDF to Bullet Point Summarizer 🗟

The Advanced NLP PDF Summarizer is a cutting-edge tool designed to process and condense lengthy PDF documents into concise, informative summaries. Leveraging state-of-the-art Natural Language Processing (NLP) techniques, this application extracts key information, presenting it in an easily digestible format. This README provides an overview of the advanced NLP methodologies employed by our application and guidance on how to utilize its features effectively.

## Features

- **PDF Text Extraction**: Utilizes PyPDF2 for efficient text extraction from PDF files, ensuring no content is overlooked during summarization.
- **Advanced Text Preprocessing**: Employs spaCy for sophisticated text preprocessing, including tokenization, lemmatization, and removal of stopwords, to refine the text for analysis.
- **Key Phrase Extraction**: Harnesses spaCy's NLP capabilities to identify and extract key phrases and named entities, pinpointing the most relevant information within the text.
- **Sentence Importance Scoring**: Implements a custom scoring algorithm based on the presence of key phrases and their centrality to the document's overall theme, highlighting sentences that encapsulate core ideas.
- **Dynamic Summarization**: Offers users the flexibility to adjust the extent of summarization, dynamically altering the summary's length based on user preference.

## How It Works

## Demo 🚀

Check out the how it works on Hugging Face:          [Space](https://huggingface.co/spaces/zamal/Pdf-2-Summary).

### Text Extraction and Preprocessing

The application begins by extracting text from the uploaded PDF document. It then preprocesses this text using spaCy, performing tokenization to break down the text into individual words and sentences, and lemmatization to reduce words to their base or dictionary form. This step is crucial for reducing complexity and focusing on the semantic meaning of the text.

### Key Phrase Extraction

Key phrases and named entities are extracted to identify the most significant elements of the text. This process involves analyzing noun chunks and named entities, which often represent the main subjects and concepts discussed in the document.

### Sentence Scoring and Summarization

Each sentence is scored based on its content, particularly the inclusion of key phrases and its relevance to the overall document. The scoring algorithm prioritizes sentences that are central to the document's theme, ensuring that the summary captures the essence of the original text. Users can adjust the summarization scale, allowing for a customizable summary length that fits their specific needs.

## Getting Started

To use the Advanced NLP PDF Summarizer, follow these steps:

1. **Installation**: Ensure you have Python and the necessary libraries installed, including PyPDF2, spaCy, and Streamlit.
2. **Running the Application**: Launch the Streamlit application by running `streamlit run app.py` in your terminal. This command will start the application and provide a URL to access the web interface.
3. **Uploading a PDF**: Use the web interface to upload a PDF document you wish to summarize.
4. **Adjusting Summary Length**: Use the provided slider to select your desired summary length as a percentage of the original content.
5. **Viewing the Summary**: The application will process your document and display a bullet-point summary highlighting the key information.

## Contribution

We welcome contributions from the community. If you have suggestions for improving this application or have identified bugs, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The spaCy team for their outstanding NLP library.
- The PyPDF2 project for their PDF processing capabilities.
- The Streamlit team for their intuitive app development framework.

Thank you for using the Advanced NLP PDF Summarizer. We hope this tool enhances your productivity and comprehension of complex documents.
