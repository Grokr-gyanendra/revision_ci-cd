from python:3.9-slim

workdir /app

copy . /app

run pip install pytest flask

CMD ["python" "main.py"]