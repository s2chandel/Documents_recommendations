# libs
from io import StringIO
import json
import flask
from flask import Flask, request
import time
from flask import jsonify
import numpy as np

from QuesRecSystem import recommendations


recs = recommendations()


def __init__(self, text):

    self.text = text


# Model Inference
def recommendations(json):
    """
    calls similar_questions function in the
    recommendations class
    """
    sim_ques_ids = recs.similar_questions(json['text'])
    return sim_ques_ids


app = Flask(__name__)


@app.route('/ping', methods=['GET'])
@app.route('/', methods=['POST'])
def sentiment_analysis():

    if flask.request.content_type == 'application/json':
        input_json = flask.request.get_json()
        print("Input json")
        print(input_json)
    else:
        return flask.Response(response='Content type should be application/json', status=415, mimetype='application/json')

    # Get the response
    response = recommendations(input_json)

    out = StringIO()
    json.dump(response, out)
    return flask.Response(response=out.getvalue(), status=200, mimetype='application/json')


if __name__ == '__main__':

    app.run(port=8000)
