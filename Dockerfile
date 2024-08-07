FROM python:3.11-slim

RUN curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
	| tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
	&& echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
	| tee /etc/apt/sources.list.d/ngrok.list \
	&& apt update \
	&& apt install ngrok

RUN ngrok config add-authtoken 2ddsF2Xa8B6PEpM71YbxvUuRMee_7sb45voWaSjNEBzCfH5to

RUN ngrok http http://localhost:8501

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
