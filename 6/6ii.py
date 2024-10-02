# type: ignore
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

lst = ['London', 'New York', 'Tokyo', 'Sydney', 'Cairo']
df = pd.DataFrame(lst, columns=['City'])

fig, ax = plt.subplots(figsize=(8, 6))
m = Basemap(projection='cyl', llcrnrlat=-60, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, ax=ax)
m.drawcoastlines()

cities = {'London': (51.5074, -0.1278), 'New York': (40.7128, -74.0060), 
          'Tokyo': (35.6762, 139.6503), 'Sydney': (-33.8688, 151.2093), 
          'Cairo': (30.0444, 31.2357)}

for city, coord in cities.items():
    x, y = m(coord[1], coord[0])
    m.plot(x, y, 'ro')
    plt.text(x, y, city, fontsize=12)

plt.savefig('cities_plot.png')
# plt.show()