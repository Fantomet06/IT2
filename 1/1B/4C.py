for i in range(3):
    tall = int(input("Skriv inn et tall: "))
    if i == 0:
        storst = tall
    elif tall > storst:
        storst = tall

print("Det største tallet er", storst)