import pandas as pd
import numpy as np

# Create DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 32, 37, 45],
    "Salary": [70000, 48000, 55000, 62000]
}
# DataFrame: A 2D table of data (rows and columns).
df = pd.DataFrame(data)
print("Full DataFrame:")
print(df)

#Filtering: Select specific rows based on conditions.
high_salary = df[df["Salary"] > 50000]
print("Employees with Salary > $50,000:")
print(high_salary)
 
array = np.array([[11, 22, 3],
                  [4, 5, 66],
                  [7, 8, 9]])

print("NumPy Array:")
print(array)
print("\nSum of all elements:", np.sum(array))
print("Mean of elements:", np.mean(array))
print("Transpose of Array:\n", np.transpose(array))
