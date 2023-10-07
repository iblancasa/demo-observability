from flask import Flask, request
from time import sleep
import random

app = Flask(__name__)

@app.route("/")
def hello():
    sleep(random.randint(0, 7))
    return "hello\n"

if __name__ == "__main__":
    app.run()
