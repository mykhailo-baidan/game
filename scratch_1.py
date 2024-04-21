


    tlacitm1 = tk.Button(root, text="-1", command=modm1)
    tlacitm1.place(x=450, y=200)

    tlacit1 = tk.Button(root, text="+1", command=modm2)
    tlacit1.place(x=500, y=200)

    tlacit2 = tk.Button(root, text="+2", command=modm3)
    tlacit2.place(x=550, y=200)

    tlacit3 = tk.Button(root, text="+3", command=modm4)
    tlacit3.place(x=600, y=200)
def modm1():

    pavel.config(text="jaký modifikátor si dáš na obratnost")
    global tlacitm1
    tlacitm1.place.forget()


def modm2():
    global pavel
    pavel.config(text="jaký modifikátor si dáš na obratnost")
    global tlacit2
    tlacit2.place.forget()


def modm3():
    global pavel
    pavel.config(text="jaký modifikátor si dáš na obratnost")
    global tlacit3
    tlacit3.place.forget()


def modm4():
    global pavel
    pavel.config(text="jaký modifikátor si dáš na obratnost")
    global tlacit4
    tlacit4.place.forget()
