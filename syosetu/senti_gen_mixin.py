from bs4 import BeautifulSoup
import requests

from syosetu import nlp

class SentiGenMixin:
    def generate_sentiments_base(self, url:str, headers:dict, language:str="en"):
        pass


    def generate_sentiments_byline(self, url:str, headers:dict, language:str="en"):
        """ generates content strings and sentiments
        
        Args:
            url (str): url of the webpage for the analysis.
            headers (dict): headers dictionary.
            language (str, optional): language of the webpage. Defaults to "en".
        """
        _nlp = nlp.NLP(language)
        # checks if the url response is 200(OK) and assign requests.get(url) to req_url
        if (req_url := requests.get(url, headers=headers)).status_code == 200:
            self.soup = BeautifulSoup(req_url.content, 'html.parser')
            # analyzes each sentence
            for child in self.soup.find(id="novel_honbun").contents:
                if child.string and child.string != "\n":
                    self.soup_contents.append(child.string)
                    self.sentiments.append(_nlp.analyze(child.string))


    def generate_sentiments_whole(self, url:str, headers:dict, language:str="en"):
        """ generates content strings and sentiments
        
        Args:
            url (str): url of the webpage for the analysis.
            headers (dict): headers dictionary.
            language (str, optional): language of the webpage. Defaults to "en".
        """
        _nlp = nlp.NLP(language)
        # checks if the url response is 200(OK) and assign requests.get(url) to req_url
        if (req_url := requests.get(url, headers=headers)).status_code == 200:
            self.soup = BeautifulSoup(req_url.content, 'html.parser')
            child_strings = []
            # analyzes each sentence
            for child in self.soup.find(id="novel_honbun").contents:
                if child.string and child.string != "\n":
                    child_strings.append(child.string)
            
            child_string_string = "\n".join(child_strings)
            self.soup_contents.append(child_string_string)
            self.sentiments.append(_nlp.analyze(child_string_string))