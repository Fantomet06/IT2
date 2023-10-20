def oppskrift_fra_sukker(sukker: float) -> dict:
    return {"sukker": sukker, "mel": sukker*2, "smør": sukker*3}

def oppskrift_fra_mel(mel: float) -> dict:
    return {"sukker": mel/2, "mel": mel, "smør": mel*1.5}

def oppskrift_fra_smøoer(smoer: float) -> dict:
    return {"sukker": smoer/3, "mel": smoer/2, "smør": smoer}

def skriv_oppskrift(sukker: float, mel: float, smør: float) -> None:
    print("\nOppskrift på kaker:")
    print("Du trenger: ")
    print(f"{sukker}g sukker:")
    print(f"{mel}g mel")
    print(f"{smør}g smør")

def _input(prompt: str):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Skriv inn et tall")

def bak_kaker():
    while True:
        try:
            a = str(input("Hva har du vil du basere oppskrift av? (sukker, mel, smoer) ")).lower()
            break
        except:
            print("Skriv inn sukker, mel eller smoer")

    if (a == "sukker"):
        sukker = _input("Hvor mye sukker har du? ")
        oppskrift_fra_sukker(sukker)
        skriv_oppskrift(**oppskrift_fra_sukker(sukker))
    elif (a == "mel"):
        mel =  _input("Hvor mye mel har du? ")
        oppskrift_fra_mel(mel)
        skriv_oppskrift(**oppskrift_fra_mel(mel))
    elif (a == "smoer"):
        smoer = _input("Hvor mye smør har du? ")
        oppskrift_fra_smøoer(smoer)
        skriv_oppskrift(**oppskrift_fra_smøoer(smoer))

bak_kaker()