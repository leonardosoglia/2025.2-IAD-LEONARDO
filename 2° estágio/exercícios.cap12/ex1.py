import socket

url = input("Digite a URL (ex: http://example.com): ")

try:
    if url.startswith("http://"):
        url = url.replace("http://", "")
    
    host = url.split("/")[0]

    print("Host:", host)

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))

    cmd = f"GET / HTTP/1.0\r\nHost: {host}\r\n\r\n"
    mysock.send(cmd.encode())

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end="")

    mysock.close()
except:
    print("URL inválida ou site inexistente.")