# Agente Mano DEV

Sistema completo de assistente de inteligência artificial versátil, com backend em Python (FastAPI), frontend em React, integração com modelos GPT-Neo, suporte a múltiplos modelos, autenticação, automação, análise de dados e interface em português.

## Estrutura do Projeto

- `backend/`: Código do backend com APIs RESTful, autenticação, integração com IA.
- `frontend/`: Interface web em React com Tailwind CSS.
- `docs/`: Documentação do projeto.
- `ferramentas/`: Scripts para instalação, configuração e inicialização.
- `Dockerfile`: Containerização do backend.
- `build_and_run.sh`: Script para construir e rodar o container Docker.
- `menu_teste.sh`: Script interativo para testar a API.

## Tecnologias

- Python 3.9+
- FastAPI
- React
- Tailwind CSS
- MongoDB
- Redis
- PyTorch
- Transformers (GPT-Neo)
- Docker

## Funcionalidades

- Chat com IA usando GPT-Neo
- Gerenciamento de usuários com autenticação JWT
- Configuração e gerenciamento de múltiplos modelos de IA
- Automação inteligente e análise de dados
- Interface administrativa para configuração e monitoramento
- Segurança robusta e logs detalhados
- Suporte a instalação local de modelos com terminal interativo

## Como usar

1. Execute o script de instalação:
   ```bash
   bash ferramentas/scripts/instalacao.sh
   ```

2. Configure o ambiente:
   ```bash
   bash ferramentas/scripts/configuracao.sh
   ```

3. Inicie o sistema:
   ```bash
   bash ferramentas/scripts/inicializacao.sh
   ```

4. Acesse a interface web:
   ```
   http://localhost:3000
   ```

5. Configure modelos e use o chat IA.

## Contato

Desenvolvido por Mano DEV IA - 2025
