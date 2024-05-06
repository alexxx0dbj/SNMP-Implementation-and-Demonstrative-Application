from tkinter import *
from MANAGER.Metode.GetRequest import GetRequest
from MANAGER.Metode.SetRequest import SetRequest
from MANAGER.Metode.ReceiveTrap import ReceiveTrap
import threading

def startWindow():
    window = Tk()
    window.title("SNMP Interface")
    window.geometry("500x200")
    window.configure(bg='#f2f2f2')  # Schimbați culoarea de fundal la alegere

    # Create a frame for better organization
    main_frame = Frame(window, bg='#f2f2f2')  # Culoare fundal frame
    main_frame.pack(padx=20, pady=20)

    title_label = Label(main_frame, text="SNMP Interface", font=('Helvetica', 16), bg='#f2f2f2')  # Culoare fundal label
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    # Get Request Button
    getRequestButton = Button(main_frame, text="Get Request", command=GetRequest, width=20, bg='#4CAF50', fg='white')  # Culoare fundal și text
    getRequestButton.grid(row=1, column=0, padx=20, pady=20)

    # Set Request Button
    setRequestButton = Button(main_frame, text="Set Request", command=SetRequest, width=20, bg='#2196F3', fg='white')  # Culoare fundal și text
    setRequestButton.grid(row=1, column=1, padx=10, pady=10)

    threading.Thread(target=ReceiveTrap).start()

    window.mainloop()
