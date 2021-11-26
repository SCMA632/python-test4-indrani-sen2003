def hello_world():
    import os 
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
nss = pd.read_csv("4. NSSO68 data set.csv")
list(nss.columns)
# col_names = ['Sector','state','State_Region','District','hhdsz','Religion','Social_Group',
# 'Whether_owns_any_land','Land_Total_possessed','land_tt','MPCE_URP','MPCE_MRP',
# 'Sex','Age','Marital_Status','Education','ricetotal_q','wheattotal_q','cerealstt_q',
# 'pulsestt_q','milkprott_q','edibletotal_q','emftt_q','ricetotal_v','wheattotal_v',
# 'cerealtot_v','pulsestt_v','milkprott_v','edibletotal_v','emftt_v','fv_tot','state_1']
# Choosing only the necessary columns
col_names = ['Religion','Social_Group','Marital_Status','District','state_1','Age','cerealstt_v', 'pulsestot_v', 'Milktotal_v', 'emftt_v', 'milkprott_v','edibletotal_q','MPCE_MRP']
# Subsetting to only the needed columns
needed=nss[col_names]
print(list(needed.columns))
print(needed.head(5))
# To find himachal pradesh:
needed['state_1'].unique()
#It is HP code
# subsetting only to HP state
hp = needed[needed['state_1'] == 'HP']
print(hp.head(5))
# Next to add districts to HP, from wikipedia there are 12.
hp['District'] = hp['District'].\
replace([1,2,3,4,5,6,7,8,9,10,11,12],["Chamba",
                         "Kangra",
                         "Una",
                         "Bilaspur",
                         "Hamirpur",
                         "Kullu",
                         "Lahaul and Spiti",
                         "Mandi",
                         "Kinnaur",
                         "Shimla",
                         "Sirmaur",
                         "Solan"])
print(hp.head(5))
# HP state descriptive stats
hp.describe()

# CLEANING DATA
# Checking for null values
hp.isnull().any()
# There are no NULL values, so no further cleaning required.
# next part of cleaning is to remove outliers
#For this we use boxplots
print(hp.boxplot(column='MPCE_MRP'))
hp['MPCE_MRP'].min(), hp['MPCE_MRP'].max()
def remove_outlier (col):
    sorted(col)
    Q1,Q3 = col.quantile([0.25,0.75])
    IQR = Q3-Q1
    lower_range = Q1-(1.5*IQR)
    upper_range = Q3+(1.5*IQR)
    return lower_range, upper_range
remove_outlier(hp['MPCE_MRP'])
lowincome, uppincome = remove_outlier(hp['MPCE_MRP'])
print(lowincome, uppincome)
hp['MPCE_MRP'] = np.where(hp['MPCE_MRP'] > uppincome,uppincome,hp['MPCE_MRP'])
hp['MPCE_MRP'] = np.where(hp['MPCE_MRP'] < lowincome,lowincome,hp['MPCE_MRP'])
print(hp.boxplot(column='MPCE_MRP'))
list(hp.columns)
dist_mean = hp.groupby(['District'])[['Religion','Social_Group','Marital_Status','Age','cerealstt_v','pulsestot_v',\
                                       'milkprott_v','emftt_v','Milktotal_v','edibletotal_q']].mean()
dist_median = hp.groupby(['District'])[['Religion','Social_Group','Marital_Status','Age','cerealstt_v','pulsestot_v',\
                                       'milkprott_v','emftt_v','Milktotal_v','edibletotal_q']].median()
print(dist_mean)
print(dist_median)


    return(1)
