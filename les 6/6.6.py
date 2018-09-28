def wijzig(lijst):
    lijst.remove('a')
    lijst.remove('b')
    lijst.remove('c')
    lijst.append('d')
    lijst.append('e')
    lijst.append('f')
    lijst[0]='d'
    lijst[1]= 'e'
    lijst[2]= 'f'
lijst= ['a', 'b', 'c']
print(lijst)
wijzig(lijst)
print(lijst)