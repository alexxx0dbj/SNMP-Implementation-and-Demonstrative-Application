import time
import socket
from SNMP_PACKET.snmp_packet import encodeASN1, decodeASN1


import psutil

def checkTrap():
    agentIp = '127.0.0.1'
    conn = bytearray(agentIp, "utf-8")
    okRam=0
    okCPU=0

    UDPagent = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    while 1:
        ramPercent = psutil.virtual_memory()[2]

        # print(ramPercent)
        if ramPercent > 50 and okRam==0:
            encoded_message = encodeASN1(oid="0.0", text="RAM", val=ramPercent)
            UDPagent.sendto(encoded_message, (conn, 162))
            okRam = 1

        cpuPercent = psutil.cpu_percent(4)

        # print(cpuPercent)
        if cpuPercent > 50 and okCPU==0:
            encoded_message = encodeASN1(oid="1.0", text="CPU", val=cpuPercent)
            UDPagent.sendto(encoded_message, (conn, 162))
            okCPU = 1

        time.sleep(5)