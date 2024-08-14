FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Copiar el script de entrada
COPY docker-entry.sh /app/docker-entry.sh

# Dar permisos de ejecución al script
RUN chmod +x /app/docker-entry.sh

# Exponer el puerto
EXPOSE 8501

# Usar el script como punto de entrada
ENTRYPOINT ["/app/docker-entry.sh"]

# Comando por defecto que ejecuta Streamlit
CMD ["streamlit", "run", "app.py"]
