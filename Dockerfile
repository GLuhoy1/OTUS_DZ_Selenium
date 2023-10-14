FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN apk add --no-cache chromium chromium-chromedriver

RUN pip install -U pip
RUN pip install -r requirements.txt

ENV PYTHONPATH=/app

# Добавьте переменные окружения для Chrome и Firefox
ENV PATH="/usr/lib/chromium-browser:/usr/lib/firefox-esr:${PATH}"
ENV CHROME_BIN="/usr/lib/chromium/chrome"
ENV DISPLAY=:99


COPY . .

ENTRYPOINT ["pytest"]

