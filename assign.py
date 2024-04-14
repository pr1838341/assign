# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 09:00:06 2023

@author: Krishna
"""

import pandas as pd
df=pd.read_csv("Q7.csv")
df
x=df["Points"]
y=df["Score"]
z=df["Weigh"]
x.mean()#points     3.5965625           score   3.2172500000000004
x.std()#              0.5346787360709716 score 0.9784574429896967
#NULL
x.mode()#points  0    3.07              scsore
                 #1    3.92
x.median()        #points 3.6950000000000003  score
x.var()      #points   0.28588135080645166  scorx
y.mean()
y.std()
import numpy as np                       #    Mean: 3.2172500000000004
                                                #   Mode: 3.0
                                          # Variance: 0.9274608750000002
                                                   #  Median: 3.325
                                       # Standard Deviation: 0.9630477013107919

def calculate_statistics(zip):
    return {                                         #Mean: 3.2172500000000004
                                                  #   Mode: 3.0
                                                #Variance: 0.9274608750000002
                                               # Median: 3.325
                                            # Standard Deviation: 0.9630477013107919
        'Mean': np.mean(z),
        'Mode': float(np.argmax(np.bincount(z))),
        'Variance': np.var(z),
        'Median': np.median(z),
        'Standard Deviation': np.std(z)
    }


statistics_result = calculate_statistics(z)

for stat, value in statistics_result.items():
    print(f"{stat}: {value}")
    
    
    


#ean: 17.848750000000003
#Mean: 17.848750000000003
#Mode: 17.0
#Mode: 17.0
##Variance: 3.0933796874999997
#Variance: 3.0933796874999997
#Median: 17.71
#Median: 17.71
#Standard Deviation: 1.758800638929836
#Standard Deviation: 1.758800638929836
#Traceback (most recent call last):      
 
    import pandas as pd 
    df=pd.read_csv("Q7.csv")
    df
    df1=df.groupby(by="Unnamed: 0").mean()[['Points','Score','Weigh']]
    df1
    df1.std()#Points    0.534679Score     0.978457 Weigh     1.786943
    df1.mean()#Points     3.59656Score      3.217250 Weigh     17.848750 dtype: float64
    df1.var()#Points    0.285881Score     0.957379Weigh     3.193166dtype: float64
    df1.mode()# Points  Score  Weigh0    3.07   3.44  17.02 1    3.92    NaN  18.90
    df1.median()#Points     3.695Score      3.325Weigh     17.710 dtype: float64
    #######
    import pandas as pd
    df=pd.read_csv("Q9_a.csv")
    df
    df.hist()
    df.skew()
    df2=pd.read_csv("Q9_b.csv")
    df2
    df2.hist()
    df2.skew()
import numpy as np
    #three coins tossed[=["HHH"],["HHT"],["HTH"],["TTT"],["TTH"],["THT"], ["HTT"],["THH"]
    threecoinstossed=8
    twoheadandonetail=3

    probabilityoftwoheadandonetail=3/8
    probabilityoftwoheadandonetail
    #dice
    #TwoDicearerolled=[1,1][1,2],[1,3],[1,4],[1,5],[1,6],[2,1],[2,2],[2,3],[2,4],
    #[2,5][2,6],[3,1][3,2],[3,3],[3,4],[3,5][3,6][4,1],[4,2],[4,3],[4,4],[4,5][4,6],[5,1,[5,2],[5,3],[5,4],[5,5][5,6]
                                    #  [6,1],[6,2],[6,3],[6,4],[6,5],[6,6]
                                      

    #Equalto1=1
    two_diced_rolled=36

    equal_to_4=8
    probability_equal_to_4=8/36
    probability_equal_to_4
