import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")

tips = sns.load_dataset("tips")
# print(tips)
sns.relplot(x="total_bill", y="tip", data=tips)

plt.show()

# Analyze complete data set of tips
# https://seaborn.pydata.org/tutorial/relational.html
# https://www.kaggle.com/datasets | Donwload any dataset of your choice
# Explore DataSet with Pandas and Seaborn