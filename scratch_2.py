import tkinter as tk






root = tk.Tk()
root.title("List postavy")
jmenotext = tk.Label(root, text="sem tadejte svoje jmeno")
jmenotext.pack(pady=5)
jmeno1 = tk.Entry(root, width=30)
jmeno1.pack(pady=30)
def kontrola():
    zaslanytext = jmeno1.get()
    if zaslanytext == "":
        petr.config(text="Opakuji sem zadejte své jméno.")

    else:

        modifikatory()

def modifikatory():
    jmeno1.pack_forget()
    tlacit.pack_forget()
    jmenotext.config(text="můžeš si rozdělit modifikátory:\n"
          "-1\n"
          "+1\n"
          "+2\n"
          "+3\n"
          "mezi vlastnosi:\n"
          "síla - hrubá fyzická síla, svaly a výdrž \n"
          "obratnost - koordinace pohybu, rychlost, motorika\n"
          "bystrost - smyslové vnímaní, inteligence a příčetnost \n"
          "osobnost - Charisma, empatie a schopnost manipulovat s lidmi\n")
    petr1 = tk.Label(root, text="")
    petr1.pack(pady=5
    tlacit1 = tk.Button(root, text="zadat jmeno", command=kontrola)
    tlacit1.place(x=450, y=200)

tlacit = tk.Button(root, text="zadat jmeno", command=kontrola)
tlacit.pack(pady=5)

petr = tk.Label(root, text="")
petr.pack(pady=5)

root.mainloop()
