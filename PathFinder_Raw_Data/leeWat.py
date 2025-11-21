import pandas as pd

file = "Watermaze_output/31-1.csv"

datos = pd.read_csv(file)

hh = datos.keys()


ncol = 54

i = 10

k = 3*i

dd = datos[[hh[k],hh[k+1],hh[k+2]]]

print(hh[k])

dd.to_csv('prueba.csv', index=False)

