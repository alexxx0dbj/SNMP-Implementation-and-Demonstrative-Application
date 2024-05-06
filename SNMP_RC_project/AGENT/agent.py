import threading
from Metode.GetResponse import GetResponse
from Metode.SetResponse import SetResponse
from Metode.Trap import *

localIP = '127.0.0.1'
localport = 161
bufferSize = 1024

UDPAgent = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPAgent.bind((localIP, localport))

# deschiderea unui alt fir de execuție pentru a verifica trapurile în mod continuu
threading.Thread(target=checkTrap).start()

try:
    while True:
        data = UDPAgent.recvfrom(bufferSize)
        oid = decodeASN1(data[0])
        print("OID este: ", oid[0])

        address = data[1]
        text = oid[1]

        if oid[0][0] == 1:
            GetResponse(oid, address, UDPAgent)
        elif oid[0][0] == 2:
            SetResponse(oid, address, UDPAgent, text)
        else:
            UDPAgent.sendto(bytes("Invalid", "utf-8"), address)
except KeyboardInterrupt:
    print("Agentul a fost oprit manual.")
finally:
    UDPAgent.close()
