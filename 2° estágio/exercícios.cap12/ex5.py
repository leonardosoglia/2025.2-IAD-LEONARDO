import socket

url = input("Digite a URL: ")

try:
    if url.startswith("http://"):
        url = url.replace("http://", "")
    
    host = url.split("/")[0]

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))

    cmd = f"GET / HTTP/1.0\r\nHost: {host}\r\n\r\n"
    mysock.send(cmd.encode())

    resposta = b""

    while True:
        data = mysock.recv(512)
        if not data:
            break
        resposta += data

    mysock.close()

    resposta = resposta.decode()

    partes = resposta.split("\r\n\r\n")

    if len(partes) > 1:
        print(partes[1])

except:
    print("Erro ao acessar a URL.")