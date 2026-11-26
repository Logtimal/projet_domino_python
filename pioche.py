def buildPioche():
    pioche = []
    for i in range(0, 7):
        for j in range(i, 7):
            pioche.append([i, j])
    return pioche