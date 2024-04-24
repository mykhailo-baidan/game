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
povolani12 = []
zdatnosti = []
hp = 10


def start():
    print("-----LIST POSTAVY--------")
    modifikatory()

def povolani():
    print("vyber si vybrat jedno z těchto typu(povolaní) \n"
          "----------------------------------------\n"
          "zadej 1 jestli si chceš vybrat - TICHÝ KID|+1 na obratnost|dovednost střelba\n"
          "zadej 2 jestli si chceš vybrat - GYM - BRO|+1 na sílu|dovednost svaly\n"
          "zadej 3 jestli si chceš vybrat - EMO KID|+1 na bystrost|dovednost nenápadnost\n"
          "zadej 4 jestli si chceš vybrat - ŠÁŠA KID|+1 na osobnost|dovednost humor\n"
          "zadej 5 jestli si chceš vybrat - GAY KID|+1 na sílu|dovednost boj z blízka\n"
          "zadej 6 jestli si chceš vybrat - FOTBAL KID|+1 na obratnost|dovednost výdrž\n"
          "zadej 7 jestli si chceš vybrat - NERD |+1 na bystrost|dovednost čachry\n"
          "zadej 8 jestli si chceš vybrat - KŘESŤAN|+1 na bystrost|dovednost pátrání\n"
          "zadej 9 jestli si chceš vybrat - SIMP |+1 na osobnost|dovednost přesvědčování\n")
    volba1 = input("Co si vybereš?")
    if volba1 == "1":
        print("vybral sis povolání TICHÝ KID")
        povolani12.append("tichý kid")
        global obratnost
        obratnost = obratnost+1
        pozice = dovednosti.index('střelba')
        prvek = dovednosti[pozice]
        del dovednosti[pozice]
        zdatnosti.append(prvek)
        dovednosti1()
    elif volba1 == "2":
        print("vybral sis povolání GYM BRO")
        povolani12.append("gym bro ")
        global sila4
        sila4 = sila4+1
        pozice = dovednosti.index('svaly')
        prvek = dovednosti[pozice]
        del dovednosti[pozice]
        zdatnosti.append(prvek)
        dovednosti1()
    elif volba1 == "3":
        print("vybral sis povolání EMO KID")
        global bystrost
        bystrost = bystrost+1
        pozice = dovednosti.index('nenápadnost')
        prvek = dovednosti[pozice]
        del dovednosti[pozice]
        zdatnosti.append(prvek)
        dovednosti1()
    elif volba1 == "4":
        print("vybral sis povolání ŠÁŠA KID")
        global osobnost
        osobnost = osobnost+1
        pozice = dovednosti.index('humor')
        prvek = dovednosti[pozice]
        del dovednosti[pozice]
        zdatnosti.append(prvek)
        dovednosti1()
    elif volba1 == "5":
        print("vybral sis povolání GAY KID")

        sila4 = sila4+1
        pozice = dovednosti.index('boj z blízka')
        prvek = dovednosti[pozice]
        del dovednosti[pozice]
        zdatnosti.append(prvek)
        dovednosti1()
    elif volba1 == "6":
        print("vybral sis povolání FOTBAL KID")

        obratnost = obratnost+1
        pozice = dovednosti.index('výdrž')
        prvek = dovednosti[pozice]
        del dovednosti[pozice]
        zdatnosti.append(prvek)
        dovednosti1()
    elif volba1 == "7":
        print("vybral sis povolání NERD")

        bystrost = bystrost+1
        pozice = dovednosti.index('čachry')
        prvek = dovednosti[pozice]
        del dovednosti[pozice]
        zdatnosti.append(prvek)
        dovednosti1()
    elif volba1 == "8":
        print("vybral sis povolání KŘESŤAN ")

        bystrost = bystrost+1
        pozice = dovednosti.index('pátrání')
        prvek = dovednosti[pozice]
        del dovednosti[pozice]
        zdatnosti.append(prvek)
        dovednosti1()
    elif volba1 == "9":
        print("vybral sis povolání SIMP")

        osobnost = osobnost+1
        pozice = dovednosti.index('přesvědčování')
        prvek = dovednosti[pozice]
        del dovednosti[pozice]
        zdatnosti.append(prvek)
        dovednosti1()

    else:
        odznova3()


def odznova3():
    print("Tuto variantu jste neměli na výběr\n")
    povolani()

def jmeno1():
    jmeno = input("jak se jmenuješ ")

    print(
        f"jmenuješ se {jmeno}\n"
        f" máš {hp} životu tvoje modifikátory jsou {sila4} pro sílu, {obratnost} pro obratnost, {bystrost} pro bystrost a {osobnost} pro osobnost\n"
        f" a máš zdatnost v: {zdatnosti}")


def modifikatory():
    print("můžeš si rozdělit modifikátory:\n"
          "-1\n"
          "+1\n"
          "+2\n"
          "+3\n"
          "mezi vlastnosi:\n"
          "síla - hrubá fyzická síla, svaly a výdrž \n"
          "obratnost - koordinace pohybu, rychlost, motorika\n"
          "bystrost - smyslové vnímaní, inteligence a příčetnost \n"
          "osobnost - Charisma, empatie a schopnost manipulovat s lidmi\n")
    sila3()


