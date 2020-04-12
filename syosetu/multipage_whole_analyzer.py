from bs4 import BeautifulSoup

from syosetu import nlp, multipage_analyzer, senti_gen_mixin

class MultiPageWholeAnalyzer(multipage_analyzer.MultiPageAnalyzer, 
                             senti_gen_mixin.SentiGenMixin):
    def __init__(self, urls:list, language:str="ja", delay:float=10.0):
        """ initializes a sentiment analyzer for some webpages
        
        Args:
            urls (list): urls of the webpages for the analysis.
            language (str, optional): language of the webpage. Defaults to "ja".
            delay (float, optional): delay of the nlp to avoid quota exceeding the Google Cloud limit. Defaults to 10.0.
        """
        super().__init__(urls=urls, language=language, delay=delay)
    
    
    def _generate_sentiments(self, url:str, headers:dict, language:str="ja"):
        self.generate_sentiments_whole(url=url, headers=headers, language=language)