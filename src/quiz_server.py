from flask import Flask, request
from flask_cors import CORS

from src.quiz_repository import *


app = Flask(__name__)
CORS(app)


@app.route("/")
def juego_quiz():
    return "juego quiz"

@app.route("/preguntas",  methods=["GET"])
def all_preguntas():
    return read_all()

@app.route("/preguntas/<id_pregunta>", methods=["GET"])
def preguntas(id_pregunta):
    return read(id_pregunta)

@app.route("/preguntas", methods=["POST"])
def new_preguntas():
     data = request.get_json()
     create(data)
     return ""
 
@app.route("/preguntas/<id_pregunta>", methods=["DELETE"])
def delete_pregunta(id_pregunta):
      remove_pregunta(id_pregunta) 
      return ""
  
@app.route("/preguntas/<id_pregunta>", methods=["PUT"])
def update_pregunta(id_pregunta):
    data = request.get_json()
    update_pregunta_data(id_pregunta, data)
    return ""


if __name__ == "__main__":
    app.run(debug=True)