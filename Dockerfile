FROM python:alpine3.15
LABEL maintainer="rzmobiledev@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./app /app
COPY ./requirements.txt /tmp/requirements.txt
COPY ./scripts /scripts

WORKDIR /app
EXPOSE 8000

RUN python -m venv /env && \
    /env/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    /env/bin/pip install -r /tmp/requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home rz && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R rz:rz /vol && \
    chown -R 755 /vol && \
    chmod -R +x /scripts


ENV PATH="/scripts:/env/bin:${PATH}"
USER rz

CMD [ "/run.sh" ]


