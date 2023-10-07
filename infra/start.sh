#!/bin/bash
docker run -d --name jaeger \
  -p 4318:4317 \
  -p 16686:16686 \
  jaegertracing/all-in-one

docker run -d  --network=host \
  --rm \
  -p 4317:4317 \
  -v "${PWD}/collector-config.yaml":/collector-config.yaml \
  otel/opentelemetry-collector \
  --config collector-config.yaml

