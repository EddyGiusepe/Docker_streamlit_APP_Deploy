FROM python:3.9-slim-buster

# A nossa área de trabalho
WORKDIR /app

# Copia nossos arquivos locais para dentro de nossa área de trabalho
COPY . .

# Instalamos as nossas dependencias
RUN pip install -r requirements.txt

# Para rodar a nossa aplicação
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8080", "server.addres=0.0.0.0"]