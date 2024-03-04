import PyPDF2
import spacy
from collections import Counter
import heapq
import io

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def read_pdf(file_stream):
    text = ''
    reader = PyPDF2.PdfReader(file_stream)
    for page in reader.pages:
        text += page.extract_text() + ' '
    return text.strip()

def extract_key_phrases(text):
    doc = nlp(text)
    # Combine noun chunks and named entities as candidates for key phrases
    key_phrases = [chunk.text for chunk in doc.noun_chunks] + [ent.text for ent in doc.ents]
    return key_phrases

def score_sentences(text, key_phrases):
    sentence_scores = {}
    doc = nlp(text)
    for sent in doc.sents:
        for phrase in key_phrases:
            if phrase in sent.text:
                if sent in sentence_scores:
                    sentence_scores[sent] += 1
                else:
                    sentence_scores[sent] = 1
    return sentence_scores

def summarize_text(sentence_scores, num_points=5):
    summary_sentences = heapq.nlargest(num_points, sentence_scores, key=sentence_scores.get)
    # Format summary as bullet points
    summary = '\n'.join([f"- {sent.text}" for sent in summary_sentences])
    return summary
