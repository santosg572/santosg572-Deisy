import pandas as pd

file = "Watermaze_output/31-1.csv"

datos = pd.read_csv(file)

hh = datos.keys()


ncol = 54

i = 0

k = 3*i

dd = datos[[hh[0],hh[1],hh[2]]]

print(dd)

dd.to_csv('prueba.csv', index=False)

