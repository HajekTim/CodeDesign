# Funktion
def quadrat(x):
    return x * x


# print(quadrat(8))

# scope bzw. wann auf eine Varibale zugegriffen werden kann
var_ausserhalb_funktion = "test"


def scope():
    var_in_function = "blabla"
    print(var_in_function)
    print(var_ausserhalb_funktion)


# print(var_in_function)


# if else
def vergleich_zu_5(x):
    if x > 5:
        print("x ist größer als 5")
    elif x == 5:
        print("x ist gleich 5")
    else:
        print("x is kleiner als 5")


def while_loop():
    i = 0
    while i < 6:
        print(i)
        i += 1


def while_loop_mit_break():
    i = 0
    while i < 6:
        i += 1
        if i == 3:
            break
        print(i)


def while_loop_mit_continue():
    i = 0
    while i < 6:
        i += 1
        if i == 3:
            break
        print(i)


def for_loop():
    fruechte = ["Apfel", "Banane", "Kirsche"]
    for frucht in fruechte:
        if frucht == "banana":
            continue
        print(frucht)