def sila3():
    sila1 = int(input("jaký modifikátor si dáš na sílu :"))
    if mody.__contains__(sila1):
        global sila4
        sila4 = sila4 + sila1
        mody.remove(sila1)
        print(f"tvoje síla je od ted {sila4}")
        obratnost1()
    else:
        print("tento modifikátor jste neměli na výběr")
        sila3()


def obratnost1():
    obratnost3 = int(input("jaký modifikátor si dáš na obratnost :"))
    if mody.__contains__(obratnost3):
        global obratnost
        obratnost = obratnost + obratnost3
        mody.remove(obratnost3)
        print(f"tvoje obratnost je od ted {obratnost}")
        bystr()
    else:
        print("tento modifikátor jste neměli na výběr nebo jste ho už použili na jinou vlastnost")
        obratnost1()


def bystr():
    bystr2 = int(input("jaký modifikátor si dáš na bystrost :"))
    if mody.__contains__(bystr2):
        global bystrost
        bystrost = bystrost + bystr2
        mody.remove(bystr2)
        print(f"tvoje bystrost je od ted {bystrost}")
        osob()
    else:
        print("tento modifikátor jste neměli na výběr nebo jste ho už použili na jinou vlastnost")
        bystr()


def osob():
    osob1 = int(input("jaký modifikátor si dáš na osobnost :"))
    if mody.__contains__(osob1):
        global osobnost
        osobnost = osobnost + osob1
        mody.remove(osob1)
        print(f"tvoje osobnost je od ted {osobnost}")
        povolani()
    else:
        print("tento modifikátor jste neměli na výběr nebo jste ho už použili na jinou vlastnost")
        osob()


def dovednosti1():
    print("tvůj zdatnostní bonus je +2 ten si přidáváš k dovednosti kterou umíš\n"
          "vyber si 4 dovednosti které budeš umět\n"
          "---síla---\n"
          "svaly\n"
          "výdrž\n"
          "boj z blízka\n"
          "---obratnost---\n"
          "plížení\n"
          "čachry\n"
          "střelba\n"
          "---bystrost---\n"
          "vnímání\n"
          "pátrání\n"
          "empatie\n"
          "---osobnost---\n"
          "zastrašování\n"
          "přesvědčování\n"
          "humor\n")
    dovednost1()


def dovednost1():
    print()
    prvnidovednost = input("v jaké dovednosti budeš mít zdatnost\n"
                           "1.  ")
    if dovednosti.__contains__(prvnidovednost):
        pozice = dovednosti.index(prvnidovednost)
        prvek = dovednosti[pozice]
        del dovednosti[pozice]
        zdatnosti.append(prvek)

        print(f"vybíráte si dovednost {prvnidovednost}. \n")
        dovednost2()

    else:
        odznova2()
        dovednost1()


def dovednost2():
    druhadovednost = input("v jaké další dovednosti budeš mít zdatnost\n"
                           "2.  ")
    if dovednosti.__contains__(druhadovednost):
        pozice2 = dovednosti.index(druhadovednost)
        prvek2 = dovednosti[pozice2]
        del dovednosti[pozice2]
        zdatnosti.append(prvek2)

        print(f"vybíráte si dovednost {druhadovednost}.")

        dovednost3()

    else:
        odznova2()
        dovednost2()


def dovednost3():
    tretidovednost = input("v jaké další dovednosti budeš mít zdatnost\n"
                           "3.  ")
    if dovednosti.__contains__(tretidovednost):
        pozice3 = dovednosti.index(tretidovednost)
        prvek3 = dovednosti[pozice3]
        del dovednosti[pozice3]
        zdatnosti.append(prvek3)

        print(f"vybíráte si dovednost {tretidovednost}.")

        dovednost4()

    else:
        odznova2()
        dovednost3()


def dovednost4():
    ctvrtadovednost = input("v jaké další dovednosti budeš mít zdatnost\n"
                            "4.  ")
    if dovednosti.__contains__(ctvrtadovednost):
        pozice3 = dovednosti.index(ctvrtadovednost)
        prvek3 = dovednosti[pozice3]
        del dovednosti[pozice3]
        zdatnosti.append(prvek3)

        print(f"vybíráte si dovednost {ctvrtadovednost}. ")

        zivoty()

    else:
        odznova2()
        dovednost4()


def zivoty():
    if zdatnosti.__contains__("výdrž"):
        global hp
        hp = hp + 2
        print("máš 12 životů")
        jmeno1()
    else:
        print("máš 10 životů")
        jmeno1()


def carecky():
    print(
        "------------------------------------------------------------------------------------------------------------------------------------------")


def odznova2():
    print("Tuto možnost jste bud neměli na výběr nebo už jste si zvolili \nzačni od znova")


start()
