FROM python:3.8.2-alpine
RUN pip install pytest
COPY app /app
WORKDIR /app
CMD pytest -q test.py

