# Debugging activity errors

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('sample_data.xlsx')
print(df)

# Plot male vs female count
gender_counts = df['Gender'].value_counts()
plt.bar(gender_counts.index, gender_counts.values)
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# Plot female ages
female_data = df(df['Gender'] == 'Female')
plt.plot(female_data['Age'], marker='o', linestyle='-')
plt.title('Female Ages')
plt.xlabel('Index')
plt.ylabel('Age')
plt.show()
