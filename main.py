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

wchars = [
    "　",
    "・",
    "。",
    "：",
    "；",
    "＊",
    "！",
    "？",
    "＃",
    "＆",
    "＠"
]

charOptions = ["Full-width", "Half-width"]

def askPath(event=None):
    tmp = filedialog.askopenfile(filetypes=fileTypes)
    if (tmp is None):
        return
    pathEntry.delete(0, tk.END)
    pathEntry.insert(0, tmp.name)

def generate(event=None):
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
    result = ""
    if (charOptionVar.get() == charOptions[0]):
        charUsing = wchars
    else:
        charUsing = chars

    for i in range(image.height):
        for j in range(image.width):
            pixel = image.getpixel((j, i))
            charIndex = round(pixel[3] / 255.0 * (len(charUsing) - 1))
            result += charUsing[charIndex]
        result += "\n"
    print(result)
    resultEntry.delete("1.0", "end")
    resultEntry.insert("1.0", result)
    

def exit_():
    root.destroy()
    exit(0)

def copy():
    pyperclip.copy(result)

def zoomIn(event=None):
    global zoom
    zoom += 1
    resultEntry.configure(font=("MS Gothic", zoom, "normal"))

def zoomOut(event=None):
    global zoom
    zoom -= 1
    if (zoom < 1):
        zoom = 1
        return
    resultEntry.configure(font=("MS Gothic", zoom, "normal"))

def zoomReset(event=None):
    global zoom
    zoom = 4
    resultEntry.configure(font=("MS Gothic", zoom, "normal"))

root = tk.Tk()
root.geometry("1920x1080")
root.title("Ascii Art Generator")

buttonFrame = ttk.Frame(root)

pathVar = tk.StringVar()
pathEntry = ttk.Entry(buttonFrame, textvariable=pathVar)
pathEntry.pack(expand=True, side=tk.LEFT, padx=PADX, pady=PADY, fill=tk.X)

browseButton = ttk.Button(buttonFrame, text="Browse...", command=askPath)
browseButton.pack(side=tk.LEFT, padx=PADX, pady=PADY)

charOptionVar = tk.StringVar(root)
# charOptionVar.set(charOptions[0])
charOption = ttk.OptionMenu(buttonFrame, charOptionVar, charOptions[0], *charOptions)
charOption.pack(side=tk.LEFT, padx=PADX, pady=PADY)

generateButton = ttk.Button(buttonFrame, text="Generate", command=generate)
generateButton.pack(side=tk.LEFT, padx=PADX, pady=PADY)

copyButton = ttk.Button(buttonFrame, text="Copy", command=copy)
copyButton.pack(side=tk.LEFT, padx=PADX, pady=PADY)

exitButton = ttk.Button(buttonFrame, text="Exit", command=exit_)
exitButton.pack(side=tk.LEFT, padx=PADX, pady=PADY)

buttonFrame.pack(fill=tk.BOTH)

resultFrame = ttk.Frame(root)

resultEntry = tk.Text(resultFrame)
resultEntry.pack(expand=True, side=tk.BOTTOM, padx=PADX, pady=PADY, fill=tk.BOTH)
zoomReset()

root.bind("<Control-=>", zoomIn)
root.bind("<Control-minus>", zoomOut)
root.bind("<Control-0>", zoomReset)
root.bind("<Control-r>", generate)
root.bind("<Control-o>", askPath)
root.bind("<Control-c>", copy)


resultFrame.pack(fill=tk.BOTH, expand=True)

menu = tk.Menu(root)

fileMenu = tk.Menu(menu, tearoff=0)
fileMenu.add_command(label="Open...", command=askPath, accelerator="Ctrl+O")
fileMenu.add_command(label="Generate", command=generate, accelerator="Ctrl+R")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=askPath, accelerator="Alt+F4")
menu.add_cascade(label="File", menu=fileMenu)

viewMenu = tk.Menu(menu, tearoff=0)
viewMenu.add_command(label="Zoom In", command=zoomIn, accelerator="Ctrl+=")
viewMenu.add_command(label="Zoom Out", command=zoomOut, accelerator="Ctrl+-")
viewMenu.add_command(label="Reset Zoom", command=zoomReset, accelerator="Ctrl+0")
menu.add_cascade(label="View", menu=viewMenu)

root.configure(menu=menu)
root.mainloop()
