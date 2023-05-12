import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x_full = np.array([250, 375, 500, 750, 1000, 1250, 1500, 1750, 2000])
y_cpp_full = np.array([6.51, 27.87, 67.06, 249.80, 596.62, 1260.32, 2464.66, 5994.50, 18814.77])
y_rust_full = np.array([9.35, 34.46, 79.65, 302.91, 846.03, 2590.23, 4606.82, 11030.09, 24203.58])


x = np.array([250, 375, 500, 750, 1000, 1250, 1500, 1750])
y_cpp = np.array([6.51, 27.87, 67.06, 249.80, 596.62, 1260.32, 2464.66, 5994.50])
y_rust = np.array([9.35, 34.46, 79.65, 302.91, 846.03, 2590.23, 4606.82, 11030.09])

def exponential_func(x, a, b, c):
    return a * np.exp(b * x) + c

bounds = ([0, -np.inf, -np.inf], [3000, np.inf, np.inf])
p0 = [1, 0.001, 1]

popt_cpp, _ = curve_fit(exponential_func, x, y_cpp, p0=p0, bounds=bounds)
popt_rust, _ = curve_fit(exponential_func, x, y_rust, p0=p0, bounds=bounds)

x_pred = 2000
y_pred_cpp = exponential_func(x_pred, *popt_cpp)
y_pred_rust = exponential_func(x_pred, *popt_rust)

x_smooth = np.linspace(x[0], x[-1], 2000)
y_smooth_cpp = exponential_func(x_smooth, *popt_cpp)
y_smooth_rust = exponential_func(x_smooth, *popt_rust)

x_ext = np.linspace(x[-1], x_pred, 100)
y_ext_cpp = exponential_func(x_ext, *popt_cpp)
y_ext_rust = exponential_func(x_ext, *popt_rust)

x_smooth = np.concatenate((x_smooth, x_ext))
y_smooth_cpp = np.concatenate((y_smooth_cpp, y_ext_cpp))
y_smooth_rust = np.concatenate((y_smooth_rust, y_ext_rust))

plt.plot(x_smooth, y_smooth_cpp, color='red')
plt.plot(x_smooth, y_smooth_rust, color='blue')

plt.scatter(x, y_cpp, label='C++', color='red')
plt.scatter(x, y_rust, label='Rust', color='blue')
plt.scatter(x_pred, y_pred_cpp, color='green', label=f'C++ prediction: {y_pred_cpp:.2f}', s=25)
plt.scatter(x_pred, y_pred_rust, color='purple', label=f'Rust prediction: {y_pred_rust:.2f}', s=25)

plt.scatter(2000, 18814.77, color='darkblue', s=25, label='C++ 2000')
plt.scatter(2000, 24203.58, color='darkred', s=25, label='Rust 2000')
plt.plot(x_full, y_cpp_full, color='red', linestyle='dashed', alpha=0.5, label='C++ approx line')
plt.plot(x_full, y_rust_full, color='blue', linestyle='dashed', alpha=0.5, label='Rust approx line')



plt.title('Comparison of C++ and Rust Matrix multiplication Regression Models for Time vs. Size', fontsize=10)

plt.text(1000, 10000, f' C++ fit: y={popt_cpp[0]:.2f}*exp({popt_cpp[1]:.4f}*x)+{popt_cpp[2]:.2f}', ha='center', color='red')
plt.text(1000, 8000, f' Rust fit: y={popt_rust[0]:.2f}*exp({popt_rust[1]:.4f}*x)+{popt_rust[2]:.2f}', ha='center', color='blue')



plt.xlabel('size')
plt.ylabel('time')
plt.legend()
plt.savefig('MatrixComparison.png')
plt.show()
