import tkinter as tk
import subprocess

def ping_ip():
    ip = entry.get()  # Obtém o IP inserido pelo usuário

    if var.get() == 1:
        command = ['ping', '-n', '4', ip]  # Comando para realizar o ping usando ICMP no Windows
    elif var.get() == 2:
        command = ['ping', '-n', '4', '-p', '80', ip]  # Comando para realizar o ping usando TCP (porta 80) no Windows

    output = subprocess.run(command, capture_output=True, text=True)

    result_text.delete(1.0, tk.END)  # Limpa o texto anterior
    result_text.insert(tk.END, output.stdout)  # Exibe o resultado do ping

# Criação da janela principal
window = tk.Tk()
window.title("Ping")
window.geometry("300x250")

# Criação dos componentes da interface
label = tk.Label(window, text="Insira o endereço IP:")
label.pack()

entry = tk.Entry(window)
entry.pack()

var = tk.IntVar()

icmp_button = tk.Radiobutton(window, text="Ping ICMP", variable=var, value=1)
icmp_button.pack()

tcp_button = tk.Radiobutton(window, text="Ping TCP (Porta 80)", variable=var, value=2)
tcp_button.pack()

button = tk.Button(window, text="Ping", command=ping_ip)
button.pack()

result_text = tk.Text(window)
result_text.pack()

# Inicia o loop principal da interface
window.mainloop()
