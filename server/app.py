from flask import Flask, request, jsonify

app = Flask(__name__)

movies = [
    {
        "name": "The Shawshank Redemption",
        "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
        "genres": ["Drama"],
    },
    {
        "name": "The Godfather ",
        "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
        "genres": ["Crime", "Drama"],
    },
]


@app.route("/movies", methods=["GET"])
def getMovies():
    return {"movies": movies}


@app.route("/movies/<int:id>", methods=["GET"])
def getMovie(id):
    movie = request.get_json(id)

    return {"movie": id}


@app.route("/movies/addMovie", methods=["POST"])
def addMovie():
    movie = request.get_json()
    movies.append(movie)

    return {"id": len(movies)}, 200


@app.route("/movies/updateMovie/<int:id>", methods=["PUT"])
def updateMovie(id):
    movie = request.get_json()
    movies[id] = movie

    # return {"id": movies[id]}, 200
    return jsonify(movies[id]), 200


@app.route("/movies/deleteMovie/<int:id>", methods=["DELETE"])
def deleteMovie(id):
    movies.pop(id)
    return "None", 200
