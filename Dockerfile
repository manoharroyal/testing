FROM python:2.7.14-slim

LABEL author="Terradata"
LABEL usage="Functional and Integration Test Cases"

# creating dedicated image
COPY requirements.txt .

RUN apt-get update \
    && apt-get install -y git \
                            build-essential \
    && pip install -r requirements.txt
