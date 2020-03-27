# Line Sentiment Bot

This is a LINE bot that replies a set of sentiment analysis to a message.

## Getting Started

Setup your [Google Cloud Functions Account](https://console.cloud.google.com/functions).

Setup your [LINE Developers Account](https://developers.line.biz/).

Get your [Google Cloud Natural Language API Key](https://cloud.google.com/docs/authentication/api-keys).

In LINE Developers console, setup a new Messaging API channel.

Find your Channel ID and Channel secret in Basic Settings the channel console, save them to the `credential.json` file in the following form in this folder.

```
{
    "client_id": {Channel ID},
    "api_key": {Channel secret}
}
```

Configure `trigger_wordds.json` to your preference.

Zip the contents in this folder.

```
cd line_bot
zip -r9 ${OLDPWD}/line_bot.zip .
```

Create a Cloud Function.
* Upload the zip file to [Google Cloud Functions](https://console.cloud.google.com/functions/).
* Set `Runtime` to `Python 3.7`.
* Setup a stage bucket for it.
* And then, set the `function to execute` to `main`.

Find the HTML trigger URL in your Google Cloud Function console. Copy it.

In the LINE Developers console, go to the Messaging API setting page and turn on webhook, paste the Google Cloud Function trigger URL into the webhook url and verify it.

Add your bot as a friend via Bot basic ID or the QR code and send an message starting with a trigger word.

### Prerequisites

Requires a [Google Cloud Platform](https://console.cloud.google.com/) account and a [LINE Developers](https://developers.line.biz/) account.

## Built With

* [Python 3.7](https://www.python.org/downloads/)
* [Google Cloud Functions](https://console.cloud.google.com/functions/)
* [LINE Developers API](https://developers.line.biz/en/reference/)

## Demo

This is a LINE bot that will reply the sentiment analysis when triggered with words.

![LINE Bot Chat Log](https://i.imgur.com/xz7Vvg2.png)

## Authors

* **[Kevin Chen](https://github.com/kkchen-dev)**

## License

**[MIT License](../LICENSE)**

## Acknowledgments

* [Billie Thompson](https://gist.github.com/PurpleBooth) provides [the template]((https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)) for this document.