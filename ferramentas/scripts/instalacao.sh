#!/bin/bash
echo "Iniciando instalação do sistema Agente Mano DEV..."

# Atualizar pacotes
sudo apt update && sudo apt upgrade -y

# Instalar dependências do sistema
sudo apt install -y python3 python3-venv python3-pip nodejs npm redis-server docker.io docker-compose

# Configurar Redis
sudo systemctl enable redis-server
sudo systemctl start redis-server

# Configurar Docker
sudo systemctl enable docker
sudo systemctl start docker

# Criar ambiente virtual Python
python3 -m venv venv
source venv/bin/activate

# Instalar dependências Python
pip install --upgrade pip
pip install fastapi uvicorn celery redis transformers torch requests

# Instalar dependências frontend
cd ../frontend
npm install

echo "Instalação concluída com sucesso."
