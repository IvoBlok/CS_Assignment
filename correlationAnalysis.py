import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('istherecorrelation.csv', delimiter=';', dtype=None)
data = data[1:] # remove header 
data = np.strings.replace(data, ',', '.')

years = data[:,0].astype(float)
WO = data[:,1].astype(float)
beer_consumption = data[:,2].astype(float)

fig, ax1 = plt.subplots()

ax1_color = 'red'
ax2_color = 'blue'

ax1.set_xlabel('year')
ax1.set_ylabel('WO x 1000', color=ax1_color)
ax1.plot(years, WO, 'o', color=ax1_color)
ax1.tick_params(axis='y')

ax2 = ax1.twinx()

ax2.set_ylabel('beer consumption', color=ax2_color)
ax2.plot(years, beer_consumption, 'o', color=ax2_color)
ax2.tick_params(axis='y')

fig.tight_layout()
plt.show()