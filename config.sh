#!/bin/bash

# Detecta a distribuição do sistema operacional
echo "Detectando a distribuição do sistema operacional..."
if [ -f /etc/os-release ]; then
    . /etc/os-release
    DISTRO=$NAME
    VERSION=$VERSION_ID
else
    echo "Não foi possível detectar a distribuição."
    exit 1
fi

echo "Distribuição detectada: $DISTRO $VERSION"

# Verifica se o Python está instalado
echo "Verificando instalação do Python..."
if ! command -v python3 &>/dev/null; then
    echo "Python3 não encontrado. Instalando..."
    if [[ "$DISTRO" == "Ubuntu" || "$DISTRO" == "Debian" ]]; then
        sudo apt update && sudo apt install -y python3 python3-pip python3-venv
    elif [[ "$DISTRO" == "Arch Linux" ]]; then
        sudo pacman -Syu --noconfirm python python-pip python-virtualenv
    else
        echo "Distribuição não suportada automaticamente para instalação do Python."
        exit 1
    fi
else
    echo "Python3 já está instalado."
fi

# Cria e ativa o ambiente virtual
echo "Criando e ativando o ambiente virtual..."
python3 -m venv Configs
source Configs/bin/activate
echo "Ambiente virtual ativado."

# Instala as dependências
echo "Instalando dependências do projeto..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Dependências instaladas com sucesso."

# Mudando para o diretório src
echo "Mudando para o diretório src..."
cd src || { echo "Diretório src não encontrado."; exit 1; }

# Executa o install.py
echo "Executando install.py..."
python3 install.py

# Executa o main.py
echo "Executando main.py..."
python3 main.py

# Finaliza
echo "Instalação e execução concluídas com sucesso!"
echo "Agora, aproveite seu projeto! Lembre-se de seguir boas práticas de segurança na internet."
