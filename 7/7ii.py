import numpy as np  # type: ignore
import matplotlib.pyplot as plt  # type: ignore

h = np.array([150, 160, 165, 170, 175, 180, 155, 165, 170, 175, 180, 190, 160, 165, 170, 175])

plt.hist(h, bins=5)
plt.xlabel('Height (cm)')
plt.ylabel('Frequency')
plt.title('Height Distribution of Clients')
plt.savefig('height_distribution_clients.png')
# plt.show()
