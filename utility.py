import pandas as pd

#本利均攤
########################################################################################################################################################
def loanpayment(amount,periods,rate,fee,time=0,default_time=0):   #time 為了讓columns不要重複 然後第幾期投 #default_time 如果是6,代表第5期繳完以後就沒繳了
    x = (amount/(1+fee))*fee
    amount = amount-x
    d = amount / ((1-pow((1+(rate/1200)),(-periods)))/ (rate/1200))
    df = pd.DataFrame(columns=[f'remain_principal',f're_principal',f're_interest',f'sum_re'])
    for i in range(0,periods+1+time):
        if i < time: 
            df.loc[i,f'remain_principal'] = 0
            df.loc[i,f're_principal'] = 0
            df.loc[i,f're_interest'] = 0
            df.loc[i,f'sum_re'] = 0
            df.loc[i,f'default'] = 0
        elif i == time:
            df.loc[i,f'remain_principal'] = amount
            df.loc[i,f're_principal'] = 0
            df.loc[i,f're_interest'] = 0
            df.loc[i,f'sum_re'] = 0
            df.loc[i,f'default'] = 0
        else:
            df.loc[i,f're_interest'] = df.loc[i-1,f'remain_principal'] * ((rate * 0.01) /12)
            df.loc[i,f're_principal'] = d - df.loc[i,f're_interest'] 
            df.loc[i,f'remain_principal'] = df.loc[i-1,f'remain_principal'] - df.loc[i,f're_principal']
            df.loc[i,f'sum_re'] = df.loc[i,f're_principal']+df.loc[i,f're_interest']
    if default_time == 0:
        return df
    else:
        df.loc[time+default_time:,[f'remain_principal',f're_interest',f're_principal',f'sum_re']]=0
        df.loc[time+default_time:,f'default'] = df.loc[default_time+time-1,f'remain_principal']
        df[f'default'].fillna(0,inplace=True)
        return df
    
#到期還本
######################################################################################################################################################
def loanpayment_maturity(amount,periods,rate,fee,time=0,default_time=0):   #time 為了讓columns不要重複 然後第幾期投 #default_time 如果是6,代表第5期繳完以後就沒繳了
    x = (amount/(1+fee))*fee
    amount = amount-x
    interest = (amount * (rate*0.01))/12
    df = pd.DataFrame(columns=[f'remain_principal',f're_principal',f're_interest',f'sum_re'])
    for i in range(0,periods+1+time):
        if i < time: 
            df.loc[i,f'remain_principal'] = 0
            df.loc[i,f're_principal'] = 0
            df.loc[i,f're_interest'] = 0
            df.loc[i,f'sum_re'] = 0
            df.loc[i,f'default'] = 0
        elif i == time:
            df.loc[i,f'remain_principal'] = amount
            df.loc[i,f're_principal'] = 0
            df.loc[i,f're_interest'] = 0
            df.loc[i,f'sum_re'] = 0
            df.loc[i,f'default'] = 0
        elif i < periods:
            df.loc[i,f're_interest'] = interest
            df.loc[i,f're_principal'] = 0
            df.loc[i,f'remain_principal'] = amount
            df.loc[i,f'sum_re'] = df.loc[i,f're_principal']+df.loc[i,f're_interest']
        else:
            df.loc[i,f're_interest'] = interest
            df.loc[i,f're_principal'] = amount
            df.loc[i,f'sum_re'] = df.loc[i,f're_principal']+df.loc[i,f're_interest']
            df.loc[i,f'remain_principal'] = 0

    if default_time == 0:
        return df
    else:
        df.loc[time+default_time:,[f'remain_principal',f're_interest',f're_principal',f'sum_re']]=0
        df.loc[time+default_time:,f'default'] = df.loc[default_time+time-1,f'remain_principal']
        df[f'default'].fillna(0,inplace=True)
        return df