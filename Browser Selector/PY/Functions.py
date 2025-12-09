from Variables import *
import sqlite3
def close(window):
    window.destroy()

def clear_frame(frame):
    frame.destroy()

def get_browsers():
    with sqlite3.connect(f"{REL_PATH}\\..\\DB\\db.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT browser_name FROM browsers")
        return cur.fetchall()
    pass

def verify_browser(icon, path, pos):
    #ensure filepath actually exists
    if(os.path.exists(path)):
        #update the browsers database
        with sqlite3.connect(f"{REL_PATH}\\..\\DB\\db.db") as conn:

            cur = conn.cursor()
            cur.execute(f"SELECT browser_exe FROM browsers WHERE browser_name = \"{icon}\"")
            #first, check if there is already a path here
            #print(beautify(cur.fetchall())[0])
            if(beautify(cur.fetchall())[0].lower() != "none"):
                if(not msgbox.askokcancel(title="Path already found", message="This browser has a path already associated with it, override?")):
                    return
                
            #set browser_exe
            cur.execute(f"UPDATE browsers SET browser_exe = \"{path}\" WHERE browser_name = \"{icon}\";")
        

    else:
        msg.showerror(message="That file path couldn't be found!", title="File not found!")
        return

def beautify(tup):
    #disgusting tuples!
    return [str(x).strip("'(),{} ") for x in tup]

def browsefunc(fp):
    fp.delete(0, tk.END)
    filename =filedialog.askopenfilename(filetypes=(("exe files","*.exe"),("All files","*.*")))
    fp.insert(tk.END, filename)