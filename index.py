libs = "time aiohttp tkinter webbrowser time socket pyfiglet colorama"
import webbrowser as wb
import os
import pyfiglet
import tkinter.ttk
from colorama import Fore, Back, Style, init
init(autoreset=True)
from tkinter import *
from time import sleep
print(Fore.LIGHTMAGENTA_EX + Back.WHITE + "Needed libs: " + libs)
os.system("pyfiglet JupitDoS")
print("Maple/TLTteam (c) 2017-2021")
#- +configure
root = Tk()
root.iconbitmap('C:\\jupitdosicon.ico')
root.geometry('975x375')
root.configure(background='#cc33cc')
root.title('JupitDoS')
root.overrideredirect(1)
#-configure +defs
def support():
    wb.open_new_tab("https://discord.gg/98SF68ueNF")
#-defs +gui
btn1 = Button(text="JupitDoS Support", bg="#474747", foreground="#ccc", height = 1, width = 1, padx="187", pady="6", font="16", command=support)
c = Label(text="Maple/TLTteam (c) 2017-2021", font="Impact", bg="#cc33cc")

btn1.place(x=550,y=60)
c.place(x=0,y=351)
root.mainloop()
#-gui
