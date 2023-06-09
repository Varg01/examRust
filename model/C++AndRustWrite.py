import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data_cpp = {'sizes(amount of numbers)': [10000, 100000, 1000000, 5000000, 10000000, 50000000, 100000000, 1000000000],
        'times(ms)': [0.38, 0.40, 1.04, 7.39, 20.88, 71.26, 764.94, 7799.02]}
df_full_cpp = pd.DataFrame(data_cpp)

data_rust = {'sizes(amount of numbers)': [10000, 100000, 1000000, 5000000, 10000000, 50000000, 100000000, 1000000000],
        'times(ms)': [0.28, 0.88, 8.16, 20.79, 83.18, 305.57, 592.73, 5881.87]}
df_full_rust = pd.DataFrame(data_rust)

data_cpp = {'sizes(amount of numbers)': [10000, 100000, 1000000, 5000000, 10000000, 50000000, 100000000],
        'times(ms)': [0.38, 0.40, 1.04, 7.39, 20.88, 71.26, 764.94]}
df_cpp = pd.DataFrame(data_cpp)

data_rust = {'sizes(amount of numbers)': [10000, 100000, 1000000, 5000000, 10000000, 50000000, 100000000],
        'times(ms)': [0.28, 0.88, 8.16, 20.79, 83.18, 305.57, 592.73]}
df_rust = pd.DataFrame(data_rust)


X_cpp = df_cpp[['sizes(amount of numbers)']]
y_cpp = df_cpp['times(ms)']
model_cpp = LinearRegression().fit(X_cpp, y_cpp)

X_rust = df_rust[['sizes(amount of numbers)']]
y_rust = df_rust['times(ms)']
model_rust = LinearRegression().fit(X_rust, y_rust)

new_size = [[1000000000]]
predicted_time_cpp = model_cpp.predict(new_size)
predicted_time_rust = model_rust.predict(new_size)

df_predicted_cpp = pd.DataFrame({'sizes(amount of numbers)': new_size[0], 'times(ms)': predicted_time_cpp})
df_predicted_rust = pd.DataFrame({'sizes(amount of numbers)': new_size[0], 'times(ms)': predicted_time_rust})
df_combined = pd.concat([df_cpp, df_predicted_cpp, df_rust, df_predicted_rust]).sort_values(by='sizes(amount of numbers)')


plt.scatter(df_combined['sizes(amount of numbers)'], df_combined['times(ms)'])
plt.plot(df_combined['sizes(amount of numbers)'], model_cpp.predict(df_combined[['sizes(amount of numbers)']]), color='red', label='C++')
plt.plot(df_combined['sizes(amount of numbers)'], model_rust.predict(df_combined[['sizes(amount of numbers)']]), color='blue', label='Rust')
plt.xlabel('sizes(amount of numbers)')
plt.ylabel('times(ms)')


plt.scatter(1000000000, 7799.02, color='darkred', s=25, label='C++ 1000000000')
plt.scatter(1000000000, 5881.87, color='darkblue', s=25, label='Rust 1000000000')
plt.plot(df_full_cpp['sizes(amount of numbers)'], df_full_cpp['times(ms)'], color='red', linestyle='dashed', alpha=0.5, label='C++ approx line')
plt.plot(df_full_rust['sizes(amount of numbers)'], df_full_rust['times(ms)'], color='blue', linestyle='dashed', alpha=0.5, label='Rust approx line')


plt.title('Comparison of C++ and Rust Write Regression Models for Time vs. Size')

# Add the predicted values to the plot
plt.scatter(df_predicted_cpp['sizes(amount of numbers)'], df_predicted_cpp['times(ms)'], color='green', label=f'C++:{predicted_time_cpp[0]:.2f}', s=25)
plt.scatter(df_predicted_rust['sizes(amount of numbers)'], df_predicted_rust['times(ms)'], color='purple', label=f'Rust:{predicted_time_rust[0]:.2f}', s=25)


equation_cpp = f'y = {model_cpp.intercept_:.2f} + {model_cpp.coef_[0]:.10f}x'
plt.text(0.4, 0.95, equation_cpp, transform=plt.gca().transAxes, color='red')

equation_rust = f'y = {model_rust.intercept_:.2f} + {model_rust.coef_[0]:.10f}x'
plt.text(0.4, 0.85, equation_rust, transform=plt.gca().transAxes, color='blue')


plt.legend()
plt.savefig('WriteComparison.png')
plt.show()