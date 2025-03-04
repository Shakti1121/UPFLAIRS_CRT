
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_add = "192.168.108.172"
port = 12345
complete = (ip_add,port)
message = input("what is your message")
encode_msg = message.encode('ascii')
s.sendto(encode_msg,complete)
