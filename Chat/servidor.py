from omniORB import CORBA
import Chat__POA

class ChatServer(Chat__POA.ChatServer):
	def __init__(self):
		self.messages = []
	def sendMessage(self, username, message):
		formatted_message = f"{username}: {message}"
		self.messages.append(formatted_message)
		texto = (f"{formatted_message} (Mensagem salva) \n")
		arquivo = open("Conversas.txt", "a")
		arquivo.write(texto)
		print(f"Message received: {formatted_message}")
		return "Message sent successfully."
	def receiveMessage(self):
		if not self.messages:
			return "No messages available."
		return self.messages
orb = CORBA.ORB_init([], CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")
poaManager = poa._get_the_POAManager()
poaManager.activate()
chatServant = ChatServer()
chatObject = chatServant._this()
print("Chat Server running...")
print("Object reference:", orb.object_to_string(chatObject))
orb.run()

