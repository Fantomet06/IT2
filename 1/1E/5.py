# kilde https://no.wikipedia.org/wiki/Liste_over_land_etter_innbyggertall
statistikk = {
    "Kina": 1439324*1000,
    "India": 1380004*1000,
    "USA": 331002*1000,
    "Indonesia": 273524*1000,
    "Pakistan": 220892*1000,
}

# a)
for i in statistikk:
    print(f"{i}: {statistikk[i]}")

# b)
for i in statistikk:
    print(statistikk[i])

# c)
for i in statistikk:
    print(f"{i} har {statistikk[i]} innbyggere")

# d)
for i in sorted(statistikk.keys()):
    print(statistikk[i])

# e)
