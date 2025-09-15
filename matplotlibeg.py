import pandas as pd
import matplotlib.pyplot as plt 

# Create DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Salary": [90000, 480000, 515000, 262000]
}
# DataFrame: A 2D table of data (rows and columns).
df = pd.DataFrame(data) 


# Plot bar chart
plt.bar(df["Name"], df["Salary"])
plt.title("Employee Salary Distribution")
plt.xlabel("Employee Name")
plt.ylabel("Salary ($)")
plt.grid(axis='y')
plt.show()