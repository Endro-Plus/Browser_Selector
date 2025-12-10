import tkinter, pathlib, os as oss, tkinter.filedialog
from tkinter import ttk as tttk, messagebox as msgbox
os = oss
tk = tkinter
ttk = tttk
msg = msgbox
filedialog = tkinter.filedialog
REL_PATH = pathlib.Path(__file__).resolve().parent
DB_PATH = f"{REL_PATH}\\..\\DB\\db.db"
IMG_PATH = f"{REL_PATH}\\..\\IMG\\"
bgcolor = "#6F3D00"
btncolor = "#512C00"
framesize = 350#how closely the buttons will pack to the center


window = tk.Tk()