from tkinter import *

window = Tk()
window.configure(bg="lightgrey")
window.title("bismillah")

# Judul
l1 = Label(text="FUEL ANALYSIS FORM", background="lightgrey", font="Times 18")
l1.grid(row=0, column=2, padx=20, pady=30)

# H2O ad
l2 = Label(text="H2O (ad)", background="white", font="Times 14")
l2.grid(row=1, column=0)

l3 = Label(text="Weight container with sample         :", background="lightgrey", font="Times 12")
l3.grid(row=2, column=0, sticky=W, padx=5, pady=5)

e3 = Entry(textvariable=1, background="white")
e3.grid(row=2, column=1, sticky=W, padx=5, pady=5)

l4 = Label(text="Weight empty container                  :", background="lightgrey", font="Times 12")
l4.grid(row=3, column=0, sticky=W, padx=5, pady=5)

e4 = Entry(textvariable=1, background="white")
e4.grid(row=3, column=1, sticky=W, padx=5, pady=5)

l5 = Label(text="Container with sample after heated :", background="lightgrey", font="Times 12")
l5.grid(row=4, column=0, sticky=W, padx=5, pady=5)
l6 = Label(text="Result                                            :", background="lightgrey", font="Times 12")
l6.grid(row=5, column=0, sticky=W, padx=5, pady=5)



a3_entry = Entry(textvariable=1, background="white")
a3_entry.grid(row=4, column=1, sticky=W, padx=5, pady=5)
a4_entry = Entry(textvariable=1, background="white")
a4_entry.grid(row=5, column=1, sticky=W, padx=5, pady=5)

a11_label = Label(text="g", background="lightgrey", font="Times 12")
a11_label.grid(row=2, column=2, sticky=W, padx=5, pady=5)
a12_label = Label(text="g", background="lightgrey", font="Times 12")
a12_label.grid(row=3, column=2, sticky=W, padx=5, pady=5)
a13_label = Label(text="g", background="lightgrey", font="Times 12")
a13_label.grid(row=4, column=2, sticky=W,padx=5, pady=5)
a14_label = Label(text="%", background="lightgrey", font="Times 12")
a14_label.grid(row=5, column=2, sticky=W, padx=5, pady=5)

# Ash ad
ash_label = Label(text="Ash (ad)", background="white", font="Times 14")
ash_label.grid(row=1, column=3)

b1_label = Label(text="Weight container with sample         :", background="lightgrey", font="Times 12")
b1_label.grid(row=2, column=3, sticky=W, padx=5, pady=5)
b2_label = Label(text="Weight empty container                  :", background="lightgrey", font="Times 12")
b2_label.grid(row=3, column=3, sticky=W, padx=5, pady=5)
b3_label = Label(text="Container with sample after heated :", background="lightgrey", font="Times 12")
b3_label.grid(row=4, column=3, sticky=W, padx=5, pady=5)
b4_label = Label(text="Result                                            :", background="lightgrey", font="Times 12")
b4_label.grid(row=5, column=3, sticky=W, padx=5, pady=5)

b1_entry = Entry(textvariable=1, background="white")
b1_entry.grid(row=2, column=4, sticky=W, padx=5, pady=5)
b2_entry = Entry(textvariable=1, background="white")
b2_entry.grid(row=3, column=4, sticky=W, padx=5, pady=5)
b3_entry = Entry(textvariable=1, background="white")
b3_entry.grid(row=4, column=4, sticky=W, padx=5, pady=5)
b4_entry = Entry(textvariable=1, background="white")
b4_entry.grid(row=5, column=4, sticky=W, padx=5, pady=5)

b11_label = Label(text="g", background="lightgrey", font="Times 12")
b11_label.grid(row=2, column=5, padx=5, pady=5)
b12_label = Label(text="g", background="lightgrey", font="Times 12")
b12_label.grid(row=3, column=5, padx=5, pady=5)
b13_label = Label(text="g", background="lightgrey", font="Times 12")
b13_label.grid(row=4, column=5, padx=5, pady=5)
b14_label = Label(text="%", background="lightgrey", font="Times 12")
b14_label.grid(row=5, column=5, padx=5, pady=5)

# H2O kb
h2okb_label = Label(text="H2O (kb)", background="white", font="Times 14")
h2okb_label.grid(row=6, column=0)

c1_entry = Entry(textvariable=1, background="white")
c1_entry.grid(row=7, column=0, sticky=EW, padx=5, pady=5)

c11_label = Label(text="%", background="lightgrey", font="Times 12")
c11_label.grid(row=7, column=1,  sticky=W, padx=5, pady=5)

# Calories
GCV_label = Label(text="Calories (GCV)", background="white", font="Times 14")
GCV_label.grid(row=6, column=3)

d1_entry = Entry(textvariable=1, background="white")
d1_entry.grid(row=7, column=3, sticky=EW, padx=5, pady=5)

d11_label = Label(text="cal/g", background="lightgrey", font="Times 12")
d11_label.grid(row=7, column=4,  sticky=W, padx=5, pady=5)

window.mainloop()