import re
import socket

HOST = "127.0.0.1"
PORT = 9093
headers = ['User-Agent', 'Accept', 'Accept-Language', 'Accept-Encoding', 'Accept-Charset', 'Keep-Alive', 'Connection', 'Cookie']

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()
while True:
    data = conn.recv(1024).decode()

    if not data:
        break

    split_data = data.split('\n')
    req = split_data[0].split()
    response = f'Request Method {req[0]}'
    response += f' Request Source {HOST} {PORT}'
    if req[0].lower() == 'get':
        status = re.search(r"status=\d{3}", req[1]).group()
        status = status.replace('status=', '')
        response += f' Response Status: {status}'

    # удаляю первый элемнет массива, так как его уже распарсили и он не нужен
    split_data.pop(0)

    for i in range(len(split_data)):
        for k in range(len(headers)):
            if headers[k] in split_data[i]:
                response += split_data[i]

    print(response)
    conn.send(response.encode())

conn.close()
