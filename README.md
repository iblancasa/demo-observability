# demo-observability

## Tools

1. `docker` or `podman`
2. `python` (tested with `3.11.5`)

## Start the infrastructure
```sh
# Start the OpenTelemetry Collector and the Jaeger instance
cd infrastructure && ./start.sh
```

Access Jaeger from your brownser: `http://localhost:16686/`

### Install the dependencies

```sh
# Install the packages needed to run the demos
pip install -r requirements.txt
```

## Run the demos
### Automatic instrumentation
```sh
cd automatic
opentelemetry-instrument \
    --service_name my-app-using-automatic-inst \
    --traces_exporter otlp \
    --metrics_exporter otlp \
    --exporter_otlp_endpoint 0.0.0.0:4317 \
    --exporter_otlp_insecure=true \
    flask run
```
### Manual instrumentation
```sh
cd manual
flask run
```
### Both instrumentations
```sh
cd both
opentelemetry-instrument \
    --service_name my-app-using-both-inst \
    --traces_exporter otlp \
    --metrics_exporter otlp \
    --exporter_otlp_endpoint 0.0.0.0:4317 \
    --exporter_otlp_insecure=true \
    flask run
```
