# PrinterAI Streamlit Project

Este es un proyecto de Streamlit que incluye integración con FlowiseAI, pruebas unitarias, y se despliega utilizando Docker y `docker-compose`.

## Estructura del Proyecto

```
./
├── Dockerfile
├── __pycache__
├── app.py
├── docker-compose.yaml
├── docker-entry.sh
├── external_systems
│   ├── __init__.py
│   └── flowiseai.py
├── ngrok.yml
├── requirements.txt
├── session_id
├── settings.py
├── tests
│   ├── test_flowiseai.py
│   ├── test_manage_chat_history_use_case.py
│   └── test_manage_session_id_use_case.py
└── use_cases
    ├── manage_chat_history_use_case.py
    └── manage_session_id_use_case.py
```

### Descripción de Archivos y Directorios

- **`app.py`**: Archivo principal de la aplicación Streamlit.
- **`Dockerfile`**: Define la imagen de Docker para el proyecto.
- **`docker-compose.yaml`**: Archivo para orquestar contenedores Docker.
- **`docker-entry.sh`**: Script de entrada para Docker.
- **`external_systems/`**: Contiene la integración con sistemas externos.
  - `flowiseai.py`: Interacción con un sistema externo llamado FlowiseAI.
- **`ngrok.yml`**: Configuración para Ngrok (si se usa).
- **`requirements.txt`**: Archivo que contiene las dependencias del proyecto.
- **`session_id`**: Fichero para gestionar las sesiones(si al menos se corre el proyecto una vez).
- **`settings.py`**: Archivo de configuración de la aplicación.
- **`tests/`**: Directorio de pruebas unitarias.
  - `test_flowiseai.py`, `test_manage_chat_history_use_case.py`, `test_manage_session_id_use_case.py`: Pruebas unitarias de las funcionalidades principales.
- **`use_cases/`**: Implementación de casos de uso de la aplicación.
  - `manage_chat_history_use_case.py`, `manage_session_id_use_case.py`: Casos de uso específicos del proyecto.

## Requisitos Previos

- Python 3.11+
- Docker y Docker Compose
- Ngrok (opcional, si se usa)

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://gitlab.com/reinaldoviedo94/printerai_streamlit.git
   
   cd printerai_streamlit
   ```

2. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Configurar variables de entorno en `settings.py`.

## Uso

Para iniciar la aplicación Streamlit localmente:

```bash
streamlit run app.py
```

Para iniciar la aplicación utilizando Docker:

```bash
docker-compose up --build
```

## Pruebas

Para ejecutar las pruebas unitarias:

```bash
pytest tests/
```

## Despliegue

Este proyecto está configurado para ser desplegado utilizando Docker. Se puede usar un servicio de alojamiento de contenedores como AWS, Google Cloud, o Heroku para desplegar la aplicación.

## Contribuciones

Las contribuciones son bienvenidas. 
