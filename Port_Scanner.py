import socket
import subprocess
import sys 

from datetime import datetime

subprocess.call('clear', shell=True)

remoteServerIP = input('Entrez l\'IP  d\'un serveur à scanner : ')

print ('-' * 60)
print (' Lancement du scan des ports de votre machine ' + remoteServerIP)
print ('-' * 60)


t1 = datetime.now()

try:
    for port in range (1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print('Port {}:   Ouvert'.format(port))
        sock.close()


except KeyboardInterrupt:
    print('Vous avez appuyé sur Ctrl+c pour interrompre le programme.')
    sys.exit()

except socket.error: 
    print('Impossible de se connecter au serveur')
    sys.exit()


t2 = datetime.now()

total = t2 -t1
print('Scan complété en : {} '.format(str(total)))