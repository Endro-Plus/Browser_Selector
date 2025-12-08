import os, pathlib, tkinter as tk, csv
from Functions import *
from tkinter import ttk, messagebox as msgbox
REL_PATH = pathlib.Path(__file__).resolve().parent
bgcolor = "#6F3D00"
btncolor = "#512C00"
framesize = 350#how closely the buttons will pack to the center
#window
window = tk.Tk()
window.configure(bg=bgcolor)#background color for window


#center the window to the screen
x = (window.winfo_screenwidth() - 450) // 2
y = (window.winfo_screenheight() - 450) // 2
window.geometry(f"450x450+{x}+{y}")




#screens
def mainscreen():
    #remove the top bar
    window.overrideredirect(True) 
    #create the frame to limit button spread
    frame = tk.Frame(window, bg=bgcolor, width= framesize, height= framesize)
    frame.pack(expand=True)
    #adding the 9 buttons
    for x in range(0, 3):
        for y in range(0, 3):
            if(x == y and x == 1):
                #the exit button is the center one
                tk.Button(frame, text="Exit", command=lambda:close(window), padx=15, pady=15).place(relx=0.5, rely=0.5, anchor="center")
                continue
            pos = ""
            #get the position of the standard button (apparently, a string works!)
            if (y < 1):
                pos+="n"
            elif (y > 1):
                pos+="s"
            if (x < 1):
                pos+="w"
            elif (x > 1):
                pos+="e"
            tk.Button(frame, text = "+", command=lambda:browser_select(frame), bg=btncolor, fg="grey", padx=20, pady=20, borderwidth=0, font="12px").place(relx = x/2, rely = y/2, anchor=pos)

def browser_select(f):
    #add the top bar
    window.overrideredirect(False) 
    clear_frame(f)
    frame = tk.Frame(window, bg=bgcolor)
    frame.pack(fill=tk.BOTH, expand=True)

mainscreen()
#create the frame
window.mainloop()