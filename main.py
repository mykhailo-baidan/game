#!/usr/bin/python
# -*- coding: utf-8 -*-

obusek1 = 0
damage = 1
pocetobleceni = 0
kukla1 = 0
penezenka1 = 0
zivotystrazneho1 = 1
lamakuvroubik = 0
zivotylamaka = 4

def start():
    intro()
    dvere1()


def dvere1():
    print(
        "zadej 1 jestli chceš jít k dveřím \n"
        "zadej 2 jestli chceš jít dál spát \n"
        "zadej 3 jestli si chceš prohlédnout místnost")
    carecky()

    volba = int(input("co budeš dělat"))
    carecky()

    if volba == 1:
        dvere2()
    elif volba == 2:
        print("ponořili jste se do spánku ale už jste se nevzbudili")
        prohra()
    elif volba == 3:
        print("prohlížíš si místnost ale nic zajímavého jsi nenašel")
        dvere1()
    else:
        odznova()
        dvere1()


def dvere2():
    print(
        "přišel jsi ke dveřím \n"
        "zadej 1 jestli si chceš prohlédnout dveře \n"
        "zadej 2 jestli se chceš pokusit otevřít dveře \n")
    volba15 = int(input("co budeš dělat "))
    carecky()
    if volba15 == 1:
        print("díváš se na dveře a vypadají docela schátrale panty jsou zrezlé a dřevo prohnilé")
        dvere3()
    elif volba15 == 2:
        print("jsou zamčené")
        dvere3()
    else:
        odznova()
        dvere1()


def dvere3():
    print(
        "zadej 1 jestli si chceš prohlédnout dveře \n"
        "zadej 2 jestli se chceš pokusit otevřít dveře \nzadej 3 jestli chceš vyrazit dveře ")
    volba16 = int(input("co budeš dělat "))
    carecky()
    if volba16 == 1:
        print("díváš se na dveře a vypadají docela schátrale panty jsou zrezlé a dřevo prohnilé")
        dvere2()
    elif volba16 == 2:
        print("jsou zamčené")
        dvere3()
    elif volba16 == 3:
        print("dveře se pod nárazem zničili a ocitl ses v dálší místnosti")
        mistnost2()
    else:
        print("Měli jste na výběr jen tři možnosti ")
        dvere2()


def intro():
    print("--------Hra utěk----------")
    print("ve hře zadávejte pouze ano/ne nebo čísla\n"
          "zdravím zavřeli tě do sklepa tvůj cíl je utéci \n"
          "probudil ses v koutě malé temné místnosti okolo tebe se nic nenachází. Před sebou vidíš dveře jinak je místnost zdánlivě prázdná")


def carecky():
    print(
        "------------------------------------------------------------------------------------------------------------------------------------------")


def prohra():
    print("prohrali jste")
    volba3 = input("chcete začít odznova")
    if volba3 == "ano":
        global damage
        damage = 1
        global pocetobleceni
        pocetobleceni = 0
        start()
    elif volba3 == "ne":
        print("dobře jsi hrál")
    else:
        print("dobře jsi hrál")


def strazny():
    volba5 = int(input("co chceš říct strážnému:\n"
                       "zadej 1 jestli se ho chceš zeptat co se tu děje\n"
                       "zadej 2 jestli chceš říct že počasí je dneska krásne \n"
                       "zadej 3 jestli mu chceš říct vtip  \n"
                       "zadej 4 jestli se chceš zeptat strážného na jméno"))
    carecky()
    if volba5 == 1:
        print("ptáš se strážce co se děje ale ten říká že to nemáš vědět a bije tě po hlavě obuškem")
        prohra()
    elif volba5 == 2:
        print("říkáš počasí je dneska krásné strážce odpovídá ano je to mu tak ale co mi chceš říct")
        strazny()
    elif volba5 == 3:
        print("říkáš strážnému jestli chce slyšet vtip. strážce nadšeně říká že ano a že miluje vtipy ")
        input("vtip:")
        print(
            "strážný se naprosto popadá smíchy lepší vtip v životě neslyšel smíchy mu spadl obušek na zem takže se pro něho naklonil ")
        reakce()
    elif volba5 == 4:
        print("strážný je docela překvapen ale odpovídá: mé jméno je jakobín a jsem strážce sklepa")
        strazny()
    else:
        odznova()
        strazny()


