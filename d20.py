import random


def hodk20():
    return random.randint(1, 20)


def main():
    print("hod kostkou ")
    print("snažís se posunot skřín to vyžaduje hod na sílu\nzadej k jestli chceš uskutečnit hod")
    while True:
        input("zmáčkni enter pro hod")
        hod = hodk20()
        print(f"hodil jsi: {hod}+3(tvoje síla) = {hod + 3}")
        if hod >= 10:
            print("super uspěšně jsi posunul skřín")
            global skrin
            skrin = skrin - 1
        else:
            print("mas smulu")

main()
