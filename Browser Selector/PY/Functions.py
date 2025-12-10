from Variables import *
import sqlite3
from time import sleep
def close(window):
    window.destroy()

def clear_frame(frame):
    frame.destroy()

def get_browsers():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT browser_name FROM browsers")
        return cur.fetchall()
    pass

def verify_browser(icon, path, pos, ms, f):
    #ensure filepath actually exists
    if(os.path.exists(path)):
        #update the browsers database
        with sqlite3.connect(DB_PATH) as conn:

            cur = conn.cursor()
            cur.execute(f"SELECT browser_exe FROM browsers WHERE browser_name = \"{icon}\"")
            #first, check if there is already a path here
            if(beautify(cur.fetchall())[0].lower() != "none"):
                if(not msgbox.askokcancel(title="Path already found", message="This browser has a path already associated with it, override?")):
                    return
            
            #set browser_exe
            cur.execute(f"UPDATE browsers SET browser_exe = \"{path}\" WHERE browser_name = \"{icon}\";")
            #get the id of the browser (icon)
            cur.execute(f"SELECT browser_ID FROM browsers WHERE browser_name = \"{icon}\"")
            
            browsID = int(cur.fetchall()[0][0])
            #update bpos
            cur.execute(f"INSERT INTO bpos VALUES ({pos[0]}, {pos[1]}, {browsID})")
            
        
        msg.showinfo(title="Complete!", message="Shortcut saved!")

        #go back to the mainscreen
        ms(f)
    else:
        msg.showerror(message="That file path couldn't be found!", title="File not found!")
        return
    
def open_browser(img):
    img = img[len(str(REL_PATH))+1:]
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute(f"SELECT browser_exe FROM bpos LEFT JOIN browsers ON bpos.browser_ID = browsers.browser_ID WHERE browser_icon = \"{img}\";")
        #end the program
        close(window)
        #run the exe
        os.startfile(beautify(cur.fetchall())[0])
        

def get_bpos():
    #get all the coordinates in bpos
    coords = []
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM bpos")
        for i in cur:
            coords.append([i[0], i[1]])
        
    return coords

def get_images():
    #get all the coordinates in bpos
    imgs = []
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        
        cur.execute("SELECT xpos, ypos FROM bpos LEFT JOIN browsers ON bpos.browser_ID = browsers.browser_ID;")
        for i in cur:
            imgs.append([i[0], i[1]])
        
    return imgs

def get_image(x, y):
    #get all the coordinates in bpos
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        
        cur.execute(f"SELECT browser_icon FROM bpos LEFT JOIN browsers ON bpos.browser_ID = browsers.browser_ID WHERE xpos = {x} and ypos = {y};")
        
    return cur.fetchall()[0]


def beautify(tup):
    #disgusting tuples!
    return [str(x).strip("'(),{} ") for x in tup]

def browsefunc(fp):
    fp.delete(0, tk.END)
    filename =filedialog.askopenfilename(filetypes=(("exe files","*.exe"),("All files","*.*")))
    fp.insert(tk.END, filename)