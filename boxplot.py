'''
# import required modules
import matplotlib as plt
import seaborn as sns
# Box plot and violin plot for Outcome vs BloodPressure
_, axes = plt.subplots(1, 2, sharey=True, figsize=(10, 4))
# box plot illustration
sns.boxplot(x='Outcome', y='BloodPressure', data=diabetes, ax=axes[0])
# violin plot illustration
sns.violinplot(x='Outcome', y='BloodPressure', data=diabetes, ax=axes[1])

# Box plot for all the numerical variables
sns.set(rc={'figure.figsize': (16, 5)})
# multiple box plot illustration
sns.boxplot(data=diabetes.select_dtypes(include='number'))
'''


# Import required modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Assuming 'diabetes' is a pandas DataFrame already defined
# For the purpose of this example, let's create a dummy DataFrame
# Remove the below lines if you have the actual 'diabetes' DataFrame
data = {
    'Outcome': [0, 1, 0, 1, 0, 1],
    'BloodPressure': [72, 80, 75, 85, 70, 90],
    'Glucose': [85, 90, 78, 110, 95, 99],
    'Insulin': [0, 130, 88, 130, 90, 150],
    'BMI': [23.1, 30.5, 27.6, 35.4, 24.7, 40.1]
}
diabetes = pd.DataFrame(data)

# Box plot and violin plot for Outcome vs BloodPressure
_, axes = plt.subplots(1, 2, sharey=True, figsize=(10, 4))
# Box plot illustration
sns.boxplot(x='Outcome', y='BloodPressure', data=diabetes, ax=axes[0])
# Violin plot illustration
sns.violinplot(x='Outcome', y='BloodPressure', data=diabetes, ax=axes[1])

# Display the plots
plt.show()

# Box plot for all the numerical variables
sns.set(rc={'figure.figsize': (16, 5)})
# Multiple box plot illustration
sns.boxplot(data=diabetes.select_dtypes(include='number'))

# Display the plot
plt.show()
