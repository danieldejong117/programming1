def standaardprijs(afstandKM):
    if afstandKM < 0:
        return 0
    elif afstandKM > 50:
        prijs = 15 + (afstandKM * 0.60)
    else:
        prijs = afstandKM * 0.80
        return prijs
def bepaal_weekend(dag):
    if dag == "zaterdag" or dag == "zondag":
        return True
    else:
        return False

def ritprijs(leeftijd, weekend, afstandKM):
    if leeftijd < 12 or leeftijd >= 65:
        if weekend:
            korting = 0.35
        else:
            korting = 0.30
    else:
        if weekend:
            korting = 0.40
        else:
            korting = 0.0
    prijs = (1 - korting) * standaardprijs(afstand)
    return prijs


afstand = eval(input("hoeveel km gaat u reizen: "))
dag = input("welke dag gaat u reizen?: ")
leeftijd = int(input ("wat is uw leeftijd?: "))

weekend = bepaal_weekend(dag)
prijs = standaardprijs(afstand)
nieuweprijs = ritprijs(leeftijd, weekend, prijs)

print (nieuweprijs)