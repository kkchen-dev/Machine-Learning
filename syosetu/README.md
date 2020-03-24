# Sentiment Flow

This is a small project that plots the sentiment flow in a page on the popular Japanese online novel website, [小説家になろう](http://syosetu.com/), using Google Cloud Natural Language.

## Getting Started

Set up your [Google Cloud Natural Language API](https://cloud.google.com/natural-language/docs/quickstart-client-libraries).

You may want to use a virtual environment for your Python code.

Create a headers.json dictionary file to include headers for your webpages.

### Prerequisites

Requires the following libraries.

```
    pip install --upgrade requests
    pip install --upgrade google-cloud-language
    pip install --upgrade bs4
    pip install --upgrade matplotlib

```

## Built With

* [Python 3.8.1](https://www.python.org/downloads/release/python-381/)

## Demo

The program will show the sentiment flow for a selected url.

```
    import page_analyzer

    panalyzer = page_analyzer.PageAnalyzer("https://ncode.syosetu.com/n6316bn/2/", "ja")
    panalyzer.plot_sentiment_flow()
```

When initializing the PageAnalyzer object, you can try a url with the language it's in (available language codes are listed in [Language Support](https://cloud.google.com/natural-language/docs/languages)).

Test URL: https://ncode.syosetu.com/n6316bn/2/

![Sentiment Flow Plot](https://i.imgur.com/GqKW5dk.png)

## Authors

* **[Kevin Chen](https://github.com/kkchen-dev)**

## License

## Acknowledgments

* [Billie Thompson](https://gist.github.com/PurpleBooth) provides [the template]((https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)) for this document.