def mistnost2():
    carecky()
    print(
        "další místnost už není tak prázdná jak předešlá před sebou vidíš osobu v černé kukle a obuškem. nevypadá moc nadšeně z pohledu na tebe\n"
        "svým hrubým hlasem křičí : hej tady nemáš bejt při tom připravuje svůj obušek k útoku\n"
        "zadej 1 jestli se chceš vrátit do první místnosti \n"
        "zadej 2 jestli chceš vrazit strážci  \n"
        "zadej 3 jestli si chceš popovídat se strážným")
    volba4 = int(input("co budeš dělat"))
    if volba4 == 1:
        print(
            "otáčíš se abyses vrátil do první místnosti ale v tu chvíli tě něco těžkeho udeří do zátylku a padáš do bezvědomí ze kterého se už neprobudíš")
        prohra()
    elif volba4 == 2:
        print(
            "už se rozmachuješ po strážným ale on je rychlejší s rychlostí blesku tě bije do hlavy a padáš do bezvědomí ze kterého se už neprobudíš")
        prohra()
    elif volba4 == 3:
        print("říkáš strážnému počkej počkej a strážný se zastavil")
        strazny()
    else:
        odznova()
        mistnost2()


def vtip():
    print("říkáš strážnému jestli chce slyšet vtip. strážce nadšeně říká že ano a že miluje vtipy ")
    input("vtip:")
    print("strážný se naprosto popadá smíchy lepší vtip v životě neslyšel smíchy mu spadl obušek na zem ")
    reakce()


def reakce():
    print("tvoje reakce na to: \n"
          "zadej 1 pokud nic nepodnikáš \n"
          "zadej 2 pokud se chceš pokusit udeřit strážného do zátylku ")
    reakce1 = int(input("reakce:"))
    if reakce1 == 1:
        print("strážný zvedá obušek a říká ten byl dobrej ")
        strazny()
    elif reakce1 == 2:
        print("Vší silou jsi udeřil strážného a ten se v bezvědomí svalil na zem")
        strazny2()
    else:
        odznova()
        reakce()


def odznova():
    print("Tuto možnost jste na výběr neměli \nzačni od znova")


def strazny2():
    print("zadej 1 jestli se chceš vrátit do první místnosti \n"
          "zadej 2 jestli chceš prohledát strážného \n"
          "zadej 3 jestli se chceš rozhlédnout po okolí\n"
          "zadej 4 jestli si chceš zkontrolovat to jestli strážný dýchá\n"
          "  .           .                         ")
    volba6 = int(input("co budeš dělat dál:  "))

    if volba6 == 1:
        print("vracíš se do první místnosti ")
        pseudomistnost1()

    elif volba6 == 2:
        vecistrazneho()
    elif volba6 == 3:
        print(
            "rozhlížíš se okolo sebe a vidíš dveře před sebou a taky napravo do tebe na zemi je rudý koberec a stěny potřísněné krví v levým rohu místnosti vidíš židli na které je položená kniha")
        volba11 = input("chceš se podívát na židli ")
        if volba11 == "ano":
            print("přišel jsi k židli a vidíš na ní knihu Stopařův průvodce Galaxii")
            strazny2()
        elif volba11 == "ne":
            strazny2()
        else:
            odznova()
            strazny2()
    elif volba6 == 4:
        print("naklonil ses k strážnému a zkontroval jestli dýcha. Ano ještě dýcha")
        pseudostrazny()
    else:
        odznova()
        strazny()


def pseudomistnost1():
    print(
        "zadej 1 jestli chceš jít zpět do další místnosti \n"
        "zadej 2 jestli chceš jít dál spát \n"
        "zadej 3 jestli si chceš prohlédnout místnost")
    volba = int(input("co budeš dělat"))
    carecky()

    if volba == 1:
        print("vracíš se do druhé místnosti a pořád tam leží tělo strážného")
        pseudostrazny()
    elif volba == 2:
        print("ponořili jste se do spánku ale už jste se nevzbudili")
        prohra()
    elif volba == 3:
        print("prohlížíš si místnost ale nic zajímavého jsi nenašel")
        pseudomistnost1()
    else:
        odznova()
        pseudomistnost1()


