import json
import pathlib

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

import nlp

class PageAnalyzer:
    def __init__(self, url, language="en"):
        """ initializes a sentiment analyzer for a webpage
        
        Args:
            url ([type]): [description]
            language (str, optional): [description]. Defaults to "en".
        """
        # loads headers dictionary
        headers = {}
        with open(f"{pathlib.Path(__file__).parent.resolve()}/headers.json", "r") as f:
            headers = json.load(f)
        
        _nlp = nlp.NLP(language)
        # checks if the url response is 200(OK) and assign requests.get(url) to req_url
        self.soup = None
        self.soup_contents = []
        self.sentiments = []
        if (req_url := requests.get(url, headers=headers)).status_code == 200:
            self.soup = BeautifulSoup(req_url.content, 'html.parser')
            # analyzes each sentence
            for child in self.soup.find(id="novel_honbun").contents:
                if child.string and child.string != "\n":
                    self.soup_contents.append(child)
                    self.sentiments.append(_nlp.analyze(child.string))
    
    def plot_sentiment_flow(self):
        """ plots the sentiment flow of the document
        """
        scores, magnitudes, sentiment_space = [], [], []
        for i, sentiment in enumerate(self.sentiments):
            scores.append(sentiment["score"])
            magnitudes.append(sentiment["magnitude"])
            sentiment_space.append(i+1)

        plt.subplot(2, 1, 1)
        plt.plot(sentiment_space, scores, 'o-')
        plt.ylabel("Scores")
        
        plt.subplot(2, 1, 2)
        plt.plot(sentiment_space, magnitudes, 'o-')
        plt.xlabel("Sentence No.")
        plt.ylabel("Magnitudes")

        plt.show()
    


if __name__ == "__main__":
    page_analyzer = PageAnalyzer("https://ncode.syosetu.com/n6316bn/2/", "ja")
    page_analyzer.plot_sentiment_flow()