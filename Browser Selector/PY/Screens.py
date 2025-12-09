
from Variables import *
from Functions import *

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
            
            tk.Button(frame, text = "+", bg=btncolor, command = lambda x=x, y=y: browser_select(frame, x, y), fg="grey", padx=20, pady=20, borderwidth=0, font="12px").place(relx = x/2, rely = y/2, anchor=pos)


def browser_select(f, x, y):
    #add the top bar
    window.title("Browser Select")
    #print(x, y)
    window.overrideredirect(False) 
    clear_frame(f)
    frame = tk.Frame(window, bg=bgcolor)
    frame.pack(fill=tk.BOTH, expand=True)
    tk.Label(frame, text="Which browser should this send you too?", background=bgcolor, fg="white").pack()
    browser_box = ttk.Combobox(frame, values=beautify(get_browsers()), state="readonly")
    browser_box.current(0)#default to the first item
    browser_box.pack()
    tk.Frame(frame, height=30, width=30, bg=bgcolor).pack()#some space
    tk.Label(frame, text="File path to .exe file")
    fp = tk.Entry(frame, width=40)
    fp.pack()
    tk.Button(frame, text="Open Files", command=lambda: browsefunc(fp)).pack()
    tk.Frame(frame, height=60, width=30, bg=bgcolor).pack()#some space
    tk.Button(frame, text="Enter", command=lambda:verify_browser(browser_box.get(), fp.get(), [x, y])).pack()

    