def pseudostrazny():
    print("zadej 1 jestli se chceš vrátit do první místnosti \n"
          "zadej 2 jestli chceš prohledát strážného \n"
          "zadej 3 jestli se chceš rozhlédnout po okolí\n"
          "zadej 4 jestli si chceš zkontrolovat to jestli strážný dýchá\n"
          "zadej 5 jestli chceš jít k dveřím které jsou napravo \n"
          "zadej 6 jestli se chceš jít k dveřím které jsou naproti tobě \n"
          "zadej 7 jestli chceš dorazit strážného   ")
    volba6 = int(input("co budeš dělat dál:  "))

    if volba6 == 1:
        print("vracíš se do první místnosti ")
        pseudomistnost1()

    elif volba6 == 2:
        vecistrazneho()
    elif volba6 == 3:
        print(
            "rozhlížíš se okolo sebe a vidíš dveře před sebou a taky napravo do tebe na zemi je rudý koberec a stěny potřísněné krví v levým rohu místnosti vidíš židli na které je položená kniha")
        volba11 = input("chceš se podívát na židli ")
        if volba11 == "ano":
            print("přišel jsi k židli a vidíš na ní knihu Stopařův průvodce Galaxii")
            strazny2()
        elif volba11 == "ne":
            strazny2()
        else:
            odznova()
            strazny2()
    elif volba6 == 4:
        global zivotystrazneho1
        if zivotystrazneho1 == 1:
            print("naklonil ses k strážnému a zkontroval jestli dýcha. Ano ještě dýcha")
            pseudostrazny()

        elif zivotystrazneho1 == 0:
            print("naklonil ses k stážnému a zkontroval jestli dýchá. Ne je mrtev")
            pseudostrazny()
        else:
            print("chyba")

    elif volba6 == 7:
        global zivotystrazneho1
        if zivotystrazneho1 == 1:
            print("nemilosrdně lámeš strážnému vaz")
            zivotystrazneho1 = zivotystrazneho1 - 1
            pseudostrazny()
        else:
            print("strážný už je mrtev")
            pseudostrazny()
    elif volba6 == 6:
        otevrenedvere()

    elif volba6 == 5:
        zamcenedvere()
    else:
        odznova()
        pseudostrazny()


def vecistrazneho():
    print("Sklonil ses k strážnému a vidíš že u sebe má jen \n"
          "černou kuklu\n"
          "obušek\n"
          "peněženku \n")

    print("zadej 1 jestli si chceš vzít černou kuklu \n"
          "zadej 2 jestli si chceš vzít obušek \n"
          "zadej 3 jestli se chceš podívat do peněženky \n"
          "zadej 4 jestli nechceš prohledávat strážného")

    volba7 = int(input("co z toho si chceš vzít ?"))

    if volba7 == 1:
        if kukla == 1:
            print("ale ty už sis vzal kuklu")
            vecistrazneho()
        else:
            kukla()
    elif volba7 == 2:
        if obusek1 == 1:
            print("ten obušek už sis vzal")
            vecistrazneho()
        else:
            obusek()
    elif volba7 == 3:
        if penezenka1 == 1:
            print("peněženka je u tebe")
        penezenka()
    elif volba7 == 4:
        pseudostrazny()

    else:
        odznova()
        vecistrazneho()


def kukla():
    global kukla1
    if kukla1 == 1:
        print("už ji máš u sebe")
    else:

        print("bereš si do ruky kuklu")
        volba7 = input("chceš si dát kuklu na hlavu? ")
        if volba7 == "ano":

            kukla1 = kukla1 + 1
            global pocetobleceni
            pocetobleceni = pocetobleceni + 1
            vecistrazneho()
        elif volba7 == "ne":
            volba7 = input("chceš vrátit kuklu strážnému? ")
            if volba7 == "ano":
                print("vrátil jsi kuklu strážnému")
                vecistrazneho()
            elif volba7 == "ne":
                kukla()


def obusek():
    print("bereš si do ruky obušek")
    volba9 = input("chceš si nechat obušek? ")
    if volba9 == "ano":
        global obusek1
        obusek1 = obusek1 + 1
        global damage
        damage = damage + 1
        vecistrazneho()
    elif volba9 == "ne":
        volba9 = input("chceš vrátit obušek strážnému? ")
        if volba9 == "ano":
            print("vrátil jsi obušek strážnému")
            vecistrazneho()
        elif volba9 == "ne":
            obusek()
        else:
            odznova()


