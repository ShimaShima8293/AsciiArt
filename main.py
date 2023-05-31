import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import pyperclip

version = "Alpha-0.0"

PADX = 10
PADY = 10

def askPath():
    tmp = filedialog.askopenfile(filetypes=[("Common image files", "*.png *.jpg *.jpeg *.gif")])
    if (tmp is None):
        return
    pathEntry.delete(0, tk.END)
    pathEntry.insert(0, tmp.name)

def generate():
    print("Generating for: " + pathVar.get())
    try:
        Image.open(pathVar.get())
    except AttributeError:
        messagebox.showerror("Error", "Please enter an image path")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found: " + pathVar.get())


def exit_():
    root.destroy()
    exit(0)

root = tk.Tk()
root.geometry("600x400")
root.title("Ascii Art Generator Version " + version)

rootFrame = tk.Frame(root, bg="#ff0000")

pathVar = tk.StringVar()
pathEntry = ttk.Entry(rootFrame, textvariable=pathVar)
pathEntry.pack(expand=True, side=tk.LEFT, padx=PADX, pady=PADY, fill=tk.X)

browseButton = ttk.Button(rootFrame, text="Browse...", command=askPath)
browseButton.pack(side=tk.LEFT, padx=PADX, pady=PADY)

generateButton = ttk.Button(rootFrame, text="Generate", command=generate)
generateButton.pack(side=tk.LEFT, padx=PADX, pady=PADY)

exitButton = ttk.Button(rootFrame, text="Exit", command=exit_)
exitButton.pack(side=tk.LEFT, padx=PADX, pady=PADY)

resultEntry = tk.Text(rootFrame)
resultEntry.pack(expand=True, side=tk.BOTTOM, padx=PADX, pady=PADY, fill=tk.X)

rootFrame.pack(fill=tk.BOTH)

root.mainloop()