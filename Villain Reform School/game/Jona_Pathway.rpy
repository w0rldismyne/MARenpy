label JonaVisit:

    if jTurn == 0:
        jump Jona1
    elif jTurn == 1:
        jump Jona2
    elif jTurn == 2:
        jump Jona3
    elif jTurn == 3:
        jump Jona4
    else:
        jump JonaF

label Jona1:

label Jona2:

label Jona3:

label Jona4:

label JonaF:
    scene backgroundfield

    return