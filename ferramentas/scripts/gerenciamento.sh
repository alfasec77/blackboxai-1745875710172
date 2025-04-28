#!/bin/bash
echo "Menu de Gerenciamento do Agente Mano DEV"
while true; do
  echo "Escolha uma opção:"
  echo "1) Instalar todas as ferramentas"
  echo "2) Configurar o sistema"
  echo "3) Iniciar o sistema"
  echo "4) Clonar e instalar Docling e OpenManus"
  echo "5) Sair"
  read -p "Opção: " opcao

  case $opcao in
    1)
      echo "Executando script de instalação..."
      bash ferramentas/scripts/instalacao.sh
      ;;
    2)
      echo "Executando script de configuração..."
      bash ferramentas/scripts/configuracao.sh
      ;;
    3)
      echo "Executando script de inicialização..."
      bash ferramentas/scripts/inicializacao.sh
      ;;
    4)
      echo "Executando script de clonagem e instalação das ferramentas..."
      bash ferramentas/scripts/clonar_e_instalar.sh
      ;;
    5)
      echo "Saindo..."
      exit 0
      ;;
    *)
      echo "Opção inválida. Tente novamente."
      ;;
  esac
done
