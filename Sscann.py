import socket
import argparse

def sScann():
	in_host = input("IP: ")
	in_port = int(input("PORT: "))
	in_port_range = int(input("PORT RANGE: "))

	print(stealthScan(in_host, in_port, in_port_range))

def connectionTry(HOST, PORT):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#print ("Socket created successfully") #Debug the socket creation

	try:
		s.connect((HOST,PORT))
		#print("Closing the socket") #Debug the socket close
		s.close()
		#return 1 #returning value
		print("Port " + str(PORT) + " is: Open")

	except socket.error:
		#print("Closing the socket") #Debug the socket close
		s.close()
		#return 0 #returning value
		print("Port " + PORT + " is: Close")

def stealthScan(s_host, s_port, s_port_range):
	if s_port_range == 0:
		return connectionTry(s_host, s_port)
	else:
		for i in range(s_port, s_port_range):
			print(connectionTry(s_host, i))

#def regularscan()

if __name__ == "__main__":
	sScann()