def penezenka():
    print("vzal sis do ruky peněženku")
    volba10 = input("chceš jí otevřít a podívat se co je uvnitř? ")
    if volba10 == "ano":
        global penezenka1
        penezenka1 = penezenka1 + 1
        print(
            "otevíráš peněženku a vidíš že v ní jsou dvě tisícovky a čtenářský průkaz s půjčenou knihou Stopařův průvodce Galaxií")
        volba11 = input("chceš si nechat peněženku ")
        if volba11 == "ano":
            penezenka1 = penezenka1 + 1
            print("nechal sis peněženku")
            vecistrazneho()
        elif volba11 == "ne":
            vecistrazneho()
        else:
            odznova()
            penezenka()
    elif volba10 == "ne":
        volba9 = input("chceš vrátit penezenku strážnému? ")
        if volba9 == "ano":
            print("vrátil jsi penezenku strážnému")
            vecistrazneho()
        if volba9 == "ne":
            penezenka()
        else:
            odznova()
            penezenka()

    else:
        odznova()
        penezenka()


def zamcenedvere():
    print(
        "přišel jsi ke dveřím \n"
        "zadej 1 jestli si chceš prohlédnout dveře \n"
        "zadej 2 jestli se chceš pokusit otevřít dveře \n"
        "zadej 3 jestli se chceš vrátit k tělu strážneho")
    volba2 = int(input("co budeš dělat "))
    carecky()
    if volba2 == 1:
        print("díváš se na dveře jsou z pevného dubového dřeva a se zámkem vyrážet je nemá smysl")
        dvere3()
    elif volba2 == 2:
        print("jsou zamčené")
    elif volba2 == 3:
        pseudostrazny()
        zamcenedvere()
    else:
        odznova()
        zamcenedvere()


def otevrenedvere():
    print(
        "přišel jsi ke dveřím \n"
        "zadej 1 jestli si chceš prohlédnout dveře \n"
        "zadej 2 jestli se chceš pokusit otevřít dveře \n")
    volba2 = int(input("co budeš dělat "))
    if volba2 == 1:
        print("díváš se na dveře a vypadají jako normální dřevěné dveře")
        otevrenedvere()
    elif volba2 == 2:
        print("tlačíš na kliku a otevíráš dveře ")
        novedvere()
    else:
        odznova()
        dvere1()


def nigi1():
    print("před sebou vidíš micolase toho který může za to že ses tu ocitl")
    if pocetobleceni == 1:
        print(
            "micolas říka: hej Bedřichu vrať se do práce musíš hlídat novou oběť jinak může utéci ty staré dveře se dají lehce zničit")
        print("micolas rika no dobrá ja je pohlídám ty zstím jdi na lov\n"
              "micolas tě vyhání ven a jsi volný")
        vyhra()
    else:
        print("micolas říká: hej ty tady nemáš bejt ")
        volba12 = int(input("zadej 1 jestli chceš bojovat s nigim\n"
                            "zadej 2 jestli chceš utéct "))
        if volba12 == 1:
            bojsnigim()
        if volba12 == 2:
            print("otáčíš se a už jsi chtěl utéci ale nigi tě dohání a usínáš do věčného spánku ")
            prohra()
        else:
            odznova()
            nigi1()


def bojsnigim():
    if obusek1 == 1:
        print("Vytahuješ si obušek a připravuješ se k boji micolas však taky")
        bojsnigim2()
    else:
        print("Připravuješ se k boji micolas však taky")
        bojsnigim2()


def bojsnigim2():
    print("zadej 1 jestli chceš jít do útoku  \n"
          "zadej 2 jestli se chceš bránit  \n"
          "zadej 3 jestli se chceš vzdát \n")

    volba13 = int(input("co toho chceš dělat ?"))

    if volba13 == 1:
        print("bleskově jdeš do útoku nikolas se snažil bránit ale ty jsi ho přenou ránou do zátylku dokonale omráčil ")
        carecky()
        vyhra()
        carecky()
    elif volba13 == 2:
        print("snažil ses bránit úderem opasku tě odzbrojuje a pěstí tě vypína")
        prohra()
    elif volba13 == 3:
        print("zvedáš ruce a nikolas tě vede zpátky do první místnosti")
        prohra()

    else:
        odznova()
        bojsnigim()


def vyhra():
    print("Před sebou vidíš dveře ven otevíráš je vycházíš ven a dál žiješ svůj normální život ")
    carecky()
    print("vyhral jsi")
    carecky()


