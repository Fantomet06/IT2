def input_tall(prompt: str) -> int:
    while True:
        try:
            out = int(input(prompt))
            return out
        except:
            print("Skriv inn et tall")

def input_streng(prompt: str) -> str:
    while True:
        try:
            out = str(input(prompt))
            return out
        except:
            print("Skriv inn en streng")

def find_person(personer: dict, forbokstav: str) -> dict:
    for i in personer:
        if (i["navn"][0] == forbokstav):
            print(i)

def legg_til_person(personer: dict):
    personer.append({"navn": input_streng("Skriv inn navn: "), "alder": input_tall("Skriv inn alder: ")})
    return personer

def main(personer):
    legger_til = True

    while legger_til != False:
        legg_til = input_streng("Vil du legge til en person? (j/n) ").lower()
        if legg_til == "j":
            personer = legg_til_person(personer)
        elif legg_til == "n":
            legger_til = False
        else:
            print("Skriv inn j eller n")

    print(personer)
    find_person(personer, input_streng("Skriv inn forbokstaven til navnet du vil finne: "))

if __name__ == "__main__":
    personer = []
    main(personer)