from random import choice


def signal_gen(amount):
    letters = "abcdefgh"
    string = []
    signal = []
    while amount > 0:
        string.append(choice(letters))
        amount -= 1
    for letter in string:
        if letter == "a":
            signal.append([0, 0, 0])
        elif letter == "b":
            signal.append([1, 0, 0])
        elif letter == "c":
            signal.append([0, 1, 0])
        elif letter == "d":
            signal.append([1, 1, 0])
        elif letter == "e":
            signal.append([0, 0, 1])
        elif letter == "f":
            signal.append([1, 0, 1])
        elif letter == "g":
            signal.append([0, 1, 1])
        elif letter == "h":
            signal.append([1, 1, 1])
        else:
            print "Wrong letter!"
            signal.append([-1, -1, -1])
    return signal
