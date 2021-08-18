import pandas as pd
import matplotlib.pyplot as plt

'''
Importing the dataset
'''
dataset=pd.read_csv("Literacy.csv")

'''
Splitting the dataset into target and independent variable
'''
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,-1].values

'''
Training the Lasso model on the dataset
'''

from sklearn.linear_model import Lasso
lasso=Lasso(alpha=0.1)
lasso_coef=lasso.fit(X,Y).coef_

'''
Plotting the priority graph
'''
names=dataset.drop('LR',axis=1).columns
plt.plot(range(len(names)),lasso_coef)
plt.xticks(range(len(names)),names,rotation=60)
plt.ylabel("Coefficients")
plt.show()

