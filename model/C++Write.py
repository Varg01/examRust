import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


data = {'Sizes': [10000, 100000, 1000000, 5000000, 10000000, 50000000, 100000000],
        'Times': [0.38, 0.40, 1.04, 7.39, 20.88, 71.26, 764.94]}
df = pd.DataFrame(data)


X = df[['Sizes']]
y = df['Times']
model = LinearRegression().fit(X, y)

# Predict a new value
new_size = [[1000000000]] 
predicted_time = model.predict(new_size)


df_predicted = pd.DataFrame({'Sizes': new_size[0], 'Times': predicted_time})
df_combined = pd.concat([df, df_predicted]).sort_values(by='Sizes')


plt.scatter(df_combined['Sizes'], df_combined['Times'])
plt.plot(df_combined['Sizes'], model.predict(df_combined[['Sizes']]), color='red')
plt.xlabel('Sizes')
plt.ylabel('Times')
plt.title('C++ Write Regression Model for Time vs. Size')


plt.scatter(df_predicted['Sizes'], df_predicted['Times'], color='green', label=f'{predicted_time[0]:.2f}', s=25)

equation = f'y = {model.intercept_:.2f} + {model.coef_[0]:.10f}x'
plt.text(0.3, 0.9, equation, transform=plt.gca().transAxes)

print(f"The predicted time for a size of {new_size[0][0]} is {predicted_time[0]:.2f}")
plt.legend()

plt.savefig('C++Write.png')


