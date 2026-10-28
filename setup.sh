#!/bin/bash
# Script de configuração do ambiente para o Tutorial de Prompt Engineering da Anthropic
# Versão com Ollama (modelo local, sem API key, sem custos)

echo "==> Instalando dependências Python..."
pip install -r requirements.txt

echo ""
echo "==> Verificando Ollama..."
if ! command -v ollama &>/dev/null; then
    echo "    Ollama não encontrado. Instalando..."
    curl -fsSL https://ollama.com/install.sh | sh
else
    echo "    Ollama já instalado: $(ollama --version)"
fi

echo ""
echo "==> Iniciando servidor Ollama em background..."
ollama serve &>/tmp/ollama.log &
sleep 3

echo ""
echo "==> Baixando modelo phi3:mini (~2.2GB, só na primeira vez)..."
ollama pull phi3:mini

echo ""
echo "==> Ambiente pronto!"
echo ""
echo "==> Para iniciar o Jupyter Notebook:"
echo "    jupyter notebook"
echo ""
echo "==> Comece pelo notebook: 'Tradução PT-BR/00_Tutorial_Como_Usar.ipynb'"
echo "    (nenhuma API key necessária!)"
