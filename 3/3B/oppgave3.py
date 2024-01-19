import matplotlib.pyplot as plt
import csv

with open("./3/boliger.csv", encoding="utf-8-sig", mode="r") as f:
    statistikk = csv.reader(f, delimiter="	") # delimiter ble endra pga excel
    x = next(statistikk) # linje 1 som liste
    y = next(statistikk) # linje 2 som liste

tittel1 = str(x[0])
tittel2 = str(y[0])
x.pop(0)
y.pop(0)
y = [int(i) for i in y]
plt.barh(x, y)
plt.xlabel(tittel2)
plt.ylabel(tittel1)
plt.show()