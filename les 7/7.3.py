def aantal_regels(file):
    f = open(file, "r")
    data = f.read()
    regels = len(data.splitlines())
    print('deze files telt', regels, 'regels')


def grootste_getal(file):
    f = open(file, "r")
    aantal_regels = 0
    mijn_lijst = []
    for regel in f:
        aantal_regels += 1
        lst = regel.split(",")
        kaartnummer = lst[0]
        naam = lst[1]
        mijn_lijst.append(lst[0])
        new = mijn_lijst.index(max(mijn_lijst))+1
    print('het grootste kaartnummer is:',max(mijn_lijst), "en dat staat op regel", new)

aantal_regels('kaartnummer')
grootste_getal('kaartnummer')




