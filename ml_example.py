# ml_example.py
# Author: Bakhrom Botirov

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample data: study hours vs. exam score
hours = np.array([[1], [2], [3], [4], [5], [6]])
scores = np.array([35, 45, 50, 60, 70, 75])

# Create and train the model
model = LinearRegression()
model.fit(hours, scores)

# Make predictions
predicted_scores = model.predict(hours)

# Display model results
print("Coefficient (slope):", model.coef_[0])
print("Intercept:", model.intercept_)
print("Predicted Scores:", predicted_scores)

# Plot
plt.scatter(hours, scores, color='blue', label='Actual')
plt.plot(hours, predicted_scores, color='red', label='Predicted')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.legend()
plt.title('Linear Regression Example')
plt.show()