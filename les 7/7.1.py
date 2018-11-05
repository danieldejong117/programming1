def convert(tempC):
    temp = tempC*1.8+ 32
    return temp

header=( "{:>4} {:>7}".format('f','C'))
print(header)

def table():
    celsius= range(-30, 41, 10)
    for c in celsius:
        f = convert(c)
        text = "{:>6} {:>7}".format(f,float(c))
        print(text)
table()

