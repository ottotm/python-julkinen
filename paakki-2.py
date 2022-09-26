while True:
    n = int(input("Anna luku: "))

    if n >  0:
        fact = 1
        
        for i in range(1,n+1):
            fact = fact * i
            
        print ("Luvun",n,"kertoma on ",end="")
        print (fact)
    else:
        print("Kiitos ja moi!")
        break
