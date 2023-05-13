import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data_cpp = {'Sizes': [100000, 500000, 1000000, 5000000, 10000000, 50000000, 100000000, 200000000],
        'Times': [9.74, 50.36, 98.54, 504.12, 1038.80, 5430.97, 10885.61, 22334.26]}
df_full_cpp = pd.DataFrame(data_cpp)

data_rust = {'Sizes': [100000, 500000, 1000000, 5000000, 10000000, 50000000, 100000000, 200000000],
        'Times': [9.22, 49.80, 97.78, 502.33, 1030.17, 5380.23, 10822.97, 21815.12]}
df_full_rust = pd.DataFrame(data_rust)


data_cpp = {'Sizes': [100000, 500000, 1000000, 5000000, 10000000, 50000000, 100000000],
        'Times': [9.74, 50.36, 98.54, 504.12, 1038.80, 5430.97, 10885.61]}
df_cpp = pd.DataFrame(data_cpp)

data_rust = {'Sizes': [100000, 500000, 1000000, 5000000, 10000000, 50000000, 100000000],
        'Times': [9.22, 49.80, 97.78, 502.33, 1030.17, 5380.23, 10822.97]}
df_rust = pd.DataFrame(data_rust)

# Create linear regression models
X_cpp = df_cpp[['Sizes']]
y_cpp = df_cpp['Times']
model_cpp = LinearRegression().fit(X_cpp, y_cpp)

X_rust = df_rust[['Sizes']]
y_rust = df_rust['Times']
model_rust = LinearRegression().fit(X_rust, y_rust)

# Predict new values
new_size = [[200000000]]
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


plt.scatter(200000000, 22334.26, color='darkred', s=25, label='C++ 2*10⁸')
plt.scatter(200000000, 21815.12, color='darkblue', s=25, label='Rust 2*10⁸')
plt.plot(df_full_cpp['Sizes'], df_full_cpp['Times'], color='red', linestyle='dashed', alpha=0.5, label='C++ approx line')
plt.plot(df_full_rust['Sizes'], df_full_rust['Times'], color='blue', linestyle='dashed', alpha=0.5, label='Rust approx line')

plt.title('Comparison of C++ and Rust Merge Sort Regression Models for Time vs. Size')

plt.scatter(df_predicted_cpp['Sizes'], df_predicted_cpp['Times'], color='green', label=f'C++:{predicted_time_cpp[0]:.2f}', s=25)
plt.scatter(df_predicted_rust['Sizes'], df_predicted_rust['Times'], color='purple', label=f'Rust:{predicted_time_rust[0]:.2f}', s=25)


equation_cpp = f'y = {model_cpp.intercept_:.2f} + {model_cpp.coef_[0]:.10f}x'
plt.text(0.4, 0.95, equation_cpp, transform=plt.gca().transAxes, color='red')

equation_rust = f'y = {model_rust.intercept_:.2f} + {model_rust.coef_[0]:.10f}x'
plt.text(0.4, 0.85, equation_rust, transform=plt.gca().transAxes, color='blue')


plt.legend()
plt.savefig('SortComparison.png')
plt.show()