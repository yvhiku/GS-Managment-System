# testing server

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "hello, how are you"

if __name__ == "__main__" :
    print("HELLO WORLD")
    app.run(port=5000)