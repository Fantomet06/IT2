import csv
import re
import numpy as np
import matplotlib.pyplot as plt

def plot(data, show=None, savename=""):
    for y in range(1, len(data)):
        if show != None:
            if data[y][0] in show:
                plt.plot(data[0][1:], data[y][1:], label=data[y][0])
        else: 
            plt.plot(data[0][1:], data[y][1:], label=data[y][0])
        
    
    plt.title("Mediebruk i Norge 2010-2019")
    plt.xlabel("År")
    plt.ylabel("Antall minutter (gjenomsnitt per dag)")
    plt.legend()
    if len(savename) > 0: plt.savefig(f'./plots/{savename}.png')
    plt.show()
    

def find_max_min(data, name):
    for i in range(1, len(data)): # for hver rad
        if data[i][0] == name: # sjekk om første element i raden er lik name
            maks = max(data[i][1:])
            minimum = min(data[i][1:])
            print(f"Max er {maks}")
            print(f"Min er {minimum}")
    

def fix_data(data):
    # fjerne de to tulle radene
    for i in range(2): data.pop(0)

    # fixe . og .. til np.NaN og årstall
    for i in range(0, len(data)): # for hver rad
        for j in range(1, len(data[i])): # for hver verdi i hver rad

            if i == 0: #raden med årstall
                data[i][j] = re.sub(r'[a-zA-Z ]', '', data[i][j])

            else: #alle andre rader
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

    find_max_min(data, "Internett")

if __name__ == '__main__':
    datasett = './datasett/Medier.csv'
    main(datasett)