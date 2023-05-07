import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Create a Pandas dataframe with the data
data = {'Sizes': [100000, 500000, 1000000, 5000000, 10000000, 50000000, 100000000],
        'Times': [9.22, 49.80, 97.78, 502.33, 1030.17, 5380.23, 10822.97]}
df = pd.DataFrame(data)

# Create a linear regression model
X = df[['Sizes']]
y = df['Times']
model = LinearRegression().fit(X, y)

# Predict a new value
new_size = [[200000000]] # Note that X must be a 2D array for predict method
predicted_time = model.predict(new_size)

# Add the predicted value to the data frame
df_predicted = pd.DataFrame({'Sizes': new_size[0], 'Times': predicted_time})
df_combined = pd.concat([df, df_predicted]).sort_values(by='Sizes')

# Plot the data points and regression line
plt.scatter(df_combined['Sizes'], df_combined['Times'])
plt.plot(df_combined['Sizes'], model.predict(df_combined[['Sizes']]), color='red')
plt.xlabel('Sizes')
plt.ylabel('Times')
plt.title('Rust Merge Sort Regression Model for Time vs. Size')

# Add the predicted value to the plot
plt.scatter(df_predicted['Sizes'], df_predicted['Times'], color='green', label=f'{predicted_time[0]:.2f}', s=25)

# Add the equation of the regression line to the plot
equation = f'y = {model.intercept_:.2f} + {model.coef_[0]:.10f}x'
plt.text(0.3, 0.9, equation, transform=plt.gca().transAxes)

print(f"The predicted time for a size of {new_size[0][0]} is {predicted_time[0]:.2f}")
plt.legend()

plt.savefig('RustSort.png')
plt.show()
