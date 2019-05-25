FROM python:3.7.3-stretch

RUN apt-get update &&\
    apt-get install -y cmake &&\
    rm -rf /var/lib/apt/lists/*

WORKDIR /src

# Generating wheels based on Pipfile (Pipfile -> requirements.txt -> wheels)
COPY Pipfile Pipfile.lock ./
RUN pip install --disable-pip-version-check --no-cache-dir pipenv && \
    pipenv lock -r > requirements.txt && pip install -r requirements.txt

COPY dprojx .
COPY run_server.sh .
RUN chmod +x run_server.sh

ARG PORT
EXPOSE $PORT
ENV PORT=$PORT

CMD ["./run_server.sh"]