from tkinter import *
from time import strftime

myWindow = Tk()
myWindow.title("MyClock")
x = 0
def time():
    
    myTime = strftime('%H:%M:%S%p')
    clock.config(text=myTime)

    while x < 100:
        myTime = strftime('%H:%M:%S%p')
    

clock = Label(myWindow,font = ('arial',40,'bold'),background="dark red",foreground="yellow")

clock.pack(anchor='center')

time()

mainloop()