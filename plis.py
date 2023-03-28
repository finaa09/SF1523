import tkinter as tk
from tkinter import *
import datetime

window = tk.Tk()
window.configure(bg="lightgrey")
window.title("bismillah")



#ga tau tanggal pake apa
tanggal = tk.StringVar()
roomhumidity = tk.StringVar()
roomtemperature = tk.StringVar()
h2oad = tk.StringVar()
w1 = tk.StringVar()
w2 = tk.StringVar()
w3 = tk.StringVar()
ash = tk.StringVar()
w4 = tk.StringVar()
w5 = tk.StringVar()
w6 = tk.StringVar()
vm = tk.StringVar()
w7 = tk.StringVar()
w8 = tk.StringVar()
w9 = tk.StringVar()
h2okb = tk.StringVar()
gcv = tk.StringVar()
fc = tk.StringVar()


# Judul
judul_label = Label(text="FUEL ANALYSIS FORM", background="lightgrey", font="Times 18")
judul_label.grid(row=0, column=2, padx=20, pady=20)

def date():
    date = datetime.datetime.now()
    judul_label.config(text=date)


pilihan = 0

# Tanggal
date_label = Label(text="Date", background="lightgrey", font="Times 11")
date_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=2)

date_entry = Entry(textvariable=tanggal, background="white")
date_entry.grid(row=1, column=1)

# Room Humidity
rh_label = Label(text="Room Humidity", background="lightgrey", font="Times 11")
rh_label.grid(row=2, column=0, sticky=tk.W, padx=10, pady=2)

entry3 = Entry(textvariable=roomhumidity, background="lightgrey")
entry3.grid(row=2, column=1)

# Room Temperature
rt_label = Label(text="Room Temperature", background="lightgrey", font="Times 11")
rt_label.grid(row=3, column=0, sticky=tk.W, padx=10, pady=2)

rh_entry = Entry(textvariable=roomtemperature, background="lightgrey")
rh_entry.grid(row=3, column=1)

# H2O ad
h2o_label = Label(text="H2O (ad)", background="white", font="Times 12")
h2o_label.grid(row=4, column=0)

wa1_label = Label(text="Weight container with sample         :", background="lightgrey", font="Times 12")
wa1_label.grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)
wa2_label = Label(text="Weight empty container                  :", background="lightgrey", font="Times 12")
wa2_label.grid(row=6, column=0, sticky=tk.W, padx=5, pady=5)
wa3_label = Label(text="Container with sample after heated :", background="lightgrey", font="Times 12")
wa3_label.grid(row=7, column=0, sticky=tk.W, padx=5, pady=5)
h2oad1_label = Label(text="Result                                            :", background="lightgrey", font="Times 12")
h2oad1_label.grid(row=8, column=0, sticky=tk.W, padx=5, pady=5)

w1_entry = Entry(textvariable=w1, background="white")
w1_entry.grid(row=5, column=1, sticky=tk.W, padx=5, pady=5)
w2_entry = Entry(textvariable=w2, background="white")
w2_entry.grid(row=6, column=1, sticky=tk.W, padx=5, pady=5)
w3_entry = Entry(textvariable=w3, background="white")
w3_entry.grid(row=7, column=1, sticky=tk.W, padx=5, pady=5)
h2oad_entry = Entry(textvariable=h2oad, background="white")
h2oad_entry.grid(row=8, column=1, sticky=tk.W, padx=5, pady=5)

wi1_label = Label(text="g", background="lightgrey", font="Times 12")
wi1_label.grid(row=5, column=2, sticky=tk.W, padx=5, pady=5)
wi2_label = Label(text="g", background="lightgrey", font="Times 12")
wi2_label.grid(row=6, column=2, sticky=tk.W, padx=5, pady=5)
wi3_label = Label(text="g", background="lightgrey", font="Times 12")
wi3_label.grid(row=7, column=2, sticky=tk.W,padx=5, pady=5)
h2oad2_label = Label(text="%", background="lightgrey", font="Times 12")
h2oad2_label.grid(row=8, column=2, sticky=tk.W, padx=5, pady=5)

