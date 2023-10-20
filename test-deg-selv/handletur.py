prisListe = [
    {"Butikk" : "Rema1000", "salat" : 12, "fisk" : 99, "melk" : 12, "brod" :12},
    {"Butikk" : "Meny", "salat" : 22, "fisk" : 60, "melk" : 18, "brod" :21},
    {"Butikk" : "Kiwi", "salat" : 8, "fisk" : 120, "melk" : 10, "brod" :19},
    {"Butikk" : "Spar", "salat" : 18, "fisk" : 40, "melk" : 30, "brod" :59},
    {"Butikk" : "Joker", "salat" : 15, "fisk" : 200, "melk" : 40, "brod" :9},
]

def finnButikk(mat: list, prisListe: dict) -> str:
    samlet_pris = []
    for i in mat:
        count = 0
        for j in range(len(prisListe)):
            try:
                samlet_pris[count] += prisListe[j][i]
            except:
                samlet_pris.append(prisListe[j][i])
            
            count += 1

    return prisListe[samlet_pris.index(min(samlet_pris))]["Butikk"]

print(finnButikk(["salat", "fisk"], prisListe))
