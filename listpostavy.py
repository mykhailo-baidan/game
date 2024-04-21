mody = [-1, +1, +2, +3]
sila4 = 0
obratnost = 0
bystrost = 0
osobnost = 0
dovednosti = ['svaly', 'výdrž', 'boj z blízka', 'obratnost', 'plížení', 'čachry', 'střelba', 'vnímání', 'pátrání',
              'empatie', 'zastrašování', 'přesvědčování', 'humor']
siladovednosti = ['svaly', 'výdrž', 'boj z blízka']
obrdovednosti = ['obratnost', 'plížení', 'čachry']
bystrdovednosti = ['vnímání', 'pátrání','empatie']
osobdovednosti = ['zastrašování', 'přesvědčování', 'humor']

zdatnosti = []


def jmeno1():
    print("list postavy")
    jmeno = input("jak se jmenuješ ")
    modifikatory()


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
        dovednosti1()
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

        dovednosti88 = input(f"vybíráte si dovednost {prvnidovednost}? \n"
                             f"jste si jistí(ano/ne)?   ")
        if dovednosti88 == "ano":
            dovednost2()

        elif dovednosti88 == "ne":
            dovednost1()
        else:
            odznova2()
            dovednost1()
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

        dovednosti88 = input(f"vybíráte si dovednost {druhadovednost}? \n"
                             f"jste si jistí(ano/ne)?   ")
        if dovednosti88 == "ano":
            dovednost3()

        elif dovednosti88 == "ne":
            dovednost2()
        else:
            odznova2()
            dovednost2()
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

        dovednosti88 = input(f"vybíráte si dovednost {tretidovednost}? \n"
                             f"jste si jistí(ano/ne)?   ")
        if dovednosti88 == "ano":
            dovednost4()

        elif dovednosti88 == "ne":
            dovednost3()
        else:
            odznova2()
            dovednost3()
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

        dovednosti88 = input(f"vybíráte si dovednost {ctvrtadovednost}? \n"
                             f"jste si jistí(ano/ne)?   ")
        if dovednosti88 == "ano":
            zdatnosti1()

        elif dovednosti88 == "ne":
            dovednost4()
        else:
            odznova2()
            dovednost4()
    else:
        odznova2()
        dovednost4()


def zdatnosti1():
    print("tvoje zdatnosti jsou:")
    print(zdatnosti)
    print("")


def carecky():
    print(
        "------------------------------------------------------------------------------------------------------------------------------------------")


def odznova2():
    print("Tuto možnost jste bud neměli na výběr nebo už jste si zvolili \nzačni od znova")


jmeno1()
