from tkinter import *

states = {
    "ut": 0.0685,
    "nv": 0.08,
    "tx": 0.0625,
    "al": 0.04,
    "ca": 0.0825
}


def calc(event):
    s1 = ent_1.get()
    s2 = ent_2.get()
    state_percent = states[variable.get().lower()]
    proizvedenie = float(s1) * float(s2)
    if proizvedenie >= 1000:
        your_discount = proizvedenie * 0.03
    elif proizvedenie >= 5000:
        your_discount = proizvedenie * 0.05
    elif proizvedenie >= 7000:
        your_discount = proizvedenie * 0.07
    elif proizvedenie >= 10000:
        your_discount = proizvedenie * 0.1
    elif proizvedenie >= 15000:
        your_discount = proizvedenie * 0.15
    else:
        your_discount = 0
    final = proizvedenie - your_discount
    state_tax = final * state_percent
    final_with_state_tax = final + state_tax
    lab_4['text'] = 'Your price + discount + state tax: ' + str(round(final_with_state_tax, 2)) + ' $'
    lab_3['text'] = 'Your price + discount: ' + str(round(final, 2)) + ' $'


root = Tk()
root.geometry("400x200")
root.configure(bg='red')
root.title("Jos calculator powered by MTS")


lab_1 = Label(root, text="SKU", font="Arial 10",bg='red',fg='white')
ent_1 = Entry(width=150)
lab_2 = Label(root, text="Price", font="Arial 10",bg='red',fg='white')
ent_2 = Entry(width=150)
but = Button(text="Calculate")
lab_3 = Label(width=150, bg='white', fg='black')
lab_4 = Label(width=150, bg='white', fg='black')
lab_5 = Label(root, text="State", font="Arial 10",bg='red',fg='white')

variable = StringVar(root)
variable.set("UT")# default value

w = OptionMenu(root, variable, "UT", "NV", "TX", "AL", "CA")
lab_5.pack()
w.pack()
but.bind('<Button-1>', calc)

lab_1.pack()
ent_1.pack()

lab_2.pack()
ent_2.pack()
but.pack()


lab_3.pack()
lab_4.pack()
root.mainloop()
