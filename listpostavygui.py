import tkinter as tk
from tkinter import Entry

mody = [-1, +1, +2, +3]
sila4 = 0
obratnost = 0
bystrost = 0
osobnost = 0
dovednosti = ['svaly', 'výdrž', 'boj z blízka', 'obratnost', 'plížení', 'čachry', 'střelba', 'vnímání', 'pátrání',
              'empatie', 'zastrašování', 'přesvědčování', 'humor']
siladovednosti = ['svaly', 'výdrž', 'boj z blízka']
obrdovednosti = ['obratnost', 'plížení', 'čachry']
bystrdovednosti = ['vnímání', 'pátrání', 'empatie']
osobdovednosti = ['zastrašování', 'přesvědčování', 'humor']
zdatnosti = []

root = tk.Tk()
root.title("List postavy")
jmenotext = tk.Label(root, text="sem tadejte svoje jmeno")
jmenotext.pack(pady=5)
jmeno1: Entry = tk.Entry(root, width=30)
jmeno1.pack(pady=30)
sigma = tk.Label(root, text="")
sigma.place(x=520, y=170)
def skib():
    sigma.config(text="jaký modifikátor si dáš na obratnost:")

tlacitm1 = tk.Button(root, text="-1", command=skib)
tlacitm1.place(x=450, y=200)
tlacitm1.place_forget()




def kontrola():
    zaslanytext = jmeno1.get()
    if zaslanytext == "":
        petr.config(text="Opakuji sem zadejte své jméno.")

    else:
        listpostavy()
        modifikatory()


def listpostavy():
    ok = jmeno1.get()
    bedrich = tk.Label(root, text="------LIST POSTAVY-------\n"
                                  "\n"
                                  f"JMÉNO: {ok}\n"
                                  "------VLASTNOSTI:-----\n"
                                  f"SÍLA: \n"
                                  f"OBRATNOST: \n"
                                  f"BYSTROST\n"
                                  f"OSOBNOST\n"
                                  "\n"
                                  "-----DOVEDNOSTI------\n "
                                  "---síla---\n"
                                  f"svaly\n"
                                  f"výdrž\n"
                                  f"boj z blízka\n"
                                  "---obratnost---\n"
                                  f"plížení\n"
                                  f"čachry\n"
                                  f"střelba\n"
                                  "---bystrost---\n"
                                  f"vnímání\n"
                                  f"pátrání\n"
                                  f"empatie\n"
                                  "---osobnost---\n"
                                  f"zastrašování\n"
                                  f"přesvědčování\n"
                                  f"humor\n")
    bedrich.place(y=10, x=90)


def modifikatory():
    jmeno1.pack_forget()
    jan.pack_forget()
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
    sigma.config(text="jaký modifikátor si dáš na sílu: ")

    tlacitm1 = tk.Button(root, text="-1", command=skib)
    tlacitm1.place(x=450, y=200)
    return tlacitm1


jan = tk.Button(root, text="zadat jmeno", command=kontrola)
jan.pack(pady=5)

petr = tk.Label(root, text="")
petr.pack(pady=5)

root.mainloop()
