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

def verify_browser(icon, path):
    #ensure filepath actually exists
    if(os.path.exists(path)):
        pass

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