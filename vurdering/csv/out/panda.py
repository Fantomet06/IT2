import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("./datasett/Medier.csv", index_col = 0, skiprows = (0, 1), \
sep =";", na_values=[".", ".."], encoding = "latin-1")

data.columns = range(2010,2020)

data = data.transpose()
data.plot().legend(bbox_to_anchor = (1, 1))

print(data.describe())

plt.show()