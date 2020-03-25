from bs4 import BeautifulSoup

from syosetu import nlp, singlepage_analyzer, senti_gen_mixin

class SinglePageByLineAnalyzer(singlepage_analyzer.SinglePageAnalyzer, 
                               senti_gen_mixin.SentiGenMixin):
    def __init__(self, url:str, language:str="ja"):
        """ initializes a sentiment analyzer for a webpage
        
        Args:
            url (str): url of the webpage for the analysis.
            language (str, optional): language of the webpage. Defaults to "ja".
        """
        super().__init__(url=url, language=language)
    
    
    def _SinglePageAnalyzer__generate_sentiments(self, url:str, headers:dict, language:str="ja"):
        self._PageAnalyzer__generate_sentiments(url=url, headers=headers, language=language)
    
    
    def _PageAnalyzer__generate_sentiments(self, url:str, headers:dict, language:str="ja"):
        self.generate_sentiments_byline(url=url, headers=headers, language=language)


if __name__ == "__main__":
    analyzer = SinglePageByLineAnalyzer("https://ncode.syosetu.com/n6316bn/2/", "ja")
    analyzer.plot_sentiment_flow()