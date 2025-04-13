import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load CSV file
df = pd.read_csv("data_Q1.csv")  # Using your specified file name

# Extract columns
x1 = df.iloc[:, 0]  # First column (x1)
x2 = df.iloc[:, 1]  # Second column (x2)
y = df.iloc[:, 2]   # Third column (y)

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
ax.scatter(x1, x2, y, c='b', marker='o')

# Labels
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('Y')
ax.set_title('3D Scatter Plot')

plt.show()

print(f"Number of points: {len(df)}")

