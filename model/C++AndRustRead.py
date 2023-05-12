import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


data_cpp = {'Sizes': [10000, 100000, 1000000, 5000000, 10000000, 50000000, 100000000, 1000000000],
            'Times': [0.01, 0.02, 0.12, 1.02, 2.84, 8.54, 17.11, 172.36]}
df_full_cpp = pd.DataFrame(data_cpp)

data_rust = {'Sizes': [10000, 100000, 1000000, 5000000, 10000000, 50000000, 100000000, 1000000000],
             'Times': [0.01, 0.03, 0.31, 1.74, 2.92, 21.60, 41.56, 345.29]}
df_full_rust = pd.DataFrame(data_rust)

data_cpp = {'Sizes': [10000, 100000, 1000000, 5000000, 10000000, 50000000, 100000000],
            'Times': [0.01, 0.02, 0.12, 1.02, 2.84, 8.54, 17.11]}
df_cpp = pd.DataFrame(data_cpp)

data_rust = {'Sizes': [10000, 100000, 1000000, 5000000, 10000000, 50000000, 100000000],
             'Times': [0.01, 0.03, 0.31, 1.74, 2.92, 21.60, 41.56]}
df_rust = pd.DataFrame(data_rust)

X_cpp = df_cpp[['Sizes']]
y_cpp = df_cpp['Times']
model_cpp = LinearRegression().fit(X_cpp, y_cpp)

X_rust = df_rust[['Sizes']]
x_rust = df_rust['Times']
model_rust = LinearRegression().fit(X_rust, x_rust)

# Predict new values
new_size = [[1000000000]]
predicted_time_cpp = model_cpp.predict(new_size)
predicted_time_rust = model_rust.predict(new_size)


df_predicted_cpp = pd.DataFrame({'Sizes': new_size[0], 'Times': predicted_time_cpp})
df_predicted_rust = pd.DataFrame({'Sizes': new_size[0], 'Times': predicted_time_rust})
df_combined = pd.concat([df_cpp, df_predicted_cpp, df_rust, df_predicted_rust]).sort_values(by='Sizes')


plt.scatter(df_combined['Sizes'], df_combined['Times'])
plt.plot(df_combined['Sizes'], model_cpp.predict(df_combined[['Sizes']]), color='red', label='C++')
plt.plot(df_combined['Sizes'], model_rust.predict(df_combined[['Sizes']]), color='blue', label='Rust')
plt.xlabel('Sizes')
plt.ylabel('Times')


plt.scatter(1000000000, 172.36, color='darkblue', s=25, label='C++ 10⁹')
plt.scatter(1000000000, 345.29, color='darkred', s=25, label='Rust 10⁹')
plt.plot(df_full_cpp['Sizes'], df_full_cpp['Times'], color='red', linestyle='dashed', alpha=0.5, label='C++ approx line')
plt.plot(df_full_rust['Sizes'], df_full_rust['Times'], color='blue', linestyle='dashed', alpha=0.5, label='Rust approx line')


plt.title('Comparison of C++ and Rust Read Regression Models for Time vs. Size')

plt.scatter(df_predicted_cpp['Sizes'], df_predicted_cpp['Times'], color='green', label=f'C++:{predicted_time_cpp[0]:.2f}', s=25)
plt.scatter(df_predicted_rust['Sizes'], df_predicted_rust['Times'], color='purple', label=f'Rust:{predicted_time_rust[0]:.2f}', s=25)

equation_cpp = f'y = {model_cpp.intercept_:.2f} + {model_cpp.coef_[0]:.10f}x'
plt.text(0.4, 0.95, equation_cpp, transform=plt.gca().transAxes, color='red')

equation_rust = f'y = {model_rust.intercept_:.2f} + {model_rust.coef_[0]:.10f}x'
plt.text(0.4, 0.85, equation_rust, transform=plt.gca().transAxes, color='blue')

plt.legend()
plt.savefig('ReadComparison.png')
plt.show()