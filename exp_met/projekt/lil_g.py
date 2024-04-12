import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import argrelextrema

def time_diff(data_in):
    n = 5
    data_in['max'] = data_in.loc[argrelextrema(data_in.values, np.greater_equal, order=n)[0]]
    data_in['max'][data_in['max'] < 0.1] = np.nan
    t = np.array(data_in['max'].dropna().index.tolist())/250
    try:
        dt = t[1]-t[0]
        T = (t[1]+t[0])/2
    except:
        dt=1
        T = 1
    return dt, T
    
data = pd.read_csv('exp_met/projekt/lilg.csv', delimiter=';', decimal=',')
data.astype('float64')

time = data[['Time (s) Run #1']].copy()
l1 = 0.147
l2 = 0.296
data = data.drop(labels='Time (s) Run #1', axis=1)
dt = {}

for (columnName, columnData) in data.items():
    dt[columnName] = time_diff(columnData)

dt = pd.DataFrame.from_dict(dt, orient='index')

gate1 = dt.query("index.str.contains('289-982')")
gate2 = dt.query("index.str.contains('805-621')")

T1=gate1[1].to_numpy()
T2=gate2[1].to_numpy()
dt1=gate1[0].to_numpy()
dt2=gate2[0].to_numpy()

dT = T2-T1
v1=l1/dt1
v2=l2/dt2
dv=v2-v1 
a=dv/dT

a = np.delete(a, (2,28,29,45))

print(a.mean())


