import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# input data
sizes = np.array([250, 375, 500, 750, 1000, 1250, 1500])
times = np.array([6.45, 27.67, 68.57, 266.17, 660.06, 1229.57, 2460.65])

# plot the data
plt.scatter(sizes, times)
plt.xlabel('Size')
plt.ylabel('Time')
plt.title('Scatter Plot of Data')

# transform input data to include polynomial features up to degree 3
poly_features = PolynomialFeatures(degree=3, include_bias=False)
sizes_poly = poly_features.fit_transform(sizes.reshape(-1, 1))

# create a linear regression model and fit it to the transformed data
model = LinearRegression().fit(sizes_poly, times)

# predict values for new inputs
new_sizes = np.array([2000, 2500, 3000]).reshape((-1, 1))
new_sizes_poly = poly_features.transform(new_sizes)
new_times = model.predict(new_sizes_poly)
print("Predicted times for new sizes:", new_times)

# create a line plot of the polynomial regression model
x = np.linspace(sizes.min(), sizes.max(), 100).reshape(-1,1)
x_poly = poly_features.transform(x)
y = model.predict(x_poly)
plt.plot(x, y, color='red')

# show the plot
plt.show()
