minutter = int(input("Skriv inn antall minutter: "))
timer = minutter // 60
minutter = minutter % 60
print("Det er", timer, "timer og", minutter, "minutter")