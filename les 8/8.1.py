def seizoen(maand):
    if maand == 12 or maand == 1 or maand == 2:
        seizoen ='het seizoen is winter'
    elif maand == 3 or maand == 4 or maand == 5:
        seizoen ='het seizoen is lente'
    elif  maand == 6 or maand == 7 or maand == 8:
        seizoen ='het seizoen is zomer'
    elif maand == 9 or maand == 10 or maand == 11:
        seizoen ='het seizoen is herfst'
    else:
        seizoen ='incorrect'
    return seizoen

maand = eval(input('geef de nummer van een maand: '))
seizoen(maand)
print('{}.'.format(seizoen(maand)))

