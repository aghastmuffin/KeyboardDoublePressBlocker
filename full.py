import keyboard, time 
import tkinter as tk
from tkinter import * #no installation should be necesary, if it is run pip install keyboard
#this is not set up in a normal module fashion, however it is on pypi, if you would like to set it up, please configure it yourself.
from threading import Thread
def main():
    while True:
        key = keyboard.read_key()
        if len(key) == 1:
            keyboard.block_key(key)
            time.sleep(0.1)
            keyboard.unblock_key(key) 

def secondary():
    root = Tk()
    root.title("Keyboard Test")
    root.geometry("400x400")
    var1 = tk.IntVar()
    c1 = tk.Checkbutton(root, text='Start',variable=var1, onvalue=1, offvalue=0, command=Thread(target=main).start())
    c1.pack()
    root.mainloop()
Thread(target=secondary).start()
