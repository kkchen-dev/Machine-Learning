import json
import base64
import hashlib
import hmac

import requests

import nlp

def authenticate(request, channel_secret):
    """Validates the incoming HTTP requests.
    
    Args:
        request (flask.Request): HTTP request object.
        channel_secret (str): channel secret got from LINE developer console.
    
    Returns:
        bool: true when input body authenticated
    """
    body_list, keep_spaces, met_final_spaces = [], False, False

    body = request.data
    hash = hmac.new(channel_secret.encode('utf-8'), 
                    body, 
                    hashlib.sha256).digest()
    
    # Compare X-Line-Signature request header and the signature
    return (
        "x-line-signature" in request.headers
    ) and (
        request.headers["x-line-signature"] == base64.b64encode(hash).decode('utf-8')
    )

def get_trigger_word_max_length(text: str, trigger_words: list):
    """Given a input text string and a list of trigger words, 
       returns the length of the longest trigger word found in text.
    
    Args:
        text (str): the input text.
        trigger_words (list): the trigger word to match.
    
    Returns:
        int: the length of the longest trigger word found in text.
    """
    trigger_words_set = set(trigger_words)
    text_lower = text.lower()
    trigger_word_max_length = -1
    for trigger_word in trigger_words:
        if text_lower[:len(trigger_word)] in trigger_words_set:
            trigger_word_max_length = max(trigger_word_max_length, len(trigger_word))
    return trigger_word_max_length

def main(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    channel_id, channel_secret = "", ""
    with open("credential.json", "r") as f:
        credential = json.load(f)
        channel_id = credential["client_id"]
        channel_secret = credential["api_key"]
    
    print("Authenticating...")
    if not authenticate(request, channel_secret):
        return ""
    print("Authenticated")

    # checks the input text
    # the input text must start with trigger words
    trigger_words = None
    with open("trigger_words.json") as f:
        trigger_words = json.load(f)
    request_json = request.get_json()
    text = ""
    try:
        text = request_json["events"][0]["message"]["text"]
        print(text)
    except:
        print("Not the target message.")
    
    # checks the longest trigger word
    trigger_word_max_length = get_trigger_word_max_length(text, trigger_words)
    if trigger_word_max_length == -1:
        return "OK"

    # removes symbols between the trigger word and the main string
    start = trigger_word_max_length
    symbol_set = {",","."," ",":","~"}
    while start < len(text) and text[start] in symbol_set:
        start += 1
    if start < len(text):
        text = text[start:]
    else:
        return "OK"
    print(text)

    _nlp = nlp.NLP()
    # _nlp = nlp.NLP("zh-Hant")
    sentiment = _nlp.analyze(text)
    print(sentiment)

    api_url_dict = {}
    with open("api_url_dict.json") as f:
        api_url_dict = json.load(f)
    # gets the access token
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    params = {
        "grant_type": "client_credentials", 
        "client_id": channel_id, 
        "client_secret": channel_secret
    }
    response = requests.post(
        api_url_dict["oauth_access_token"], 
        headers=headers, 
        params=params
    )
    access_token = json.loads(response.content)["access_token"]
    
    # formets the sentiment analysis
    headers = {
        "Content-Type": "application/json", 
        "Authorization": f"Bearer {access_token}"
    }
    score = sentiment["score"] * 10
    magnitude = sentiment["magnitude"]
    data = {
        "replyToken": request_json["events"][0]["replyToken"],
        "messages":[
            {
                "type": "text",
                "text": f"Positiveness(-10.00 ~ 10.00): {score:.2f}"
            },
            {
                "type": "text",
                "text": f"Emotion(>0.00): {magnitude:.2f}"
            }
        ]
    }
    # sends the sentiment analysis results with LINE Messaging API reply.
    response = requests.post(
        api_url_dict["message_reply"], 
        headers=headers, 
        data=json.dumps(data)
    )
    print(response.content)
    
    return "OK"