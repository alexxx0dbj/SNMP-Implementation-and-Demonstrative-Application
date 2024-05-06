import psutil
import wmi
import time
from tkinter import messagebox


class MIB():
    Name = "Agent"
    Temperature= "Celsius"
    getData = True

    def get_temperatura(self, temperature_unit='Celsius'):
        try:
            # informații despre temperatură pentru procesor
            temperature_info = psutil.sensors_temperatures()

            cpu_temperature = next((temp.current for temp in temperature_info.get('coretemp', []) if 'CPU' in temp.label), None)
            return cpu_temperature
            if cpu_temperature is not None:
                if temperature_unit.lower() == 'fahrenheit':
                    cpu_temperature = (cpu_temperature * 9/5) + 32

                return cpu_temperature
            else:
                return "Nu s-au găsit informații ."
        except Exception as e:
            return f"O eroare a apărut: {str(e)}"


    def changeTemperature(NewTemperature):
        Temperature = NewTemperature

    def changeName(NewName):
        Name = NewName

    def getRamPercent(self):
        ramPercent = psutil.virtual_memory()[2]
        ramPercent = str(ramPercent)
        return ramPercent

    def getRamGB(self):
        ramGB = psutil.virtual_memory()[3]/1000000000
        ramGB = str(ramGB)
        return ramGB

    def getCPUPercent(self):
        cpuPercent = psutil.cpu_percent(4)
        cpuPercent = str(cpuPercent)
        return cpuPercent

    def checkTrap(self):
        while 1:
            ramPercent = psutil.virtual_memory()[2]

            print(ramPercent)
            if ramPercent > 50:
                messagebox.showerror('TRAP', 'Ram% mai mare decat 50%')
                break

            cpuPercent = psutil.cpu_percent(4)

            print(cpuPercent)
            if cpuPercent > 60:
                messagebox.showerror('TRAP', 'Cpu% mai mare decat 60%')
                break

            print("")

            time.sleep(5)
