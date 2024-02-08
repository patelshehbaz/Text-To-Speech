from text_to_speech.exception import TTSException
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from text_to_speech.components.get_accent import get_accent_tld, get_accent_message
import sys
from text_to_speech.components.textTospeech import TTSapplication

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    try: 
        accent_list = get_accent_message()
        return render_template('index.html', accent_list=accent_list)
    except Exception as e:
        raise TTSException(e, sys)

@app.route("/predict", methods=['POST', 'GET'])
@cross_origin()
def predict():
    try:
        if request.method == 'POST':
            data = request.json['data']
            accent_input = request.json['accent']
            accent = get_accent_tld(accent_input)
            print(accent)
            result = TTSapplication().text2speech(data, accent)
            return {"data": result.decode("utf-8")}
    except Exception as e:
        raise TTSException(e, sys)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001, debug=False)