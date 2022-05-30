# -*- coding: utf-8 -*-
"""
Created on Mon May 30 05:14:42 2022

@author: 06nic
"""

List = [1,2,4]
type(List)
import pandas as pd
import numpy as np
import yfinance as yf

start = "2014-12-31"
end = "2021-12-31"

Cac40_data = yf.download("^FCHI", start, end )["Close"][:1759]
EuroStoxx_data = yf.download("^STOXX50E", start, end )["Close"][:1759]
Dow_Jones_data =  yf.download("^DJI", start, end )["Close"][:1759]

Cac_change = Cac40_data.pct_change().dropna()
Eurostoxx_change= EuroStoxx_data.pct_change().dropna()
DJ_change= Dow_Jones_data.pct_change().d)ropna()

Change_ptf = np.transpose(np.array([Cac_change,Eurostoxx_change,DJ_change]))
type(Change_ptf)
np.percentile(Change_ptf[:,1], 0.15)


def value_at_risk (Histo_returns, weight, alpha, lookback_days, initial_portfolio):
    List = [np.percentile(Histo_returns[:,0],1-alpha),np.percentile(Histo_returns[:,1],1-alpha),np.percentile(Histo_returns[:,2],1-alpha) ]
    Var_ptf = List @ np.transpose(weight)
    return print("There is a probability of ", formatpct(1-alpha) ," that our portfolio loses more than",Var_ptf*initial_portfolio)
    
        
value_at_risk(Change_ptf, [0.3,0.4,0.3], 0.99, 1000, 100000)

def C_Var (Histo_returns, weight, alpha, lookback_days, initial_portfolio):
    value_at_risk(Histo_returns, weight, alpha, lookback_days, initial_portfolio)
    Mean_extreme_loss = [np.mean(Histo_returns[:,0][Histo_returns[:,0]< List[0]]),np.mean(Histo_returns[:,1][Histo_returns[:,1]< List[1]]),np.mean(Histo_returns[:,2][Histo_returns[:,2]< List[2]])]
    Cond_Var = Mean_extreme_loss @ np.transpose(weight)   
    return print ("Conditional value at risk is ", format(Cond_Var*initial_portfolio) )              

C_Var(Change_ptf, [0.3,0.4,0.3], 0.99, 1000, 100000)
