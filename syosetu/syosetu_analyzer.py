from syosetu import singlepage_byline_analyzer
from syosetu import singlepage_whole_analyzer
from syosetu import multipage_byline_analyzer
from syosetu import multipage_whole_analyzer

class SyosetuAnalyzer():
    def __init__(self,
                 analyzer_code="sl",
                 url:str="",
                 urls:list=None,
                 language:str="ja",
                 delay:float=10.0):
        """ initializes a sentiment analyzer for a webpage or some webpages
        
        Args:
            analyzer_code (str, optional): Choose an analyzer with an Analyzer Code. Defaults to "sl".
            url (str, optional): url of the webpage for the analysis. Defaults to "".
            urls (list, optional): urls of the webpages for the analysis. Defaults to None.
            language (str, optional): language of the webpage. Defaults to "ja".
            delay (float, optional): delay of the nlp to avoid quota exceeding the Google Cloud limit. Defaults to 10.0.

            Valid Analyzer Codes ->
            sl -> SinglePageByLineAnalyzer(url:str, language:str="ja")
            sw -> SinglePageWholeAnalyzer(url:str, language:str="ja")
            ml -> MultiPageByLineAnalyzer(urls:list, language:str="ja", delay:float=10.0)
            mw -> MultiPageWholeAnalyzer(urls:list, language:str="ja", delay:float=10.0)
        """
        if analyzer_code == "sl":
            self.analyzer = singlepage_byline_analyzer.SinglePageByLineAnalyzer(url, language=language)
        elif analyzer_code == "sw":
            self.analyzer = singlepage_whole_analyzer.SinglePageWholeAnalyzer(url, language=language)
        elif analyzer_code == "ml":
            self.analyzer = multipage_byline_analyzer.MultiPageByLineAnalyzer(urls, language=language, delay=delay)
        elif analyzer_code == "mw":
            self.analyzer = multipage_whole_analyzer.MultiPageWholeAnalyzer(urls, language=language, delay=delay)
        else:
            raise ValueError("Invalid Analyzer Code")
    
    def plot_sentiment_flow(self):
        self.analyzer.plot_sentiment_flow()
    
    def get_sentiments(self):
        return self.analyzer.get_sentiments()