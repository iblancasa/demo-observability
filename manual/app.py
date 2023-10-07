from flask import Flask, request
from time import sleep
import random

from opentelemetry.trace import set_tracer_provider
from opentelemetry.instrumentation.wsgi import collect_request_attributes
from opentelemetry.propagate import extract
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

app = Flask(__name__)

resource = Resource(attributes={
    "service.name": "my-app-using-manual-inst"
})
tracer_provider = TracerProvider(resource=resource)
tracer_provider.add_span_processor(
    BatchSpanProcessor(
        OTLPSpanExporter(
            endpoint="http://localhost:4317",
            insecure=True
        )
    )
)

set_tracer_provider(tracer_provider)
tracer = tracer_provider.get_tracer(__name__)

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