# Ash ad
ash_label = Label(text="Ash (ad)", background="white", font="Times 12")
ash_label.grid(row=9, column=0)

wa4_label = Label(text="Weight container with sample         :", background="lightgrey", font="Times 12")
wa4_label.grid(row=10, column=0, sticky=tk.W, padx=5, pady=5)
wa5_label = Label(text="Weight empty container                  :", background="lightgrey", font="Times 12")
wa5_label.grid(row=11, column=0, sticky=tk.W, padx=5, pady=5)
wa6_label = Label(text="Container with sample after heated :", background="lightgrey", font="Times 12")
wa6_label.grid(row=12, column=0, sticky=tk.W, padx=5, pady=5)
ash1_label = Label(text="Result                                            :", background="lightgrey", font="Times 12")
ash1_label.grid(row=13, column=0, sticky=tk.W, padx=5, pady=5)

w4_entry = Entry(textvariable=w4, background="white")
w4_entry.grid(row=10, column=1, sticky=tk.W, padx=5, pady=5)
w5_entry = Entry(textvariable=w5, background="white")
w5_entry.grid(row=11, column=1, sticky=tk.W, padx=5, pady=5)
w6_entry = Entry(textvariable=w6, background="white")
w6_entry.grid(row=12, column=1, sticky=tk.W, padx=5, pady=5)
ash_entry = Entry(textvariable=ash, background="white")
ash_entry.grid(row=13, column=1, sticky=tk.W, padx=5, pady=5)

wi4_label = Label(text="g", background="lightgrey", font="Times 12")
wi4_label.grid(row=10, column=2, sticky=tk.W, padx=5, pady=5)
wi5_label = Label(text="g", background="lightgrey", font="Times 12")
wi5_label.grid(row=11, column=2, sticky=tk.W, padx=5, pady=5)
wi6_label = Label(text="g", background="lightgrey", font="Times 12")
wi6_label.grid(row=12, column=2, sticky=tk.W, padx=5, pady=5)
ash2_label = Label(text="%", background="lightgrey", font="Times 12")
ash2_label.grid(row=13, column=2, sticky=tk.W, padx=5, pady=5)

# Volatile
VM_label = Label(text="Volatile Matter (ad)", background="white", font="Times 12")
VM_label.grid(row=14, column=0)

wa7_label = Label(text="Weight container with sample         :", background="lightgrey", font="Times 12")
wa7_label.grid(row=15, column=0, sticky=tk.W, padx=5, pady=5)
wa8_label = Label(text="Weight empty container                  :", background="lightgrey", font="Times 12")
wa8_label.grid(row=16, column=0, sticky=tk.W, padx=5, pady=5)
wa9_label = Label(text="Container with sample after heated :", background="lightgrey", font="Times 12")
wa9_label.grid(row=17, column=0, sticky=tk.W, padx=5, pady=5)
vm1_label = Label(text="Result                                            :", background="lightgrey", font="Times 12")
vm1_label.grid(row=18, column=0, sticky=tk.W, padx=5, pady=5)

w7_entry = Entry(textvariable=w7, background="white")
w7_entry.grid(row=15, column=1, sticky=tk.W, padx=5, pady=5)
w8_entry = Entry(textvariable=w8, background="white")
w8_entry.grid(row=16, column=1, sticky=tk.W, padx=5, pady=5)
w9_entry = Entry(textvariable=w9, background="white")
w9_entry.grid(row=17, column=1, sticky=tk.W, padx=5, pady=5)
vm_entry = Entry(textvariable=vm, background="white")
vm_entry.grid(row=18, column=1, sticky=tk.W, padx=5, pady=5)

