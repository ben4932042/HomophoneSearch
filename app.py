from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
from HomophoneSearch.Chinese.transfer import ChineseTransfer
from HomophoneSearch.English.transfer import EnglishTransfer

app = Flask(__name__)


@app.route('/HomophoneSearch')
def homephone():
    word = request.args.get('word')
    language = request.args.get('language')
    if language == 'chinese':
        return_list = ChineseTransfer.text_to_text(str(word))
    elif language == 'english':
        return_list = EnglishTransfer.text_to_text(str(word))
    else:
        abort(404)
    return jsonify({'language': language, 'text': return_list})

if __name__ == "__main__":
    app.run()
