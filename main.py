from pprint import pprint
import requests
import numpy as np
import giphy_client as gc
from giphy_client.rest import ApiException
from numpy import random
from variables import basic_response_list
from variables import dingus_hi
from variables import roast_list
from random import randint
from flask import Flask, request
app = Flask(__name__)

groupme_api_path = "https://api.groupme.com/v3/bots/post"



api_instance = gc.DefaultApi()

query = 'art'
fmt = 'gif'

#Stuff for markov chains
trump = open('trump_speeches.txt', encoding='utf8').read()
corpus = trump.split()
def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])
        
pairs = make_pairs(corpus)

word_dict = {}

for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

math = open('math.txt', encoding='utf8').read()
corpus_math = math.split()

pairs_math = make_pairs(corpus_math)

word_dict_math = {}

for word_1, word_2 in pairs_math:
    if word_1 in word_dict_math.keys():
        word_dict_math[word_1].append(word_2)
    else:
        word_dict_math[word_1] = [word_2]
dickens = open('dickens.txt', encoding='utf8').read()
corpus_dickens = dickens.split()

pairs_dickens = make_pairs(corpus_dickens)

word_dict_dickens= {}

for word_1, word_2 in pairs_dickens:
    if word_1 in word_dict_dickens.keys():
        word_dict_dickens[word_1].append(word_2)
    else:
        word_dict_dickens[word_1] = [word_2]

@app.route('/test', methods=['POST'])
def hello_world():
    # print(vars(request))
    
    text = request.json["text"]
    phrase = text[7:]
    roastee = text[14:]
    sender_name = request.json["name"]
    bot_text = random.choice(basic_response_list).format(sender_name,phrase)

    if not text.startswith("@dongus"):
        return "ya goofed"
    if text.startswith("@dongus yo"):
        bot_text = "Fuck off "
    if text.startswith("@dongus roast" or "@dongus Roast" or "@dongus ROAST"):
        bot_text = random.choice(roast_list).format(roastee)
    if random.rand() < .14:
        bot_text = "@dingus " + random.choice(dingus_hi)
    if text.startswith("@dongus ##"):
        response = api_instance.gifs_search_get(api_key,text[10:],limit=1,offset=randint(1,10),fmt=fmt)
        gif_id = response.data[0]     
        gif_url = gif_id.images.downsized.url
        gif_url = gif_url.split("?")[0]
        requests.post(groupme_api_path,json={"bot_id": bot_id, "picture_url": gif_url})
        return "You bet your API"
    if random.rand() < .5:
        first_word = np.random.choice(corpus)

        while first_word.islower():
            first_word = np.random.choice(corpus)

        chain = [first_word]

        n_words = 25

        for i in range(n_words):
            chain.append(np.random.choice(word_dict[chain[-1]]))

        trump_response = ' '.join(chain)
        first_word_math = np.random.choice(corpus_math)

        while first_word_math.islower():
            first_word_math = np.random.choice(corpus_math)

        chain_math = [first_word_math]

        n_words = 15

        for i in range(n_words):
            chain_math.append(np.random.choice(word_dict_math[chain_math[-1]]))

        math_response = ' '.join(chain_math)    

        first_word_dickens = np.random.choice(corpus_dickens)

        while first_word_dickens.islower():
            first_word_dickens = np.random.choice(corpus_dickens)

        chain_dickens = [first_word_dickens]

        n_words = 30

        for i in range(n_words):
            chain_dickens.append(np.random.choice(word_dict_dickens[chain_dickens[-1]]))

        dickens_response = ' '.join(chain_dickens)  
        bot_text = np.random.choice([trump_response, math_response, dickens_response])
    requests.post(groupme_api_path,json={"bot_id": bot_id, "text": bot_text})
    return 'Hello, World!'



@app.route('/real', methods=['POST'])
def hello_world_real():
    # print(vars(request))
    
    text = request.json["text"]
    phrase = text[7:]
    roastee = text[14:]
    sender_name = request.json["name"]
    bot_text = random.choice(basic_response_list).format(sender_name,phrase)

    if not text.startswith("@dongus"):
        return "ya goofed"
    if text.startswith("@dongus yo"):
        bot_text = "Fuck off "
    if text.startswith("@dongus roast" or "@dongus Roast" or "@dongus ROAST"):
        bot_text = random.choice(roast_list).format(roastee)
    if random.rand() < .14:
        bot_text = "@dingus " + random.choice(dingus_hi)
        return "dingus"
    if text.startswith("@dongus ##"):
        response = api_instance.gifs_search_get(api_key,text[10:],limit=1,offset=randint(1,10),fmt=fmt)
        gif_id = response.data[0]     
        gif_url = gif_id.images.downsized.url
        requests.post(groupme_api_path,json={"bot_id": bot_id_real, "picture_url": gif_url})
        return "You bet your API"
    if random.rand() < .7:
        first_word = np.random.choice(corpus)

        while first_word.islower():
            first_word = np.random.choice(corpus)

        chain = [first_word]

        n_words = 25

        for i in range(n_words):
            chain.append(np.random.choice(word_dict[chain[-1]]))

        trump_response = ' '.join(chain)
        first_word_math = np.random.choice(corpus_math)

        while first_word_math.islower():
            first_word_math = np.random.choice(corpus_math)

        chain_math = [first_word_math]

        n_words = 15

        for i in range(n_words):
            chain_math.append(np.random.choice(word_dict_math[chain_math[-1]]))

        math_response = ' '.join(chain_math)    

        first_word_dickens = np.random.choice(corpus_dickens)

        while first_word_dickens.islower():
            first_word_dickens = np.random.choice(corpus_dickens)

        chain_dickens = [first_word_dickens]

        n_words = 30

        for i in range(n_words):
            chain_dickens.append(np.random.choice(word_dict_dickens[chain_dickens[-1]]))

        dickens_response = ' '.join(chain_dickens)  
        bot_text = np.random.choice([trump_response, math_response, dickens_response])
    requests.post(groupme_api_path,json={"bot_id": bot_id_real, "text": bot_text})
    return 'Hello, World!'
