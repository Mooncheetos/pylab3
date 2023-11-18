import numpy as np
import matplotlib.pyplot as plt


def lag_lab5(x, y, q):
    g = 0
    for j in range(len(y)):
        d1 = 1
        d2 = 1
        for i in range(len(x)):
            if i == j:
                d1 = d1 * 1
                d2 = d2 * 1
            else:
                d1 = d1 * (q - x[i])
                d2 = d2 * (x[j] - x[i])
        g = g + y[j] * d1 / d2
    return g


x = np.array([11, 13, 15, 17, 20, 22], dtype=float)
y = np.array([42.26, 35.39, 29.88, 16.97, 6.05, 4.21], dtype=float)

xnew = np.linspace(np.min(x), np.max(x), 100)
ynew = [lag_lab5(x, y, i) for i in xnew]
print("g=", lag_lab5(x, y, 12))
print("g=", lag_lab5(x, y, 14))
print("g=", lag_lab5(x, y, 19))

plt.plot(x, y, "o", color="b", label="table")
plt.plot(xnew, ynew, color="g", label="lagrang")
plt.grid()
plt.rc("font", size=12)
plt.legend(fontsize=10)
plt.show()
