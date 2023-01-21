import uuid
from flask import Flask, render_template, request
from joblib import load
from utils import utils

app = Flask(__name__)


@app.route('/hello', methods=['GET', 'POST'])
def hello_world():
    """_summary_

    Returns:
        _type_: _description_
    """
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href='static/base_pic.svg')
    else:
        text = request.form['text']
        random_string = uuid.uuid4().hex
        path = "app/static/" + random_string + ".svg"
        model = load('app/models/model.joblib')
        np_arr = utils.floats_string_to_np_arr(text)
        utils.make_picture('app/models/AgesAndHeights.pkl', model, np_arr, path)

        return render_template('index.html', href=path[4:])
