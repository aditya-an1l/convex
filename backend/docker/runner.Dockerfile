FROM python:3.11-slim

WORKDIR /sandbox

RUN useradd -m sandbox

USER sandbox

ENTRYPOINT ["python3"]
