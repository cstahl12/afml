import pandas as pd
import numpy as np


def dollar_bar(dates, series, m):
      
    idx = []
    d_acum = []
    c_dv = 0 

    for i, dv in aux["dollar_vol"].items():
        c_dv = c_dv + dv 
        if c_dv >= m:
            idx.append(i)
            d_acum.append(c_dv)
            c_dv = 0 
    dollar_bar = aux.loc[idx]
    dollar_bar.loc[idx, 'cum_dollar_vol'] = d_acum 
    dollar_bar = dollar_bar.set_index('date')
    return dollar_bar.copy()



def dollar_bar_cum(df, m):
    aux = df.reset_index()
    cum_dv = aux.dollar_vol.cumsum()  
    th = m
    idx = []
    for i, c_dv in cum_dv.items():
        if c_dv >= th:
            th = th + m
            idx.append(i)
    return aux.loc[idx].set_index('date').copy()

