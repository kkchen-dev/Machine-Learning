from abc import ABC, abstractmethod


class PageAnalyzer(ABC):
    @abstractmethod
    def _generate_sentiments(self, url, headers, language="ja"):
        pass


    @abstractmethod
    def save_sentiments(self, filename="sentiment_data.txt"):
        pass