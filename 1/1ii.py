import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

sa = np.array([50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160])
sb = np.array([30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140])
ea = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75])
eb = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(sa, label='Product A Sales')
axs[0, 0].legend()

axs[0, 1].plot(sb, label='Product B Sales')
axs[0, 1].legend()

axs[1, 0].plot(ea, label='Product A Expenses')
axs[1, 0].legend()

plt.tight_layout()
plt.savefig('sales_expenses_subplot_fixed.png')
# plt.show()
