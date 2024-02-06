import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("./datasett/Medier.csv", index_col = 0, skiprows = (0, 1), \
sep =";", na_values=[".", ".."], encoding = "utf-8-sig")

data.columns = range(2010,2020)

data = data.transpose()
data.plot().legend(bbox_to_anchor = (1, 1))

print(data.describe())

plt.xlabel("Årstall")
plt.ylabel("Minutter per dag i gjennomsnitt")
plt.title("Tid brukt på ulike medier 2010–2019")
plt.suptitle("Kilde: Statistisk sentralbyrå", fontsize = 8)
plt.grid(True)
plt.show()