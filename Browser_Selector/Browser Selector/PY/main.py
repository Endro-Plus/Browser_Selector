from Functions import *
from Variables import *
from Screens import *


window.configure(bg=bgcolor)#background color for window


#center the window to the screen
x = (window.winfo_screenwidth() - 450) // 2
y = (window.winfo_screenheight() - 450) // 2
window.geometry(f"450x450+{x}+{y}")




#screens
mainscreen()
#create the frame
window.mainloop()