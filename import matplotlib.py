import matplotlib.pyplot as plt
import pandas as pd

# Example dataset: You can replace this with your own CSV or data file
data = {
    'Age': [23, 45, 31, 35, 52, 41, 28],
    'Salary': [50000, 80000, 54000, 58000, 95000, 67000, 48000],
    'Department': ['HR', 'Engineering', 'HR', 'Marketing', 'Engineering', 'Marketing', 'HR']
}

# Create DataFrame
df = pd.DataFrame(data)

# Line Plot: Age vs Salary
plt.figure(figsize=(8, 5))
plt.plot(df['Age'], df['Salary'], marker='o', linestyle='--', color='b')
plt.title('Line Plot of Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.grid(True)
plt.show()

# Bar Chart: Average Salary by Department
avg_salary = df.groupby('Department')['Salary'].mean()
plt.figure(figsize=(8, 5))
avg_salary.plot(kind='bar', color='green')
plt.title('Average Salary by Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.show()

# Histogram: Distribution of Age
plt.figure(figsize=(8, 5))
plt.hist(df['Age'], bins=5, color='orange', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Scatter Plot: Age vs Salary
plt.figure(figsize=(8, 5))
plt.scatter(df['Age'], df['Salary'], color='red')
plt.title('Scatter Plot of Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()

# Pie Chart: Distribution of Departments
dept_count = df['Department'].value_counts()
plt.figure(figsize=(6, 6))
dept_count.plot(kind='pie', autopct='%1.1f%%', colors=['skyblue','lightgreen','lightcoral'])
plt.title('Department Distribution')
plt.ylabel('')  # Hide y-label for pie chart
plt.show()