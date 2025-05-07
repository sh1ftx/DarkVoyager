# -*- coding: utf-8 -*-
import time
import os
import subprocess
import shutil
import requests
from stem import Signal
from stem.control import Controller

# Verificar e instalar requests, caso necessário
try:
    import requests
except ImportError:
    print('[+] python3 requests is not installed')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[✓] requests installed.')

# Verificar e instalar Tor, caso necessário
if not shutil.which('tor'):
    print('[+] tor is not installed!')
    try:
        import distro
    except ImportError:
        os.system('pip3 install distro')
        import distro

    distro_id = distro.id()
    if 'arch' in distro_id:
        os.system('sudo pacman -S --noconfirm tor')
    elif 'debian' in distro_id or 'ubuntu' in distro_id:
        os.system('sudo apt update && sudo apt install -y tor')
    else:
        print('[!] Distro não suportada automaticamente. Instale o Tor manualmente.')
    print('[✓] tor is installed successfully.')

os.system("clear")

# Função para pegar o IP atual via Tor
def ma_ip():
    url = 'http://checkip.amazonaws.com'
    get_ip = requests.get(url, proxies=dict(http='socks5://127.0.0.1:9050', https='socks5://127.0.0.1:9050'))
    return get_ip.text.strip()

# Função para mudar o IP
def change():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()  # Isso usa a autenticação do cookie ou senha configurada no torrc
        controller.signal(Signal.NEWNYM)  # Envia o sinal para Tor trocar o IP
    print('[+] Your IP has been Changed to: ' + ma_ip())

print('''\033[1;32;40m
```
_____             _  __      __                               
|  __ \           | | \ \    / /                               
| |  | | __ _ _ __| | _\ \  / /__  _   _  __ _  __ _  ___ _ __ 
| |  | |/ _` | '__| |/ /\ \/ / _ \| | | |/ _` |/ _` |/ _ \ '__|
| |__| | (_| | |  |   <  \  / (_) | |_| | (_| | (_| |  __/ |   
|_____/ \__,_|_|  |_|\_\  \/ \___/ \__, |\__,_|\__, |\___|_|   
                                    __/ |       __/ |          
                                   |___/       |___/           ```
from mr.Sh1ft
''')

print("\033[1;40;31m Sh1ft is a legend!")

# Iniciar o Tor com systemctl
os.system("systemctl start tor")

time.sleep(3)
print("\033[1;32;40m Change your SOCKS proxy to 127.0.0.1:9050 \n")

x = input("[+] Time between IP changes in seconds [default=60] >> ") or "60"
lin = input("[+] How many times to change your IP? [enter for infinite] >> ") or "0"

try:
    lin = int(lin)
    delay = int(x)

    if lin == 0:
        print("Starting infinite IP change. Press Ctrl+C to stop.")
        while True:
            try:
                time.sleep(delay)
                change()
            except KeyboardInterrupt:
                print('\n[!] Auto IP changer stopped.')
                break
    else:
        for _ in range(lin):
            time.sleep(delay)
            change()

except ValueError:
    print("Invalid input. Please enter a valid number.")
