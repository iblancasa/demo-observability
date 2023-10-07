from flask import Flask, request
from time import sleep
from opentelemetry import trace
import random

app = Flask(__name__)
tracer = trace.get_tracer(__name__)

@app.route("/")
def hello():
    with tracer.start_as_current_span(
        "parent-span",
	):
        sleep(random.randint(0, 7))
        with tracer.start_as_current_span(
            "child-span",
		):
            return "hello"

if __name__ == "__main__":
    app.run()
