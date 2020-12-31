from pprint import pprint
import requests
from flask import Flask, request
app = Flask(__name__)

groupme_api_path = "https://api.groupme.com/v3/bots/post"

@app.route('/test', methods=['POST'])
def hello_world():
    if request.json["sender_type"] == "bot":
        return 'Yer a bot!' 
    # print(vars(request))
    text = request.json["text"]
    sender_name = request.json["name"]
    bot_text = f"hi! {sender_name}"
    if not text.startswith("@dongus"):
        return "ya goofed"
    if text.startswith("@dongus yo"):
        bot_text = "Fuck off "
    requests.post(groupme_api_path,json={"bot_id": bot_id, "text": bot_text})
    return 'Hello, World!'



@app.route('/real', methods=['POST'])
def hello_world_real():
    if request.json["sender_type"] == "bot":
        return 'Yer a bot!' 
    # print(vars(request))
    text = request.json["text"]
    sender_name = request.json["name"]
    bot_text = f"hi! {sender_name}"
    if not text.startswith("@dongus"):
        return "ya goofed"
    if text.startswith("@dongus yo"):
        bot_text = "Fuck off "
    requests.post(groupme_api_path,json={"bot_id": bot_id_real, "text": bot_text})
    return 'Hello, World!'
