from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return 'Welcome to the copier management backend'

#@app.route("/api")
#def api():


if __name__ == "__main__":
    app.run(port = 5001)
