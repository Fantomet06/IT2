import matplotlib.pyplot as plt
import csv

with open("./3/3B/boliger.csv", encoding="utf-8-sig", mode="r") as f:
    statistikk = csv.reader(f, delimiter=";") 
    x, y = next(statistikk), next(statistikk) # linje 1 som liste

plt.xlabel(y.pop(0))
plt.ylabel(x.pop(0))

above_1000 = [int(y[i]) for i in range(len(y)) if len(x[i]) >= 11]
y = [int(y[i]) if int(y[i]) not in above_1000 else sum(above_1000) for i in range(len(y))]
x = [x[i] if len(x[i]) < 11 else "Over 1000m" for i in range(len(y))]

plt.title("Antall fritidsbygg gitt meter over havet")
plt.grid()
plt.barh(x, y)
plt.show()