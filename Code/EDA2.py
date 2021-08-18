import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np
states_data_br = pd.read_csv('india-districts-census-2011.csv')

''' 1 '''
states_pop_br = states_data_br.Population.sum()
states_pop_br_male = states_data_br.Male.sum()
states_pop_br_female = states_data_br.Female.sum()
labels_br = ['Total','Male','Female']
li_br = [states_pop_br,states_pop_br_male,states_pop_br_female]
plt.title('MALE v/s FEMALE Ratio')
sn.barplot(labels_br,li_br)
plt.show()

''' 2 '''
states_pop_br_hh_lp = states_data_br.LPG_or_PNG_Households.sum()
states_pop_br_hh_el = states_data_br.Housholds_with_Electric_Lighting.sum()
states_pop_br_hh_in = states_data_br.Households_with_Internet.sum()
states_pop_br_hh_co = states_data_br.Households_with_Computer.sum()
labels_br_hh_fa = ['LPG or PNG','Electricity','Internet Facility','Computer']
plt.xticks(rotation=45)
li_br_hh_fa = [states_pop_br_hh_lp,states_pop_br_hh_el,states_pop_br_hh_in,states_pop_br_hh_co]
plt.title('FACILITIES')
sn.barplot(labels_br_hh_fa,li_br_hh_fa)
plt.show()

''' 3 '''
states_pop_br_lit = states_data_br.Literate.sum()
states_pop_br_lit_male = states_data_br.Male_Literate.sum()
states_pop_br_lit_female = states_data_br.Female_Literate.sum()
labels_br_l = ['Total','Male','Female']
li_br_l = [states_pop_br_lit,states_pop_br_lit_male,states_pop_br_lit_female]
plt.title('MALE v/s FEMALE Literacy rate')
sn.barplot(labels_br_l,li_br_l)
plt.show()


''' 4 '''
x=states_data_br['Male_Literate']
y=states_data_br['Female_Literate']
plt.plot(x,y,'o')
plt.xlabel('Male Literate')
plt.ylabel('Female Literate')
plt.show()


''' 5 '''

states_data_br[['Primary_Education','Higher_Education']].plot(figsize=(12,5))