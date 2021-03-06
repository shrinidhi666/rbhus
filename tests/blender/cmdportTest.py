import bpy
import asyncore
import socket
import threading

class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        data = self.recv(8192)
        if data:
          print(data)
          eval(data)

class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print('Incoming connection from '+ repr(addr))
            handler = EchoHandler(sock)

def startCmdPort():
  server = EchoServer('localhost', 8999)
  asyncore.loop()


a = threading.Thread(target=startCmdPort)
a.start()
# server = EchoServer('localhost', 8999)