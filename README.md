```
_____             _  __      __                               
|  __ \           | | \ \    / /                               
| |  | | __ _ _ __| | _\ \  / /__  _   _  __ _  __ _  ___ _ __ 
| |  | |/ _` | '__| |/ /\ \/ / _ \| | | |/ _` |/ _` |/ _ \ '__|
| |__| | (_| | |  |   <  \  / (_) | |_| | (_| | (_| |  __/ |   
|_____/ \__,_|_|  |_|\_\  \/ \___/ \__, |\__,_|\__, |\___|_|   
                                    __/ |       __/ |          
                                   |___/       |___/           
  ```

-- 

Script automático para troca de IP via Tor com configuração assistida, autodetecção de sistema e verificação de dependências.

![bash](https://img.shields.io/badge/script-bash-blue?logo=gnu-bash)
![status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![python](https://img.shields.io/badge/python-3.11%2B-blue.svg)
![tor](https://img.shields.io/badge/tor-integrado-7e4798?logo=tor-project)

---

## 📜 Descrição

Automatize a configuração do ambiente para rotação de IP usando a rede Tor. Ideal para usuários preocupados com **anonimato**, **privacidade** ou que queiram entender como scripts automatizados interagem com serviços de rede.

---

## Funcionalidades

- Detecção automática da distribuição Linux
- Verificação e instalação do Python
- Configuração inteligente do Tor (`torrc`)
- Agendamento de troca de IP (em construção)
- Tudo via script bash, pronto para rodar

---

## 📂 Estrutura

```bash
DarkVoyager/
├── Configs/                  # Ambiente virtual Python
├── src/
│   ├── config.sh          # Script principal de setup
│   ├── install.py         # Dependências Python (separadas)
│   └── main.py            # Lógica principal de rotação
├── requirements.txt
└── README.md
```

## Como usar?

1. Clone o repositório

```
git clone https://github.com/sh1ftx/DarkVoyager.git
cd DarkVoyager
```

2. Torne o script executável

```
chmod +x config.sh
```
3. Execute o script de configuração

```
./config.sh
```
### O script irá:

    + Detectar sua distro
    + Instalar o Python (se necessário)
    + Configurar o ambiente virtual
    + Validar se o Tor está instalado

## 📌 Requisitos

    + Linux (Debian, Ubuntu, Arch ou derivados)
    + Tor instalado ou permissão para instalar
    + bash 5+

🤝 Contribua

Pull requests são muito bem-vindos! Sinta-se livre para abrir issues, sugerir melhorias ou reportar bugs. # DarkVoyager
