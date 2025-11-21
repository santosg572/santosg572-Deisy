import pandas as pd
 
file='PathFinder_Raw_Data/Watermaze_output/31-1.csv'

df = pd.read_csv(file)

key = df.keys()

for i in range(55):
  k = 3*i
  nom1 = key[k]
  nom2 = key[k+1]
  nom3 = key[k+2]
  datos = df[[nom1, nom2, nom3]]
  print(datos)
  datos.to_csv(nom1+'.csv', index=False)




