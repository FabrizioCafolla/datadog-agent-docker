import logging
from ddtrace import tracer
import json_log_formatter

formatter = json_log_formatter.JSONFormatter()

json_handler = logging.FileHandler(filename='/var/log/app/example.log')
json_handler.setFormatter(formatter)

logger = logging.getLogger('app')
logger.addHandler(json_handler)
logger.setLevel(logging.INFO)


def main():
    span = tracer.current_span()

    correlation_ids = {"span_id": span.trace_id, "trace_id": span.trace_id} if span else {"span_id": "", "trace_id": ""}

    logger.info("Hello world!", extra={'dd': correlation_ids})

main()