wi7_label = Label(text="g", background="lightgrey", font="Times 12")
wi7_label.grid(row=15, column=2, sticky=tk.W, padx=5, pady=5)
wi7_label = Label(text="g", background="lightgrey", font="Times 12")
wi7_label.grid(row=16, column=2, sticky=tk.W, padx=5, pady=5)
wi7_label = Label(text="g", background="lightgrey", font="Times 12")
wi7_label.grid(row=17, column=2, sticky=tk.W, padx=5, pady=5)
vm2_label = Label(text="%", background="lightgrey", font="Times 12")
vm2_label.grid(row=18, column=2, sticky=tk.W, padx=5, pady=5)

# H2O kb
h2okb1_label = Label(text="H2O (kb)", background="white", font="Times 12")
h2okb1_label.grid(row=4, column=3, sticky=tk.W, padx=10)

h2okb_entry = Entry(textvariable=h2okb, background="white")
h2okb_entry.grid(row=4, column=4, padx=5, pady=5)

h2okb2_label = Label(text="%", background="lightgrey", font="Times 12")
h2okb2_label.grid(row=4, column=5, sticky=tk.W, padx=5, pady=5)

# Calories
gcv1_label = Label(text="Calories (GCV)", background="white", font="Times 12")
gcv1_label.grid(row=5, column=3, sticky=tk.W, padx=10)

gcv_entry = Entry(textvariable=gcv, background="white")
gcv_entry.grid(row=5, column=4, padx=5, pady=5)

gcv2_label = Label(text="%", background="lightgrey", font="Times 12")
gcv2_label.grid(row=5, column=5, sticky=tk.W, padx=5, pady=5)

# 5. Tombol
tombol_hitung = Button(text="Hitung")
tombol_hitung.grid(row=6, column=4, padx=10, pady=10)

# fungsi

# H2O (ad) yg kedua
h2okb_label = Label(text="H2O (ad)", background="white", font="Times 12")
h2okb_label.grid(row=7, column=3, sticky=tk.W, padx=10)

c1_entry = Entry(textvariable=h2oad, background="white")
c1_entry.grid(row=7, column=4, padx=5, pady=5)

c11_label = Label(text="%", background="lightgrey", font="Times 12")
c11_label.grid(row=7, column=5, sticky=tk.W, padx=5, pady=5)

# Ash (ad) yg kedua
h2okb_label = Label(text="Ash (ad)", background="white", font="Times 12")
h2okb_label.grid(row=8, column=3, sticky=tk.W, padx=10)

c1_entry = Entry(textvariable=ash, background="white")
c1_entry.grid(row=8, column=4, padx=5, pady=5)

c11_label = Label(text="%", background="lightgrey", font="Times 12")
c11_label.grid(row=8, column=5, sticky=tk.W, padx=5, pady=5)

# Volatile Matter (ad) yg kedua
h2okb_label = Label(text="Volatile Matter (ad)", background="white", font="Times 12")
h2okb_label.grid(row=9, column=3, sticky=tk.W, padx=10)

c1_entry = Entry(textvariable=vm, background="white")
c1_entry.grid(row=9, column=4, padx=5, pady=5)

c11_label = Label(text="cal/g", background="lightgrey", font="Times 12")
c11_label.grid(row=9, column=5, sticky=tk.W, padx=5, pady=5)

# Fixed Carbon (ad) yg kedua
h2okb_label = Label(text="Fixed Carbon (ad)", background="white", font="Times 12")
h2okb_label.grid(row=10, column=3, sticky=tk.W, padx=10)

c1_entry = Entry(textvariable=fc, background="white")
c1_entry.grid(row=10, column=4, padx=5, pady=5)

c11_label = Label(text="%", background="lightgrey", font="Times 12")
c11_label.grid(row=10, column=5, sticky=tk.W, padx=5, pady=5)


#bikin tempat hasilnya dulu, terus bikin fungsi
window.mainloop()