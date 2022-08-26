FROM python:3.10.5-slim

RUN apt-get update
RUN apt-get -y upgrade

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential libpq-dev \
  && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /opt/venv \
  && /opt/venv/bin/pip install pip --upgrade

ADD requirements.txt /tmp/requirements.txt
RUN /opt/venv/bin/pip install --no-cache-dir -r /tmp/requirements.txt \
  && rm -rf /tmp/requirements.txt \
  && useradd -U app_user \
  && install -d -m 0755 -o app_user -g app_user /app/static

WORKDIR /app
COPY skeleglennsaysSite .
COPY entrypoint.sh entrypoint.sh

RUN chmod +x entrypoint.sh

USER app_user

CMD [ "/app/entrypoint.sh" ]