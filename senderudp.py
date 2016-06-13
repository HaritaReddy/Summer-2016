#This is a mutual chat
#This is the Sender side. The sender send the message first.
#THe chat ends when either sender or receiver types "bye"
from socket import*
host="localhost"
portsend=1345
portrec=5567
address1=(host,portsend)
address2=(host,portrec)
buff_size=2048
s=socket(AF_INET,SOCK_DGRAM)
s.bind(address2)
while True:
 msg=raw_input()
 s.sendto(msg,address1)
 if msg=="bye" or msg=="Bye":
  break
 data,addr=s.recvfrom(buff_size)
 print data
 if data=="bye" or data=="Bye":
  break
s.close()

