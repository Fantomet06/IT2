krypter = {
    "a": "c",
    "b": "d",
    "c": "e",
    "d": "f",
    "e": "g",
    "f": "h",
    "g": "i",
    "h": "j",
    "i": "k",
    "j": "l",
    "k": "m",
    "l": "n",
    "m": "o",
    "n": "p",
    "o": "q",
    "p": "r",
    "q": "s",
    "r": "t",
    "s": "u",
    "t": "v",
    "u": "w",
    "v": "x",
    "w": "y",
    "x": "z",
    "y": "æ",
    "z": "ø",
    "æ": "å",
    "ø": "a",
    "å": "b",
}

# Kryptering
tekst = "Hei, dette er en skikkelig hemmelig tekst!"
nytekst = ""
for i in tekst:
    try:
        nytekst += krypter[i.lower()]
    except:
        nytekst += i

print(nytekst)

# Dekryptering
dekryptert_tekst = ""
for i in nytekst:
    try:
        dekryptert_tekst += [key for key, value in krypter.items() if value == i.lower()][0]
    except IndexError:
        dekryptert_tekst += i

print(dekryptert_tekst)