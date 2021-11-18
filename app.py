from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hola, Mundo!</h1>"


@app.route("/login")
def login():
    print("Entrando al proceso de login")
    return "<h1>La super página</h1>"


if __name__ == "__main__":
    app.run(debug=True)