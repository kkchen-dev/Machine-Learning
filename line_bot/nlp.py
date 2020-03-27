import os
import pathlib

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

class NLP:
    def __init__(self, default_language=None):
        """ Uses Google Cloud NLP libraries to calculate sentiments.
        
        Args:
            default_language (str, optional): default language code for the text. Defaults to None.
        """
        # Sets environmental varable
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = f"{pathlib.Path(__file__).parent.resolve()}/google_cloud_api.json"
        # Instantiates a client
        self.client = language.LanguageServiceClient()
        self.default_language = default_language

    def analyze(self, text, language=None):
        """ Given a text string calculate the sentiment.
        
        Args:
            text (str): text to test the sentiment
            language (str, optional): language code for the text. Defaults to None.
        
        Returns:
            dict: a sentiment dictionary with the score and the magnitude.
        """
        # Checks if language is set. If not, set it with default_language.
        # If default_language is not set either, set language to "en"
        if not language:
            if self.default_language:
                language = self.default_language
            else:
                language = "en"
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT,
            language=language)
        sentiment = self.client.analyze_sentiment(document=document).document_sentiment

        return {"score": sentiment.score, "magnitude": sentiment.magnitude}


if __name__ == "__main__":
    # The text to analyze
    text = "Good luck!"
    nlp = NLP()
    sentiment = nlp.analyze(text)
    print(sentiment["score"], sentiment["magnitude"])