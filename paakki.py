height = int(input("Määritä korkeus: "))
length = int(input("Määritä leveys: "))

times = height

while times != 0:
 
    if times == height or times < height:
        print("#" * length)
        times -= 1
        