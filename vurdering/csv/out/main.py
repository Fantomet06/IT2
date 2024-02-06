import csv
import re
import numpy as np
import matplotlib.pyplot as plt

def plot(data, show=None, savename=""):
    f = plt.subplots()

    for y in range(1, len(data)):
        if show != None:
            if data[y][0] in show:
                plt.plot(data[0][1:], data[y][1:], label=data[y][0])
        else: 
            plt.plot(data[0][1:], data[y][1:], label=data[y][0])

    plt.title("Mediebruk i Norge 2010-2019")
    plt.xlabel("År")
    plt.ylabel("Antall minutter (gjennomsnitt per dag)")

    plt.legend()

    if len(savename) > 0:
        plt.savefig(f'./plots/{savename}.png')

    return f
    

def find_max_min(data, name):
    for check in data: # for hver rad
        if check[0] == name: # sjekk om første element i raden er lik name
            maks = max(check[1:])
            minimum = min(check[1:])
            print(f"Max er {maks}")
            print(f"Min er {minimum}")
            break
    

def fix_data(data):
    # fjerne de to tulle radene
    data = data[2:]

    # fixe . og .. til np.NaN og årstall
    for i in range(1, len(data)): # for hver rad
        data[0][i-1] = re.sub(r'[a-zA-Z ]', '', data[0][i-1])
        for j in range(1, len(data[i])): # for hver verdi i hver rad                
            #søk etter . med regex - dekker . og ..
            if re.search(r'[.]', data[i][j]): 
                data[i][j] = np.NaN
            else: 
                data[i][j] = int(data[i][j])
    
    return data


def main(datasett):
    with open(datasett, 'r', encoding="utf-8-sig") as f:
        fil = csv.reader(f, delimiter=';')
        data = []
        for row in fil:
            data.append(row)

    
    data = fix_data(data) #fikser dataen :)

    plot(data) #vis alle plots
    plot(data, show=["Hjemme-PC", "Bøker", "Internett"], savename="oppgaveB")
    plt.show()

    find_max_min(data, "Internett")

if __name__ == '__main__':
    datasett = './datasett/Medier.csv'
    main(datasett)