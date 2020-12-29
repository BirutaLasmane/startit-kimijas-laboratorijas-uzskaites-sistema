from flask import Flask, jsonify
import dati

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return "Labrīt!"


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
