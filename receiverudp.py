#This is a mutual chat. THe receiverudp.py side receives the message first.
from socket import*
host="localhost"
portrec=1345
portsend=5567
address1=(host,portrec)
address2=(host,portsend)
s=socket(AF_INET,SOCK_DGRAM)
buff_size=2048
s.bind(address1)
while True:
 data,addr=s.recvfrom(buff_size)
 print data
 if data=="bye" or data=="Bye":
  break
 msg=raw_input()
 s.sendto(msg,address2)
 if msg=="bye" or msg=="Bye":
  break
s.close()

