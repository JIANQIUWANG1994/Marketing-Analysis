import pandas as pd
import matplotlib.pyplot as plt

excel_file = 'Assignment3.xlsx'
df_1 = pd.read_excel(excel_file)
df_2 = pd.read_excel(excel_file, sheet_name = 'Example 2')
df_3 = pd.read_excel(excel_file, sheet_name = 'Example 3')

print(df_2.head(5))

grade = df_1.Grade
bins = [30,40,50,60,70,80,90]
graph = plt.hist(grade,bins,rwidth=0.75)
plt.xlabel('Bin')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()


data_1 = df_2[['No. of Cup of Coffee']]
data_2 = df_2[['No. of Cup of Hot Tea']]

Descriptive_Statistics_1 = data_1.describe()
Descriptive_Statistics_2 = data_2.describe()
print(Descriptive_Statistics_1, Descriptive_Statistics_2)
Descriptive_Statistics_1.to_excel('coffee.xlsx')
Descriptive_Statistics_2.to_excel('hot tea.xlsx')

data1 = df_3.Demand
print(data1)