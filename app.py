from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

animals = [
    {"id": 1, "name": "Octopus"},
    {"id": 2, "name": "Fox"}
]


@app.route("/")
def home():
    return {"message": "Favorite Animals API is running"}


@app.route("/animals", methods=["GET"])
def get_animals():
    return animals


@app.route("/animals", methods=["POST"])
def add_animal():
    data = request.get_json()

    new_animal = {
        "id": len(animals) + 1,
        "name": data["name"]
    }

    animals.append(new_animal)

    return new_animal, 201


if __name__ == "__main__":
    app.run(debug=True)