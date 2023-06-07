import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import pyperclip
import threading
import math

version = "Alpha-0.0"

PADX = 10
PADY = 10

fileTypes = [
    ("Common image files", "*.png *.jpg *.jpeg *.gif *.bmp *.tiff *.tif *.ico *.webp"),
    ("All files", "*.*")
]

chars = [
    " ",
    ".",
    ":",
    ";",
    "*",
    "!",
    "?",
    "#",
    "&",
    "@",
]

def askPath():
    tmp = filedialog.askopenfile(filetypes=fileTypes)
    if (tmp is None):
        return
    pathEntry.delete(0, tk.END)
    pathEntry.insert(0, tmp.name)

def generate():
    global result
    print("Generating for: " + pathVar.get())
    try:
        image = Image.open(pathVar.get())
    except AttributeError:
        messagebox.showerror("Error", "Please enter an image path")
        return
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found: " + pathVar.get())
        return
    image = image.resize((int(image.width / 5), int(image.height / 5)))
    # image = image.rotate(90)
    result = ""
    for i in range(image.width):
        for j in range(image.height):
            pixel = image.getpixel((i, j))
            # print(pixel)
            charIndex = round(image.getpixel((i, j))[3] / 255.0 * (len(chars) - 1))
            # print(charIndex)
            result += chars[charIndex]
        result += "\n"
    print(result)
    resultEntry.delete("1.0", "end")
    resultEntry.insert("1.0", result)
    

def exit_():
    root.destroy()
    exit(0)

def copy():
    pyperclip.copy(result)

root = tk.Tk()
root.geometry("600x400")
root.title("Ascii Art Generator Version " + version)

rootFrame = ttk.Frame(root)

pathVar = tk.StringVar()
pathEntry = ttk.Entry(rootFrame, textvariable=pathVar)
pathEntry.pack(expand=True, side=tk.LEFT, padx=PADX, pady=PADY, fill=tk.X)

browseButton = ttk.Button(rootFrame, text="Browse...", command=askPath)
browseButton.pack(side=tk.LEFT, padx=PADX, pady=PADY)

generateButton = ttk.Button(rootFrame, text="Generate", command=generate)
generateButton.pack(side=tk.LEFT, padx=PADX, pady=PADY)

copyButton = ttk.Button(rootFrame, text="Copy", command=copy)
copyButton.pack(side=tk.LEFT, padx=PADX, pady=PADY)

exitButton = ttk.Button(rootFrame, text="Exit", command=exit_)
exitButton.pack(side=tk.LEFT, padx=PADX, pady=PADY)

resultEntry = tk.Text(rootFrame)
resultEntry.pack(expand=True, side=tk.BOTTOM, padx=PADX, pady=PADY, fill=tk.X)
resultEntry.configure(font=("MS Gothic", 4, "normal"))

rootFrame.pack(fill=tk.BOTH)

root.mainloop()
