import sys, subprocess, os
def init():
    def load(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
    load("pyinstaller")
    load("customtkinter")

init()

import customtkinter as Ctk




Ctk.set_appearance_mode("dark")
Ctk.set_default_color_theme("dark-blue")

def compilePythonFile(path):
    try:
        init()
        if subprocess.check_call([sys.executable, "-m", "pip", "show", "pyinstaller"]) == 0 and subprocess.check_call([sys.executable, "-m", "pip", "show", "customtkinter"]) == 0:
                subprocess.check_call(["pyinstaller", "--onefile", "-w", path])
        else:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "customtkinter"])
            compilePythonFile()
            return
    except subprocess.CalledProcessError as e:
        print(f"Compilation failed with error code {e.returncode}: {e.cmd}")
        return
        

root = Ctk.CTk()
root.title("Compiler")
root.geometry("500x300")

DirTitle = Ctk.CTkLabel(root,text=("Put file path here!"))

DirEntry = Ctk.CTkEntry(root)

Button = Ctk.CTkButton(master=root, command=lambda: compilePythonFile(DirEntry.get()), text="Compile")


DirTitle.pack(pady=10)
DirEntry.pack(pady=25)

Button.pack()

root.mainloop()
