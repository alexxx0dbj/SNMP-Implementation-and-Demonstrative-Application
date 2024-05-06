from tkinter import *
import socket

from SNMP_PACKET.snmp_packet import encodeASN1, decodeASN1


def SetRequest():
    window = Tk()
    window.title("Selectați informația dorită")
    window.geometry("500x200")
    window.configure(bg='#f2f2f2')  # Culoare fundal

    # Frame pentru butoanele orizontale
    button_frame = Frame(window, bg='#f2f2f2')
    button_frame.pack(pady=20)

    # Lista de comenzi pentru fiecare buton
    button_commands = [
        ("Nume", setRequestName),
        ("Temperatura", setRequestTemperature),
    ]

    for i, (text, command) in enumerate(button_commands):
        button = Button(button_frame, text=text, command=command, width=20, height=2, bg='#4CAF50', fg='white', font=('Helvetica', 12))  # Stil buton
        button.grid(row=0, column=i, padx=8, pady=8)

    # Frame pentru butonul "Înapoi"
    back_frame = Frame(window, bg='#f2f2f2')
    back_frame.pack(pady=20)

    # Buton Înapoi
    backButton = Button(back_frame, text="Înapoi", command=window.destroy, width=15, bg='#FF5733', fg='white')  # Stil buton
    backButton.grid(row=0, column=0, pady=5)

    window.mainloop()

def introdusNume(inputtxt):
    nume = inputtxt.get("1.0", "end-1c")
    print(nume)
    conn = '127.0.0.1'

    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    encoded_message = encodeASN1(oid="2.1", text=nume, val=0)
    UDPclient.sendto(encoded_message, (conn, 161))

    data = UDPclient.recvfrom(1024)[0]
    text = decodeASN1(data)[1]
    print("Numele a fost schimbat in ", text)

def setRequestName():
    # Window pentru introducerea numelui
    window = Tk()
    window.title("Introduceți numele")
    window.geometry("300x150")
    window.configure(bg='#f2f2f2')  # Culoare fundal

    # Label pentru instrucțiuni
    instructions_label = Label(window, text="Introduceți numele:", bg='#f2f2f2')
    instructions_label.pack(pady=(10, 5))

    # Input pentru nume
    inputtxt = Text(window, height=1, width=20, bg="light yellow")
    inputtxt.pack(pady=5)

    # Buton pentru a seta numele
    set_name_button = Button(window, text="Setează Nume", command=lambda: introdusNume(inputtxt), bg='#4CAF50', fg='white')  # Stil buton
    set_name_button.pack(pady=10)

    window.mainloop()

def setRequestTemperature():
    # window pentru introdus numele
    window = Tk()
    window.title("Temperatura:")
    window.configure(width=100, height=300)

    # Buton Inapoi
    celsiusButton = Button(window, text="Celsius", command=temperatura1)
    celsiusButton.place(x=35, y=50)
    # Buton Inapoi
    farenheitButton = Button(window, text="Farenheit", command=temperatura2)
    farenheitButton.place(x=30, y=100)
    # Buton Inapoi
    kelvinButton = Button(window, text="Kelvin", command=temperatura3)
    kelvinButton.place(x=35, y=150)
    # Buton Inapoi
    backButton = Button(window, text="Inapoi", command=window.destroy)
    backButton.place(x=35, y=250)

def temperatura1():
    conn = '127.0.0.1'
    temp="Celsius"
    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    encoded_message = encodeASN1(oid="2.2", text=temp, val=0)
    UDPclient.sendto(encoded_message, (conn, 161))
    data = UDPclient.recvfrom(1024)[0]
    text = decodeASN1(data)[1]
    print("Temperatura a fost schimbata in ", text)

def temperatura2():
    conn = '127.0.0.1'
    temp="Farenheit"
    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    encoded_message = encodeASN1(oid="2.2", text=temp, val=0)
    UDPclient.sendto(encoded_message, (conn, 161))
    data = UDPclient.recvfrom(1024)[0]
    text = decodeASN1(data)[1]
    print("Temperatura a fost schimbata in ", text)

def temperatura3():
    conn = '127.0.0.1'
    temp="Kelvin"
    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    encoded_message = encodeASN1(oid="2.2", text=temp, val=0)
    UDPclient.sendto(encoded_message, (conn, 161))
    data = UDPclient.recvfrom(1024)[0]
    text = decodeASN1(data)[1]
    print("Temperatura a fost schimbata in ", text)