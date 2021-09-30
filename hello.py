def hello_world():
    import pandas as pd;
    df=pd.read_csv("Walmart2.csv");
    df.dtypes
    df.head(15)
    
    import os 
    import pandas as pd 
    import numpy as np
    os.getcwd()#get cureent working directory
#os.chdir("C:\\Users\\HP\\Desktop\\VCU COURSES\\SCMA\\SCMA IPL")#change directory
    os.getcwd()
    cric=pd.read_csv('d:/IPL Ball-by-Ball 2008-2020.csv')
    cric.columns
    cric['batsman'].unique()
    cric1=cric.groupby(['batsman','id'])[['batsman_runs']].sum()#SUBSETTING BATSMAN
    cric1
    cric.reset_index()
    cric1.reset_index(inplace=True)
    cric1
    cric['batsman'].unique()
    gc=cric1[cric1['batsman']=='GC Smith']#Extracting the assigned batsman
    gc
    score=gc['batsman_runs'].sum()
    score
# finding the appropriate distrubution for the runs scored
    import seaborn as sns
    from fitter import Fitter
    import matplotlib.pyplot as plt
    f=Fitter(score,distributions=['gamma','lognorm','beta','norm','dweibull'])
    f.fit()
    f.summary()
    f.fitted_param['dweibull']
    from scipy.stats import dweibull
    import matplotlib.pyplot as plt
    d=dweibull.rvs(c=0.9854736308803953, loc=738.9999999999998, scale=2.2691608583031957e-13, size=1000,random_state=None)
    sns.distplot(d);
    sns.distplot(score);
    cric['bowler'].unique()
# finding the appropriate distribution for the wickets taken
    cric2=cric.groupby(['bowler','id'])[['is_wicket']].sum() #subsetting 
    cric2
    cric.reset_index()
    cric2.reset_index(inplace=True)
    gg=cric2[cric2['bowler']=='G Gambhir'] #extracting the bowler assigned
    gg
    wicket=gg['is_wicket'].sum()
    wicket
    import seaborn as sns
    from fitter import Fitter
    f=Fitter(wicket,distributions=['gamma','lognorm','beta','norm','dweibull'])
    f.fit()
    f.summary()
    f.fitted_param['dweibull']
    from scipy.stats import dweibull
    import matplotlib.pyplot as plt
    dd=dweibull.rvs(c=0.9064330950735626, loc=8.000000000000002, scale=1.0633413319802765e-14, size=1000,random_state=None)
    sns.distplot(dd);
    sns.distplot(wicket);
    return(1)
