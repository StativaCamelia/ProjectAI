from flask import request, jsonify, make_response
from google.cloud import language_v1
from googletrans import Translator
from flask_cors import CORS, cross_origin
import os
import flask
import requests
import re
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.abspath("ProiectTw-12bf250f4662.json")


operators_sim = dict()
translator = Translator()


def sample_analyze_entities(text_content):
    client = language_v1.LanguageServiceClient()
    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}
    response = client.analyze_entities(request={'document': document})
    return response.entities


def sample_analyze_syntax(text_content):
    client = language_v1.LanguageServiceClient()
    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}
    encoding_type = language_v1.EncodingType.UTF8
    response = client.analyze_syntax(request={'document': document, 'encoding_type': encoding_type})
    return response


def get_similarities_for_word(word):
    url = 'https://api.datamuse.com/words?ml=' + word
    response = requests.get(url)
    similarities_list = response.json()
    return [item['word'] for item in similarities_list]


def get_similarities_for_operators():
    operators_list = ['define', 'filetype', 'site', 'related', 'weather', 'stocks', 'map', 'movie', 'location']
    for operator in operators_list:
        operators_sim[operator] = get_similarities_for_word(operator)


def get_similarity_for_word(word):
    word = word.replace(' ', '')
    if word in operators_sim.keys():
        return word
    for operator in operators_sim.keys():
        if word in operators_sim[operator]:
            return operator
    return None


app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)
get_similarities_for_operators()


@app.route('/', methods=['POST'])
def create_task():
    text_ro = request.json["text"]
    translation = translator.translate(text_ro, dest='en')
    text_en_all = translation.text
    text_en_all = re.split(r'(\sand\s|\sor\s)', text_en_all)
    print(text_en_all)
    query_all = ""
    for text_en in text_en_all:
        if text_en.lower() == ' and ':
            query_all += ' AND '
            continue
        if text_en.lower() == ' or ':
            query_all += ' OR '
            continue
        response_entities = sample_analyze_entities(text_en)
        query = ''
        entities_types = []
        entity_dict = {
            'operator': '',
            'operator_value': ''
        }
        for entity in response_entities:
            entity_operator_name = get_similarity_for_word(str(entity.name).lower())
            entity_operator_type = get_similarity_for_word(str(entity.type_)[5:].lower())
            if entity_operator_name and entity_dict.get('operator') == '':
                entity_dict['operator'] = entity_operator_name
            else:
                if entity_operator_type and entity_dict.get('operator') == '':
                    entity_dict['operator'] = entity_operator_type
                    # in special pentru location; daca exista o singura entitate, care are tipul location..atunci operatorul este location (gasit in operatori) iar valoarea este entity.name:
                    if len(response_entities) == 1:
                        entity_dict['operator_value'] = entity.name
                else:
                    entity_dict['operator_value'] = entity.name
        entities_types.append(entity_dict)
        for entity_type in entities_types:
            query = entity_type['operator'] + ':' + entity_type['operator_value']
        query_all += query
    response = jsonify({'response': query_all})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/", methods=["OPTIONS"])
def api_create_order():
    return build_cors_prelight_response()

def build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

app.run()
