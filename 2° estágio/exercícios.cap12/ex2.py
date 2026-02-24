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

    total = 0
    mostrado = 0

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        
        total += len(data)

        if mostrado < 3000:
            restante = 3000 - mostrado
            print(data[:restante].decode(), end="")
            mostrado += len(data[:restante])

    mysock.close()

    print("\n\nTotal de caracteres recebidos:", total)

except:
    print("Erro ao acessar a URL.")