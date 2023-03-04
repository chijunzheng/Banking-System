.PHONY: build test dockerize push

build:
    python3 -m venv env
    source env/bin/activate && pip install -r requirements.txt
    python3 setup.py build

test:
    python3 -m pytest

dockerize:
    docker build -t ballerchi/banking-system:1.0 .
    docker tag ballerchi/banking-system:1.0 ballerchi/banking-system:latest

push:
    docker login -u ballerchi -p $(password)
    docker push ballerchi/banking-system:latest

