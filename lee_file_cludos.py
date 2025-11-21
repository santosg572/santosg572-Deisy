
import pandas as pd
 
file='PathFinder_Raw_Data/Watermaze_output/31-1.csv'

def sacaCol(i=0, dd=0):
  j = 3*i
  return (dd[j], dd[j+1], dd[j+2])



fil = open(file, 'r')

datos = fil.readlines()

nfil = len(datos)

dd = datos[0]

dd = dd.split(',')

nc = 54

k = 0

ll = list()
for i in range(nfil):
  dd = datos[i]
  dd = dd.split(',')
  rr = sacaCol(k, dd)
  ll.append(rr)

file = 'salida.csv'

filo = open(file,'w')
for ss in ll:
  filo.write(ss)

filo.close()


 
