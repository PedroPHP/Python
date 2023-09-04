import tkinter as tk
import customtkinter as ctk
import subprocess

import dns.resolver
import getpass
import telnetlib
import telnetlib3
#https://giacomo-quinalia.medium.com/telnet-com-python-em-olts-eb5641324148
# Função para realizar a conexão Telnet
# async def telnet_connect(ip):
#     host = ip
#     port = 23

#     try:
#         telnet=telnetlib.Telnet(host,port,timeout=5)
#     except Exception:
#         print("erro ao realizar a conexão")

#     user = b'admin \n'
#     password = b'admin\n' 
 
#     telnet.read_until(b'name:')
#     telnet.write(user)
 
#     telnet.read_until(b'password:')
#     telnet.write(password)



    # user = input("Enter your remote account: ")
    # password = getpass.getpass()

    # tn = telnetlib.Telnet(HOST)

    # tn.read_until(b"login: ")
    # tn.write(user.encode('ascii') + b"\n")
    # if password:
    #     tn.read_until(b"Password: ")
    #     tn.write(password.encode('ascii') + b"\n")

    # tn.write(b"ls\n")
    # tn.write(b"exit\n")
#     try:
#         tn = telnetlib.Telnet(ip)
#         tn.read_until(b"login: ")
#         tn.write(b"admin\n")  # Insira o nome de usuário
#         tn.read_until(b"Password: ")
#         tn.write(b"admin\n")  # Insira a senha
#         # Agora você está conectado e pode interagir com o prompt do Telnet
#         # Por exemplo, você pode enviar comandos e ler as respostas

#         # Para desconectar:
#         tn.write(b"exit\n")
#         tn.read_all()  # Lê todas as saídas pendentes

#     except Exception as e:
#         print("Erro:", e)


def start():
    ip = entry.get()  # Obtém o IP inserido pelo usuário
   

    if var.get() == 1:
        command = ['ping', '-n', '4', ip]  # Comando para realizar o ping usando ICMP no Windows
    elif var.get() == 2:
        command = ['ping', '-n', '4', '-p', '80', ip]  # Comando para realizar o ping usando TCP (porta 80) no Windows
    elif var.get() == 3:
        command = ['nmap', ip] #Comando para realizar o nmap usando o ip inserido
    # elif var.get() == 4:
        # try:
        #     telnet_connect(ip)  # Chama a função de conexão Telnet
        # except Exception as e:
        #     print("Erro na conexão Telnet:", e)
        # return  # Retorna após a conexão Telnet
    elif var.get() == 5:
        #Defina o domínio de destino e o tipo de registro
        target_domain = ip
        record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]
        resolver = dns.resolver.Resolver()
        output = ""
        for record_type in record_types:
            try:
                answers = resolver.resolve(target_domain, record_type)
                output += f"{record_type} records for {target_domain}:\n"
                for rdata in answers:
                    output += f" {rdata}\n"
            except dns.resolver.NoAnswer:
                continue
        result_text.delete(1.0, ctk.END)  # Limpa o texto anterior
        result_text.insert(ctk.END, output)
        return  # Retorna após a enumeração DNS
    output = subprocess.run(command, capture_output=True, text=True)

    result_text.delete(1.0, ctk.END)  # Limpa o texto anterior
    result_text.insert(ctk.END, output.stdout)  # Exibe o resultado do ping



# Criação da janela principal
window = ctk.CTk()
window.title("Ping")
window.geometry("300x450")

# Criação dos componentes da interface
label = ctk.CTkLabel(window, text="Insira o endereço IP:")
label.pack()

entry = ctk.CTkEntry(window)
entry.pack()

var = ctk.IntVar()

icmp_button = ctk.CTkRadioButton(window, text="Ping ICMP", variable=var, value=1)
icmp_button.pack()

tcp_button = ctk.CTkRadioButton(window, text="Ping TCP (Porta 80)", variable=var, value=2)
tcp_button.pack()

nmap_button = ctk.CTkRadioButton(window, text="Nmap (escanear as portas)", variable=var, value=3)
nmap_button.pack()

prov_button = ctk.CTkRadioButton(window, text="Telnet", variable=var, value=4)
prov_button.pack()

enum_button = ctk.CTkRadioButton(window, text="Enumerando DNS", variable=var, value=5)
enum_button.pack()


button = ctk.CTkButton(window, text="Start", command=start)
button.pack()

result_text = ctk.CTkTextbox(window,height=500, width=580)
result_text.pack()


# Inicia o loop principal da interface
window.mainloop()
