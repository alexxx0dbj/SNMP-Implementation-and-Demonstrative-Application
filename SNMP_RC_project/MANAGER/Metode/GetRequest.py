from tkinter import *
import socket
from SNMP_PACKET.snmp_packet import encodeASN1, decodeASN1

agentIp = '127.0.0.1'
conn = bytearray(agentIp, "utf-8")
bufferSize = 1024
def GetRequest():
    window = Tk()
    window.title("Selectați informația dorită")
    window.geometry("1300x200")
    window.configure(bg='#f2f2f2')  # culoare fundal

    button_frame = Frame(window, bg='#f2f2f2')
    button_frame.pack(pady=20)

    # lista comenzi pentru fiecare buton
    button_commands = [
        ("Nume", GetRequestName),
        ("Temperatura", GetRequestTemperatura),
        ("Ram % Usage", GetRequestRamPercent),
        ("Ram Gb Usage", GetRequestRamGB),
        ("Cpu Usage", GetRequestCpuUsage)
    ]

    for i, (text, command) in enumerate(button_commands):
        button = Button(button_frame, text=text, command=command, width=20, height=2, bg='#4CAF50', fg='white', font=('Helvetica', 12))
        button.grid(row=0, column=i, padx=7, pady=7)

    # butonul "Înapoi"
    back_frame = Frame(window, bg='#f2f2f2')
    back_frame.pack(pady=20)

    backButton = Button(back_frame, text="Înapoi", command=window.destroy, width=15, bg='#FF5733', fg='white')  # Stil buton
    backButton.grid(row=0, column=0, pady=5)

    window.mainloop()

def GetRequestCpuUsage():
    encoded_message = encodeASN1(oid="1.5", text="Null", val=0)

    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    UDPclient.sendto(encoded_message, (conn, 161))

    data = UDPclient.recvfrom(bufferSize)[0]
    decoded = decodeASN1(data)
    text = decoded[2]
    print("CPU usage:", text)

def GetRequestRamPercent():
    encoded_message = encodeASN1(oid="1.3", text="Null", val=0)

    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    UDPclient.sendto(encoded_message, (conn, 161))

    data = UDPclient.recvfrom(bufferSize)[0]
    decoded = decodeASN1(data)
    text = decoded[2]
    print("RAM (%) : ", text)

def GetRequestRamGB():
    encoded_message = encodeASN1(oid="1.4", text="Null", val=0)

    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    UDPclient.sendto(encoded_message, (conn, 161))

    data = UDPclient.recvfrom(bufferSize)[0]
    decoded = decodeASN1(data)
    text = decoded[2]
    print("RAM (GB) :", text)
def GetRequestName():
    encoded_message = encodeASN1(oid="1.2", text="Null", val=0)

    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    UDPclient.sendto(encoded_message, (conn, 161))

    data = UDPclient.recvfrom(bufferSize)[0]
    decoded = decodeASN1(data)
    text = decoded[1]
    print("Numele agentului este: ", text)

def GetRequestTemperatura():
    encoded_message = encodeASN1(oid="1.1", text="Null", val=0)

    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    UDPclient.sendto(encoded_message, (conn, 161))
    data = UDPclient.recvfrom(bufferSize)[0]
    decoded = decodeASN1(data)
    text = decoded[2]
    print("Am primit temperatura de: ", text)
