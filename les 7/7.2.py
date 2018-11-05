filename = 'kaartnummer'
file = open(filename, "r")
for line in file:
    lst = line.split(",")
    kaartnummer = lst[0]
    naam = lst[1]
    print('{} {} {}'.format(naam.strip(), 'heeft kaartnummer:', kaartnummer))