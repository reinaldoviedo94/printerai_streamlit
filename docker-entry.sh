#!/bin/bash
set -e

echo "Ejecutando pruebas unitarias..."

pytest

echo "Iniciando la aplicación..."

exec "$@"
