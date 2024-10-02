import numpy as np  # type: ignore
import matplotlib.pyplot as plt  # type: ignore

t = np.array([5, 7, 10, 15, 20, 25, 30, 28, 22, 15, 10, 5])
months = np.arange(1, 13)

plt.scatter(months, t, c=t, cmap='coolwarm')
plt.colorbar(label='Temperature (°C)')
plt.plot(months, t, color='gray')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.title('Average Monthly Temperatures')
plt.savefig('temperature_variation.png')
# plt.show()
