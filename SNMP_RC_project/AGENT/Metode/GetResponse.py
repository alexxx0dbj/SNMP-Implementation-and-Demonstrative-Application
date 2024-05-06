from AGENT.mib import MIB
from SNMP_PACKET.snmp_packet import encodeASN1

def GetResponse(OID,address, UDPAgent):
    while 1:
        if not OID: break
        print(OID)
        if (OID[0][1] == 1):
            print(MIB.get_temperatura(MIB.getData, MIB.Temperature))
            encoded_message = encodeASN1(oid="1.1", text="Null", val=MIB.get_temperatura(MIB.getData, MIB.Temperature))
            UDPAgent.sendto(encoded_message, address)
            break
        elif (OID[0][1] == 2):
            encoded_message = encodeASN1(oid="1.2", text=MIB.Name, val=0)
            UDPAgent.sendto(encoded_message, address)
            break
        elif (OID[0][1] == 3):
            encoded_message = encodeASN1(oid="1.3", text="Null", val=MIB.getRamPercent(MIB.getData))
            UDPAgent.sendto(encoded_message, address)
            break
        elif (OID[0][1] == 4):
            encoded_message = encodeASN1(oid="1.4", text="Null", val=MIB.getRamGB(MIB.getData))
            UDPAgent.sendto(encoded_message, address)
            break
        elif (OID[0][1] == 5):
            encoded_message = encodeASN1(oid="1.5", text= "Null", val=MIB.getCPUPercent(MIB.getData))
            UDPAgent.sendto(encoded_message, address)
            break
        else:
            UDPAgent.sendto(bytes("Invalid", "utf-8"), address)
            break