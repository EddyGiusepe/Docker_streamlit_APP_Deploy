FROM python:3.9-slim-buster

EXPOSE 8501

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]