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
        print("Väärin")
    else:
        if yritykset > 1:
            #Tässä printataan teksti ja yritysten määrä.       
            print("Oikein, tarvitsit " + str(yritykset) + " yritystä")
            #Tämä lopettaa while-silmukan
            break
        else: 
            print("Oikein, tarvitsit yhden yrityksen")
            break
