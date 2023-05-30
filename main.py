import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image

imagepath = ""

def openImage():
    global imagepath
    imagepath = filedialog.askopenfile(filetypes=[("Common image files", "*.png *.jpg *.jpeg *.gif")]).name

def generate():
    print(imagepath)

root = tk.Tk()

rootFrame = ttk.Frame(root)

pathBox = ttk.Entry(rootFrame)
pathBox.pack(anchor=tk.W, expand=True, side=tk.LEFT)

openButton = ttk.Button(rootFrame, text="Open image...", command=openImage)
openButton.pack(anchor=tk.E, side=tk.LEFT)

generateButton = ttk.Button(rootFrame, text="Generate", command=generate)
generateButton.pack(side=tk.TOP)

rootFrame.pack()

root.mainloop()