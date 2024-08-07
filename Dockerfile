FROM python:3.11-slim

RUN apt update -y

RUN wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz

RUN tar xvzf ./ngrok-v3-stable-linux-amd64.tgz -C /usr/local/bin

RUN ngrok config add-authtoken 2ddsF2Xa8B6PEpM71YbxvUuRMee_7sb45voWaSjNEBzCfH5to

RUN ngrok http http://localhost:8501

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
