
def risunelio(height):
    times = height

    while times != 0:
    
        if times == height or times < height:
            print("#" * height)
            times -= 1

risunelio(3)
print()
risunelio(5)