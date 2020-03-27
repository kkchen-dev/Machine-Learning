import json
import pathlib
from abc import abstractmethod

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

from syosetu import nlp, page_analyzer

class SinglePageAnalyzer(page_analyzer.PageAnalyzer):
    def __init__(self, url:str, language:str="ja"):
        """ initializes a sentiment analyzer for a webpage
        
        Args:
            url (str): url of the webpage for the analysis.
            language (str, optional): language of the webpage. Defaults to "ja".
        """
        # loads headers dictionary
        headers = {}
        with open(f"{pathlib.Path(__file__).parent.resolve()}/headers.json", "r") as f:
            headers = json.load(f)
        
        self.soup, self.soup_contents, self.sentiments = None, [], []
        self.__generate_sentiments(url, headers, language)

    @abstractmethod
    def __generate_sentiments(self, url:str, headers:dict, language:str="ja"):
        pass


    def save_sentiments(self, filename:str="sentiment_data.txt"):
        """ dumps sentiment data into a text file
        
        Args:
            filename (str, optional): text filename. Defaults to "sentiment_data.json".
        """
        with open(f"{pathlib.Path(__file__).parent.resolve()}/{filename}", "w") as f:
            f.write(
                "\n".join([
                    " ".join(
                        [c, str(s["score"]), str(s["magnitude"])]
                    ) for c, s in zip(self.soup_contents, self.sentiments)
                ])
            )
    
    
    def plot_sentiment_flow(self):
        """ plots the sentiment flow of the document
        """
        scores, magnitudes, sentiment_space = [], [], []
        for i, sentiment in enumerate(self.sentiments):
            scores.append(sentiment["score"])
            magnitudes.append(sentiment["magnitude"])
            sentiment_space.append(i+1)

        plt.subplot(2, 1, 1)
        plt.plot(sentiment_space, scores, '-')
        plt.ylabel("Scores")
        
        plt.subplot(2, 1, 2)
        plt.plot(sentiment_space, magnitudes, '-')
        plt.xlabel("Sentence No.")
        plt.ylabel("Magnitudes")

        plt.show()


    def get_sentiments(self):
        return self.sentiments