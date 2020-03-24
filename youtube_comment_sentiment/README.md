# Youtube Comment Analyzer

This is a small project that shows the average sentiment score of the comment section on a Youtube video.

## Getting Started

Set up your [Google Cloud Natural Language API](https://cloud.google.com/natural-language/docs/quickstart-client-libraries).

Get your Google API key.

You may want to use a virtual environment for your Python code.

### Prerequisites

Requires the following libraries.

```
    pip install --upgrade requests
    pip install --upgrade google-cloud-language
```

## Built With

* [Python 3.8.1](https://www.python.org/downloads/release/python-381/)

## Demo

The program will show the average comment sentiment for a selected video.

```
    import yt_comment_analyzer

    ytcanalyzer = yt_comment_analyzer.YTCAnalyzer("QHF8x25FxFM", 50)
    print(ytcanalyzer.get_average_score())
```

## Authors

* **[Kevin Chen](https://github.com/kkchen-dev)**

## License

## Acknowledgments

* [Billie Thompson](https://gist.github.com/PurpleBooth) provides [the template]((https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)) for this document.