import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


x = np.array([250, 375, 500, 750, 1000, 1250, 1500, 1750])
y = np.array([6.51, 27.87, 67.06, 249.80, 596.62, 1260.32, 2464.66, 5994.50])


def exponential_func(x, a, b, c):
    return a * np.exp(b * x) + c


bounds = ([0, -np.inf, -np.inf], [3000, np.inf, np.inf])
p0 = [1, 0.001, 1]


popt, pcov = curve_fit(exponential_func, x, y, p0=p0, bounds=bounds)

# predict y for x=2000
x_pred = 2000
y_pred = exponential_func(x_pred, *popt)

plt.scatter(x_pred, y_pred, color='green')


x_smooth = np.linspace(x[0], x[-1], 2000)
y_smooth = exponential_func(x_smooth, *popt)


x_ext = np.linspace(x[-1], x_pred, 100)
y_ext = exponential_func(x_ext, *popt)
x_smooth = np.concatenate((x_smooth, x_ext))
y_smooth = np.concatenate((y_smooth, y_ext))

plt.scatter(x, y)
plt.plot(x_smooth, y_smooth, 'r-', label='fit')
plt.scatter(x_pred, y_pred, color='green', label=f'{y_pred:.2f}', s=25)
plt.title('C++ Matrix multiplication Regression Model for Time vs. Size')


eqn = f'y = {popt[0]:.2f} * exp({popt[1]:.4f} * x) + {popt[2]:.2f}'
plt.text(0.3, 0.9, eqn, transform=plt.gca().transAxes, color='red')


plt.xlabel('size')
plt.ylabel('time')
plt.legend()

plt.savefig('C++Matrix.png')



y_pred = exponential_func(x, *popt)
rss = np.sum((y - y_pred)**2)
mse = rss / (len(y) - 3)
approx_error = np.sqrt(mse)
print(f"Approximation error: {approx_error:.2f}")

plt.show()


