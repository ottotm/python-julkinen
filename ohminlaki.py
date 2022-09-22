a_list = [0, 0, 0]

ohmi = False
teho = False
def teholaskin():
    for index, integer in enumerate(a_list):
        if index == 0:
            teksti = "U"
        elif index == 1:
            teksti = "R"
        elif index == 2:
            teksti = "P"
        luku = int(input("Syötä "+teksti+": "))     
        if luku == 0:
            nolla = index
        a_list[index] += luku
        
    print(a_list)



def ohminlaskin():
    for index, integer in enumerate(a_list):
        if index == 0:
            teksti = "U"
        elif index == 1:
            teksti = "R"
        elif index == 2:
            teksti = "I"
        luku = int(input("Syötä "+teksti+": "))    
        if luku == 0:
            nolla = index
        a_list[index] += luku

    if nolla == 2:
        virta = a_list[0] / a_list[1]
        print("I on " + str(virta) + "A")
        
    elif nolla == 1:
        resistanssi = a_list[0] / a_list[2]
        print("R on " + str(resistanssi) + "Ω")  
    else:
        jannite = a_list[1] * a_list[2]
        print("U on " + str(jannite) + "V")


def maarita_laskin():
    laskin =  input("Laskin: ")
    if laskin == "ohminlaki":
        ohminlaskin()
    elif laskin == "teho":
        teholaskin()

while True:
    maarita_laskin()


