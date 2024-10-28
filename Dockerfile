from python:3.9-slim

workdir /app

copy . /app

run pip install pytest

CMD ["python" "main.py"]