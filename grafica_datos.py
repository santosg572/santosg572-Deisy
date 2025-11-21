import sys
import pandas as pd
import matplotlib.pyplot as plt

file = '31-1.csv'

file = sys.argv[1]

import pandas as pd

# Assuming 'data.csv' is in the same directory as your script
df = pd.read_csv(file)

# Display the first few rows of the DataFrame to verify
print(df.keys())

nombres = df.keys()

x = df[nombres[0]]

x = x[1:]

y = df[nombres[1]]

y = y[1:]

xx = [float(s) for s in x]
yy = [float(s) for s in y]

plt.plot(xx,yy)
plt.show()



