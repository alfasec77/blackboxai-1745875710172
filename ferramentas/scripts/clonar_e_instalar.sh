#!/bin/bash
echo "Iniciando clonagem e instalação das ferramentas..."

# Função para clonar repositório se não existir
clonar_repositorio() {
  local url=$1
  local pasta=$2
  if [ ! -d "$pasta" ]; then
    echo "Clonando $url em $pasta..."
    git clone "$url" "$pasta"
  else
    echo "Diretório $pasta já existe. Pulando clonagem."
  fi
}

# Clonar Docling
clonar_repositorio "https://github.com/docling/docling.git" "ferramentas/docling"

# Clonar OpenManus
clonar_repositorio "https://github.com/openmanus/openmanus.git" "ferramentas/openmanus"

# Instalar dependências Python para Docling
echo "Instalando dependências do Docling..."
cd ferramentas/docling || exit 1
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
cd ../../

# Instalar dependências Python para OpenManus
echo "Instalando dependências do OpenManus..."
cd ferramentas/openmanus || exit 1
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
cd ../../

echo "Clonagem e instalação concluídas."
