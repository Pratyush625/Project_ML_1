FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir --progress-bar off -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app