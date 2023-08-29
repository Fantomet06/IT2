while True:
    snitt = float(input("Skriv inn karaktersnittet ditt: "))
    if snitt < 0 or snitt > 6:
        print("Ugyldig snitt")
    else:
        print("Snittet ditt er", snitt)
        break
