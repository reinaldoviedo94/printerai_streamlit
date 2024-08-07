#!/bin/bash

# Start the first process
python -m streamlit run app.py &

# Start the second process
ngrok http http://localhost:8501 &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?