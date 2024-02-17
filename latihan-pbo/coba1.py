import tkinter as tk

window = tk.Tk()
salam = tk.Label(text="hai!")

WButton = tk.Button(   
    text = "klik disini!", 
    width = 20, 
    height = 10, 
    bg = "red", 
    fg = "black",
) 
salam.pack()
WButton.pack()

window.mainloop()