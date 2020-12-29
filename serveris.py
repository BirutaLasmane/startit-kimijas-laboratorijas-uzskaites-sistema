from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Labrīt!"
    
@app.route('/sveiki')
def sveiki():
  return "Nav vairs nekāds rīts!"

@app.route('/sveiki/<vards>')
def sveikiPersona(vards):
  return f"Sveiki {vards}"

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
