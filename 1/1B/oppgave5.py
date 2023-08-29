tall = float(input("Skriv inn en temperatur: "))
enhet = input("Er dette i Celsius eller Fahrenheit? ")
if enhet == "C":
    print(tall, "grader Celsius tilsvarer", tall*9/5+32, "grader Fahrenheit")
elif enhet == "F":
    print(tall, "grader Fahrenheit tilsvarer", (tall-32)*5/9, "grader Celsius")