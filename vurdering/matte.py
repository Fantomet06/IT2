import numpy as np

def rettvinklet(x1, y1, x2, y2):
    vektor1 = np.array([x1, y1])
    vektor2 = np.array([x2, y2])

    if np.dot(vektor1,vektor2) == 0:
        kat1 = np.sqrt(vektor1[0]**2 + vektor1[1]**2)
        kat2 = np.sqrt(vektor2[0]**2 + vektor2[1]**2)
        hypotenus = np.sqrt(kat1**2 + kat2**2)
        return f"Trekanten er rettvinklet med omkrets {kat1 + kat2 + hypotenus} og areal {kat1*kat2/2}"
    else:
        return "Trekanten er ikke rettvinklet"

def main():
    x1, y1 = input("Skriv inn vektor 1 (x1,y1): ").split(",")
    x2, y2 = input("Skriv inn vektor 2 (x2,y2): ").split(",")
    print(rettvinklet(int(x1), int(y1), int(x2), int(y2)))

if __name__ == "__main__":
    main()