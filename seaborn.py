import pandas 

data = pandas.read_csv('polomki.csv', index_col='Magazine')

import seaborn

seaborn.heatmap(data)
