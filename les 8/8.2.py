lijst = (input("Geef lijst met minimaal 10 strings: "))

outfile = open("woorden.txt", "w")
outfile.write(lijst)
outfile.close()
infile = open("woorden.txt", 'r')
regel = infile.readlines()
letters =''

for words in regel:
    woorden = words.split("\", \"")
    outfile = open("strings.txt", 'a')
    outfile.write('De nieuw-gemaakte lijst met alle vier-letter strings is: ')
    for woord in woorden:
        if len(woord) == 4:
            outfile.write('\''+woord+'\',')
outfile.close()