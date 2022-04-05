import json
import managers
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/chars/<int:char_encoding>", methods=["GET"])
def get_character(char_encoding: int):
    """Returns the encoded utf-8 character

    char_encoding: A number representing a character in utf-8 encoding system
    """
    if request.method == "GET":
        db = managers.DBManager("utf8.db")
        try:
            character = db.query_character(char_encoding)
        except KeyError:
            response = make_response("")
            response.status = 404
            return response
        else:
            character = json.dumps(character)
            response = make_response(character)
            response.content_type = "application/json"
            return response


@app.route("/codes/<string:char>", methods=["GET"])
def get_encoding(char: str):
    """Returns the encoding of a utf-8 character

    char: A utf-8 encoded character
    """
    if request.method == "GET":
        db = managers.DBManager("utf8.db")
        try:
            encoding = db.query_encoding(char)
        except KeyError:
            response = make_response("")
            response.status = 404
            return response
        else:
            encoding = json.dumps(encoding)
            response = make_response(encoding)
            response.content_type = "application/json"
            return response

if __name__ == "__main__":
    app.run()
