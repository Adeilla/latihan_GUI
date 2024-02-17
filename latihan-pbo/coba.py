import tkinter as tk

def show(): 
    namdep = e1.get()
    nambel = e2.get()
    output_label.config(text=f" {namdep} {nambel}")

master = tk.Tk()
master.title('illa')

tk.Label(master, text="namdep").grid(row=0) 
tk.Label(master, text="nambel").grid(row=1)
  
e1 = tk.Entry(master) 
e2 = tk.Entry(master) 
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 

output_label = tk.Label(master, text="")
output_label.grid(row=2, columnspan=2)

tombol_cetak = tk.Button(master, text="cetak", command=show)
tombol_cetak.grid(row=3, columnspan=2)

master.mainloop()