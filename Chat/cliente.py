from omniORB import CORBA
from Chat import ChatServer

orb = CORBA.ORB_init()
ior = input("Enter IOR: ")


if message.lower() == 'exit':
	break

obj = orb.string_to_object(ior)
server = obj._narrow(ChatServer)

# Adicione lógica para interagir com o chat

while True:
	x = input(print("selecione (1) para enviar uma msg.\n"
					"Selecione (2) ara sair."
					))

	if x==1:
		username = input("Enter your username: ")
		message = input("Digite uma mensagem: ")

	elif x==2:
		break

	response = server.sendMessage(username, message)
	received_message = server.receiveMessage()
