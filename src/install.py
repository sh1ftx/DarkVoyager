import os
import shutil

def get_distro():
    try:
        import distro
    except ImportError:
        os.system('pip3 install distro')
        import distro
    return distro.id()

choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system

if choice.lower() == 'y':
    run('chmod 777 autoTOR.py')
    run('mkdir -p /usr/share/aut')
    run('cp autoTOR.py /usr/share/aut/autoTOR.py')

    cmnd = ('#! /bin/sh\nexec python3 /usr/share/aut/autoTOR.py "$@"')
    with open('/usr/bin/aut', 'w') as file:
        file.write(cmnd)

    run('chmod +x /usr/bin/aut')
    run('chmod +x /usr/share/aut/autoTOR.py')

    # Verifica e instala Tor conforme a distro
    if not shutil.which('tor'):
        distro_id = get_distro()
        print("[!] Tor not found. Installing...")
        if 'arch' in distro_id:
            run('sudo pacman -S --noconfirm tor')
        elif 'debian' in distro_id or 'ubuntu' in distro_id:
            run('sudo apt update && sudo apt install -y tor')
        else:
            print("[!] Distro não suportada automaticamente. Instale o Tor manualmente.")

    print('\n[✓] Auto Tor IP Changer installed successfully!\nNow just type \x1b[6;30;42maut\x1b[0m in terminal.')
elif choice.lower() == 'n':
    run('rm -rf /usr/share/aut')
    run('rm -f /usr/bin/aut')
    print('[!] Auto Tor IP Changer has been removed successfully.')
