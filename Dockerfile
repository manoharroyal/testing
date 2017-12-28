FROM python:2.7.14-slim

LABEL author="Terradata"
LABEL usage="Functional and Integration Test Cases"

# creating dedicated image

RUN apt-get update \
   && apt-get install -y git \
                           build-essential \
   && pip install requests \
                   pyyaml \
                   enum \
                   pyjwt \
                   pytest==3.2.5 \
                   pytest-html \
                   pytest-instafail
