import pandas as pd
import matplotlib.pyplot as plt
from itertools import groupby
pop=pd.read_csv("D:\Academics\SEM 5\Data Analytics\Project\India census 2011\india-districts-census-2011.csv")


#Female population vs Female literacy rate
a=(pop['Female'].groupby(pop['State name'])).sum()
b=(pop['Female_Literate'].groupby(pop['State name'])).sum()

print(((pop['Female'].groupby(pop['State name'])).sum()))
print(((pop['Female_Literate'].groupby(pop['State name'])).sum()))

for i in range(0,35):
        for j in range(0,35):
            if(i==j):
                print(i+1," ",b[i]/a[i],"\n")
                
#Male population vs Male literacy rate
a=(pop['Male'].groupby(pop['State name'])).sum()
b=(pop['Male_Literate'].groupby(pop['State name'])).sum()

print(((pop['Male'].groupby(pop['State name'])).sum()))
print(((pop['Male_Literate'].groupby(pop['State name'])).sum()))

for i in range(0,35):
        for j in range(0,35):
            if(i==j):
                print(i+1," ",b[i]/a[i],"\n")

#Total population vs Total literacy rate
a=(pop['Population'].groupby(pop['State name'])).sum()
b=(pop['Literate'].groupby(pop['State name'])).sum()

print(((pop['Population'].groupby(pop['State name'])).sum()))
print(((pop['Literate'].groupby(pop['State name'])).sum()))

for i in range(0,35):
        for j in range(0,35):
            if(i==j):
                print(i+1," ",b[i]/a[i],"\n")


#Correlation
from numpy import cov
cov(pop['Graduate_Education'],pop['Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car'])


plt.scatter(pop['Graduate_Education'],pop['Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car'])
plt.show()


pop['Graduate_Education'].corr(pop['Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car'])

pop['Total_Education'].corr(pop['Age_Group_0_29'])




#workers vs population

a=(pop['Population'].groupby(pop['State name'])).sum()
b=(pop['Workers'].groupby(pop['State name'])).sum()

print(((pop['Population'].groupby(pop['State name'])).sum()))
print(((pop['Workers'].groupby(pop['State name'])).sum()))
min=1
for i in range(0,35):
        for j in range(0,35):
            if(i==j):
                print(i+1," ",b[i]/a[i],"\n")
                if(min>(b[i]/a[i]) and i!=17):
                    min=b[i]/a[i];
                    index=i+1;
print(min,index) #UP has highest unemployement


#population grouped by states
states=pop.groupby('State name').sum()
states=states[['Population']]
states=states.sort_values(['Population'],ascending=[0])
print(states)
plt.figure(figsize=(2,5))
states.plot(kind='bar',stacked=True)
plt.show()

