FROM gcr.io/datadoghq/agent:7

ARG ENV

ADD datadog.yml /etc/datadog-agent/datadog.yaml
RUN sed -i "s/%ENV%/${ENV}/g" /etc/datadog-agent/datadog.yaml

ADD conf.d/logs.yml /etc/datadog-agent/conf.d/logs.yaml
RUN sed -i "s/%ENV%/${ENV}/g" /etc/datadog-agent/conf.d/logs.yaml