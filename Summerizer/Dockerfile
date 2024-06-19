
FROM python:3.10

WORKDIR /app

COPY Summary/ /app/

RUN pip install --no-cache-dir -r requirements.txt

ENV UVICORN_CMD="uvicorn app:app --host 0.0.0.0 --port 8000"

CMD ["python", "app.py"]


