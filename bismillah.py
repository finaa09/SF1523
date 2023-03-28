import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(bg="white")
window.geometry("450x300")
window.resizable(True,True)
window.title("H2O (ad)")

containersample = tk.StringVar()
container = tk.StringVar()
containersample2 = tk.StringVar()

def tombol_click():
    pesan = f"Moisture_ADL = {containersample2.get()}"
    showinfo(title="Moisture_ADL",message=pesan)

# frame input
input_frame = ttk.Frame(window)
# penempatan Grid, Pack, Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen-komponen
# 1. label container sample
containersample_label = ttk.Label(input_frame,text="Weight Container with Sample")
containersample_label.pack(padx=10,pady=10,fill="x",expand=True)
#2. entry container sample
containersample_entry = ttk.Entry(input_frame,textvariable=containersample)
containersample_entry.pack(padx=10,pady=10,fill="x",expand=True)
# 3. label container
container_label = ttk.Label(input_frame,text="Weight Empty Container")
container_label.pack(padx=10,pady=10,fill="x",expand=True)
# 4. entry container
container_entry = ttk.Entry(input_frame,textvariable=container)
container_entry.pack(padx=10,pady=10,fill="x",expand=True)
# 5. label container sample after heated
containersample2_label = ttk.Label(input_frame,text="Weight Container with Sample After Heated")
containersample2_label.pack(padx=10,pady=10,fill="x",expand=True)
# 6. entry container sample after heated
containersample2_entry = ttk.Entry(input_frame,textvariable=containersample2)
containersample2_entry.pack(padx=10,pady=10,fill="x",expand=True)
# 5. Tombol
tombol_hitung = ttk.Button(input_frame,text="Hitung",command=tombol_click)
tombol_hitung.pack(fill='x',expand=True,padx=10,pady=10)

window.mainloop()