import os
import speech_recognition as sr
import requests
import nltk
import csv
import tkinter as tk
from tkinter import filedialog
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def record_from_mic(self):
        with sr.Microphone() as source:
            print("Say something!")
            audio = self.recognizer.listen(source)
            return self.recognizer.recognize_google(audio)

    def record_from_file(self, file_path):
        with sr.AudioFile(file_path) as source:
            audio = self.recognizer.record(source)
            return self.recognizer.recognize_google(audio)

class TextProcessor:
    def __init__(self):
        nltk.download('wordnet')
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def preprocess(self, text):
        tokens = word_tokenize(text)
        filtered_tokens = [self.lemmatizer.lemmatize(w.lower()) for w in tokens if w.lower() not in self.stop_words]
        return ' '.join(filtered_tokens)

class ProfanityChecker:
    def __init__(self, api_url):
        self.api_url = api_url

    def check(self, text):
        response = requests.get(f"{self.api_url}{text}")
        return response.json()['result'] != text

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze(self, text):
        return self.analyzer.polarity_scores(text)

class CSVWriter:
    def __init__(self, filename):
        self.filename = filename

    def write_row(self, row):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)

class Application:
    def __init__(self):
        self.recognizer = SpeechRecognizer()
        self.text_processor = TextProcessor()
        self.profanity_checker = ProfanityChecker(os.getenv("API_URL"))
        self.sentiment_analyzer = Sent