def novedvere():
    print(
        "oteviraš dveře a před sebou visíš prázdnou místnost nalevo a napravo jsou dveře v pravým rohu stojí skřínˇ a jinak je místnost zdánlivě prázna ")
    int(input("zadej 1 jestli se chceš podívat na dveře ktere jsou napravo\n"
              "zadej 2 jestli se chceš podívat na dveře ktere jsou nalevo \n"
              "zadej 3 jestli se chceš podívat ke skříni\n"
              "zadej 4 jestli se chceš pečlivě podívat okolo sebe \n"
              "zadej 5 jestli se chceš vráti zpátky do místnosti se stržážným\n"))
    volba14 = int(input("co budeš dělat dál?"))
    if volba14 == 1:
        dvere5()
    elif volba14 == 2:
        dvere6()
    elif volba14 == 3:
        skrin()
    elif volba14 == 4:
        ventilace1()
    elif volba14 == 5:
        print("vracíš se do místnosti se strážným")
        pseudostrazny()
    else:
        odznova()
        novedvere()


def dvere5():
    print("přišel jsi ke dveřím \n"
          "zadej 1 jestli si chceš prohlédnout dveře \n"
          "zadej 2 jestli se chceš pokusit otevřít dveře \n"
          "zadej 3 jestli nechceš být u dveří")
    volba17 = int(input("co budeš dělat "))
    if volba17 == 1:
        print("díváš se na dveře a vypadají jako normální dřevěné dveře")

    elif volba17 == 2:
        print("tlačíš na kliku ale jsou zavřene ")
        dvere5()
    elif volba17 == 3:
        print("jdeš zpátky")
        novedvere()

    else:
        odznova()
        dvere5()


def dvere6():
    print("přišel jsi ke dveřím \n"
          "zadej 1 jestli si chceš prohlédnout dveře \n"
          "zadej 2 jestli se chceš pokusit otevřít dveře \n"
          "zadej 3 jestli nechceš být u dveří")
    volba2 = int(input("co budeš dělat "))
    if volba2 == 1:
        print("díváš se na dveře a vypadají jako normální dřevěné dveře")
        dvere6()
    elif volba2 == 2:
        print("tlačíš na kliku a otevíráš dveře")
        mistnost3()
    elif volba2 == 3:
        novedvere()
    else:
        odznova()
        dvere6()


def skrin():
    print("přišel jsi ke skříní")


def ventilace1():
    print("")


def mistnost3():
    print("Otevíráš dveře a vidíš nejakeho muže v poutech v puse má roubík a něco nesrozumitelně mumlá \n"
          "zadej 1 jestli si chceš prohlédnout malakova pouta \n"
          "zadej 2 jestli se chceš pokusit osvobodit malaka \n"
          "zadej 3 jestli nechceš být u něho \n"
          "zadej 4 jestli si chceš prohlednout jeho místnost \n"
          "zadej 5 jestli si s ním chceš popovídat")
    volba2 = int(input("co budeš dělat "))
    if volba2 == 1:
        print("díváš se na pouta a vypadají docela pevně je na nich pevný železný zámek")
        mistnost3()
    elif volba2 == 2:
        print("snažíš se rozbít pouta ale marně")
        mistnost3()
    elif volba2 == 3:
        if lama0
        print("odcházíš z místnosti a slyšíš za sebou smutný výkřik")
        novedvere()
    elif volba2 == 4:
        print("díváš se okolo a vidíš na stěnách naškrábané: MHD, trAmVAjE, VlAkY Koloje")
        mistnost3()
    elif volba2 == 5:
        if zivotylamaka == 0:
            print("je mrtvý")
            mistnost3()
        else:
            if lamakuvroubik == 0:
                volba17 = int(input("chceš mu sundat roubík"))
                if volba17 == "ano":
                    print("sundáváš mu roubik")

                    povidanislamakem()
                elif volba17 == "ne":
                    povidanislamakem()
            elif lamakuvroubik == 1:
                povidanislamakem()

    else:
        odznova()
        mistnost3()


def povidanislamakem():
    print("zadej 1 jestli se ho chceš zeptat na jméno\n"
          "zadej 2 jestli se ho chceš zeptat co tady dělat\n"
          "zadej 3 jestli si už s nim nechceš povídat\n"
          "zadej 4 jestli ho chceš udeřit"
          "zadej 5 jestli mu chceš dát roubík\n")
    volba18 = int(input("co budeš dělat"))
    if volba18 == 1:
        if lamakuvroubik == 1:
            print("odpovida ze se jmenuje lamak")
            povidanislamakem()
        else:
            print("...")

    elif volba18 == 2:
        if lamakuvroubik == 1:
            print("odpovida ze se jmenuje lamak")
            povidanislamakem()
        else:
            print("...")
    elif volba18 == 3:

    elif volba18 == 4:
    elif volba18 ==  5:

    else:
        odznova()
        povidanislamakem()


start()
