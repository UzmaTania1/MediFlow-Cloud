import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Path setup
base_path = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(os.path.dirname(__file__), "..", "data", "patient_data.csv")
df = pd.read_csv(file_path)

# Convert dates
df['admission_date'] = pd.to_datetime(df['admission_date'])
df['discharge_date'] = pd.to_datetime(df['discharge_date'])

# Length of stay
df['los'] = (df['discharge_date'] - df['admission_date']).dt.days

# Metrics
print("Readmission Rate:", df['readmitted'].mean()*100)
print("Average LOS:", df['los'].mean())

# Create outputs folder
output_path = os.path.join(base_path, "outputs")
os.makedirs(output_path, exist_ok=True)

sns.set(style="whitegrid")

# 1. Readmission by disease
plt.figure()
df.groupby('disease')['readmitted'].mean().plot(kind='bar')
plt.savefig(os.path.join(output_path, "readmission.png"))
plt.close()

# 2. City count
plt.figure()
df['city'].value_counts().plot(kind='bar')
plt.savefig(os.path.join(output_path, "city.png"))
plt.close()

# 3. Age vs readmission
plt.figure()
sns.boxplot(x='readmitted', y='age', data=df)
plt.savefig(os.path.join(output_path, "age.png"))
plt.close()

# 4. Department
plt.figure()
df['department'].value_counts().plot(kind='bar')
plt.savefig(os.path.join(output_path, "department.png"))
plt.close()

# 5. Cost
plt.figure()
df.groupby('disease')['treatment_cost'].mean().plot(kind='bar')
plt.savefig(os.path.join(output_path, "cost.png"))
plt.close()

print("All charts created ✅")
print("Saving files to:", output_path)