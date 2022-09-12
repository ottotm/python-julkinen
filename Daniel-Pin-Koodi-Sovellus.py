# Määritellään Pin-koodi
tunnus  = "4321"

#Pin-Koodi muutetaan int muuttujaksi, eli numeroksi.
tunnusMuuttuja = int(tunnus)

#yritysten määrä
yritykset = 1

while True:
    #Käyttäjä syöttää pin-koodin
    syotettyTunnus = int(input("Anna pinkoodi:"))

    #Ehtolause tarkistaa tunnuksen. Jos tunnus on väärä printtaa se tekstin ja lisää yritykset muuttujaan luvun. != tarkoittaa jos jokin ei ole sama.
    if syotettyTunnus != tunnusMuuttuja:
        yritykset += 1
        print("PIN-koodi: " + str(syotettyTunnus))
        print("Väärin")
    else:
        if yritykset > 1:
            #Tässä printataan teksti ja yritysten määrä.
            print("PIN-koodi: " + str(syotettyTunnus))
            print("Tunnus on oikein. Tarvitsit " + str(yritykset) + " yritystä")
            #Tämä lopettaa while-silmukan
            break
        else:
            print("PIN-koodi: " + str(syotettyTunnus))
            print("Oikein, tarvitsit yhden yrityksen")
            break