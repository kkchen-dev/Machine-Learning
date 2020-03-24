import json
import pathlib

import requests

import nlp

class YTCAnalyzer:
    def __init__(self, videoId, maxResults=50):
        """ Given a video id and a max comment count calculate the average sentiment.
        
        Args:
            videoId (str): a youtube video id.
            maxResults (int, optional): max comment count for the analysis. Defaults to 50.
        """
        with open(f"{pathlib.Path(__file__).parent.resolve()}/credential.json", "r") as f:
            api_key = json.load(f)["api_key"]

        url = f"https://www.googleapis.com/youtube/v3/commentThreads?key={api_key}&textFormat=plainText&part=snippet&videoId={videoId}&maxResults={maxResults}"
        # checks if the url response is 200(OK) and assign requests.get(url) to req_url
        if (req_url := requests.get(url)).status_code == 200:
            comment_dict = json.loads(req_url.text)
            _nlp = nlp.NLP()
            total_score = sum(
                _nlp.analyze(item["snippet"]["topLevelComment"]["snippet"]["textOriginal"])["score"]
                for item in comment_dict["items"]
            )
            self.average_score = total_score / len(comment_dict["items"])
    

    def get_average_score(self): return self.average_score

if __name__ == "__main__":
    ytcanalyzer = YTCAnalyzer("QHF8x25FxFM", 50)
    print(ytcanalyzer.get_average_score())