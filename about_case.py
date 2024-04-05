from plotly.subplots import make_subplots
import plotly.graph_objects as go
import sql_commond as sc
import numpy as np
import pandas as pd
import utility as u 
import numpy_financial as npf


import warnings
warnings.filterwarnings('ignore')


#先組fig1框架
fig = make_subplots(rows=3,cols=3,
                    specs=[[{'type': 'domain', "rowspan": 3,"colspan": 1}, {'type': 'xy', "rowspan": 3,"colspan": 2}, None],
                            [None, None, None],
                            [None, None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=('逾期催收相關',
                                    '逾催30天機率密度分布(by件數)'
                                    )
                    )
fig.update_layout(height=500,width=1900) #調整fig的大小
##############################################################
#先組fig1框架
fig7 = make_subplots(rows=3,cols=3,
                    specs=[[{'type': 'domain', "rowspan": 3,"colspan": 1}, {'type': 'domain', "rowspan": 3,"colspan": 1}, {'type': 'domain', "rowspan": 3,"colspan": 1}],
                            [None, None, None],
                            [None, None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=('案件量(by 期數)',
                                    '案件量(by 利率)',
                                    '案件量(期數 & 利率)'
                                    )
                    )
fig7.update_layout(height=500,width=1900) #調整fig的大小
##############################################################
#figure_case_summary
figure_case_summary = make_subplots(rows=2,cols=1,
                    specs=[
                            [{'type': 'xy', "rowspan": 2,"colspan": 1,"secondary_y": True}],
                            [None],
                            ],
                    subplot_titles=(
                                    '每月上架總數/總量' ,
                                    ),
                    )
##############################################################
##############################################################
#figure_case_summary
Defulat30_summary = make_subplots(rows=1,cols=2,
                    specs=[
                            [{'type': 'domain', "rowspan": 1,"colspan": 1},{'type': 'domain', "rowspan": 1,"colspan": 1}],
                            ],
                    subplot_titles=(
                                    '每月進入逾催階段之件數/量' ,
                                    '預計本月再新增件數/量',
                                    ),
                    )
##############################################################
##############################################################
#報酬率的彙整
about_return = make_subplots(rows=2,cols=2,
                    specs=[
                            [{'type': 'domain', "rowspan": 2,"colspan": 1},{'type': 'domain', "rowspan": 2,"colspan": 1}],
                            [None, None],
                            ],
                    subplot_titles=(
                                    '本息均攤' ,
                                    '到期還本',
                                    ),
                    )
about_return.update_layout(font=dict(size=20)) 
##############################################################
#叫資料
#呆帳率計算

defualt_table = pd.read_excel(r'data/defualt_table.xlsx')


total_case_number = 68853
defualt_case_number = 3512

x_default,y_default = sc.default_distribution(total_case_number,defualt_case_number)



df_forecast_summary = pd.read_excel(r'data/df_forecast_summary.xlsx')
df_forecast30 = df_forecast_summary[['本月預計尚有金額']]
df_forecast_summary = df_forecast_summary[['總逾催金額']]




#案件分布狀態
number = pd.read_excel(r'data/number.xlsx')
rate = pd.read_excel(r'data/rate.xlsx')
combin = pd.read_excel(r'data/combin.xlsx')

#期數
_ = np.sum(number['件數'])
number['pct'] = number.apply(lambda x:f"{(x['件數']/_)*100:.2f}%",axis=1)
number = number.sort_values('件數',ascending=False)

#利率
rate.loc[rate['利率'] < 10 ,'利率'] = 'Others'
rate = rate.groupby('利率',as_index=False)['件數'].agg('sum')
_ = np.sum(rate['件數'])
rate['pct'] = rate.apply(lambda x:f"{(x['件數']/_)*100:.2f}%",axis=1)
rate = rate.sort_values('件數',ascending=False)
rate_df = rate

#利率+期數
_ = np.sum(combin['件數'])
combin['pct'] = combin.apply(lambda x:f"{(x['件數']/_)*100:.2f}%",axis=1)
combin = combin.sort_values('件數',ascending=False)

#每月上架總數及總量

case_summary = pd.read_excel(r'data/case_summary.xlsx')


#逾催30天明細

defualt_30_detail = pd.read_excel(r'data/defualtMaturity_30_combine.xlsx')

#by案件到期的逾催狀況(合併用)
defualtMaturity_30_combine = pd.read_excel(r'data/defualtMaturity_30_combine.xlsx')
defualtMaturity_30_credit = defualtMaturity_30_combine.loc[defualtMaturity_30_combine['type'] == '信',:]
defualtMaturity_30_house = defualtMaturity_30_combine.loc[defualtMaturity_30_combine['type'] == '房']


defualtMaturity_30_combine['件數逾催(%)'] = round((defualtMaturity_30_combine['累積總逾催案件數'] / defualtMaturity_30_combine['累積總結案數'])*100,3)
defualtMaturity_30_combine['金額逾催(%)'] = round((defualtMaturity_30_combine['累積總逾催總金額'] / defualtMaturity_30_combine['累積總案件金額'])*100,3)


#by案件到期的逾催狀況(拆信房)
defualtMaturity_30_credit['件數逾催(%)'] = round((defualtMaturity_30_credit['累積總逾催案件數'] / defualtMaturity_30_credit['累積總結案數'])*100,3)
defualtMaturity_30_credit['金額逾催(%)'] = round((defualtMaturity_30_credit['累積總逾催總金額'] / defualtMaturity_30_credit['累積總案件金額'])*100,3)

defualtMaturity_30_house['件數逾催(%)'] = round((defualtMaturity_30_house['累積總逾催案件數'] / defualtMaturity_30_house['累積總結案數'])*100,3)
defualtMaturity_30_house['金額逾催(%)'] = round((defualtMaturity_30_house['累積總逾催總金額'] / defualtMaturity_30_house['累積總案件金額'])*100,3)




#計算報酬率相關
################################################################################################################## 本利均攤
amount = 1000000
periods_list = [12,18,24,36,48] #案件期數
rate_list = [14,15,16]  #案件利率
fee_list = [0,0.01,0.02]  #交易手續費
manage_fee_list = [0,0.1,0.2] #金流管理費
principalAndInterestePayack_dict = {}
num=0 #字典編號用
for fee in fee_list:
        for manage_fee in manage_fee_list:
                for periods in periods_list:
                        for rate in rate_list:
                                df_1 = u.loanpayment(amount,periods,rate,fee)
                                df_1['real_interest'] = df_1['re_interest']*(1-manage_fee)
                                df_1['total_return'] = df_1['re_principal'] + df_1['real_interest']
                                total_return = df_1['total_return'].sum()
                                irr_list = [amount*-1] + df_1.loc[1:,'total_return'].to_list()
                                irr_value = npf.irr(irr_list)*12 #因為是月份 所以*12變成年化
                                principalAndInterestePayack_dict[num]= {'交易手續費':f"{int(fee*100)}%",'金流維護費':f"{int(manage_fee*100)}%",'期數':periods,'利率':f"{rate}%",'成本':amount ,'總回收':round(total_return,0) ,'利息收入':round((total_return-amount),0) ,
                                                        '到期報酬率(ROI)':f"{round(((total_return/amount)-1)*100,2)}%" ,'年化報酬率':f"{round(((total_return/amount)**(1/(periods/12))-1)*100,2)}%"  ,
                                                        'IRR':f"{round(irr_value*100,2)}%"}
                                num += 1

principalAndInterestePayack_df = pd.DataFrame(principalAndInterestePayack_dict).T
# print(principalAndInterestePayack_df)
################################################################################################################## 到期還本
maturityPayback_dict = {}
num=0 #字典編號用
for fee in fee_list:
        for manage_fee in manage_fee_list:
                for periods in periods_list:
                        for rate in rate_list:
                                df_1 = u.loanpayment_maturity(amount,periods,rate,fee)
                                df_1['real_interest'] = df_1['re_interest']*(1-manage_fee)
                                df_1['total_return'] = df_1['re_principal'] + df_1['real_interest']
                                total_return = df_1['total_return'].sum()
                                irr_list = [amount*-1] + df_1.loc[1:,'total_return'].to_list()
                                irr_value = npf.irr(irr_list)*12 #因為是月份 所以*12變成年化
                                maturityPayback_dict[num]= {'交易手續費':f"{int(fee*100)}%",'金流維護費':f"{int(manage_fee*100)}%",'期數':periods,'利率':f"{rate}%",'成本':amount ,'總回收':round(total_return,0) ,'利息收入':round((total_return-amount),0) ,
                                                        '到期報酬率(ROI)':f"{round(((total_return/amount)-1)*100,2)}%" ,'年化報酬率':f"{round(((total_return/amount)**(1/(periods/12))-1)*100,2)}%" ,
                                                        'IRR':f"{round(irr_value*100,2)}%"}
                                num += 1
maturityPayback_df = pd.DataFrame(maturityPayback_dict).T
# print(maturityPayback_df)


writer = pd.ExcelWriter(r"C:\Users\kojun\Desktop\dashboard\data\年金報酬率彙整.xlsx")  
for df,sheetname in zip([principalAndInterestePayack_df,maturityPayback_df],['本息均攤','到期還本']):
    df.to_excel(writer,sheet_name = str(sheetname), header = df.columns, index = False) 
writer.close() 

#畫圖
######################################################################################################################################################

#fig 違約機率分布
fig.add_trace(go.Table(header=dict(values=[column for column in defualt_table.columns],align=['center','center'],font_size = 20,height =50), 
                       cells = dict(values=[defualt_table[column] for column in defualt_table.columns],align=['center','center'],font_size = 22,height =60)) , row=1 , col=1) #違約機率分布(by 件數)
fig.add_trace(go.Scatter(y =y_default ,x = x_default,mode = 'lines',name ='times') , row=1 , col=2) #違約機率分布(by 件數)
fig.update_yaxes(minor=dict(tick0=0),showgrid=False,rangemode='tozero',constraintoward='bottom')
fig.update_layout(xaxis_showgrid=False, yaxis_showgrid=False)

#fig7
fig7.add_trace(go.Table(header=dict(values=[column for column in number.columns],align=['center','center'],font_size = 20,height =50), 
                       cells = dict(values=[number[column] for column in number.columns],align=['center','center'],font_size = 22,height =60)) , row=1 , col=1) 
fig7.add_trace(go.Table(header=dict(values=[column for column in rate_df.columns],align=['center','center'],font_size = 20,height =50), 
                       cells = dict(values=[rate_df[column] for column in rate_df.columns],align=['center','center'],font_size = 22,height =60)) , row=1 , col=2) 
fig7.add_trace(go.Table(header=dict(values=[column for column in combin.columns],align=['center','center'],font_size = 20,height =50), 
                       cells = dict(values=[combin[column] for column in combin.columns],align=['center','center'],font_size = 22,height =60)) , row=1 , col=3)

#逾期30天資料
Defulat30_summary.add_trace(go.Table(header=dict(values=[column for column in df_forecast_summary.columns],align=['center','center'],font_size = 20,height =50), 
                       cells = dict(values=[df_forecast_summary[column] for column in df_forecast_summary.columns],align=['center','center'],font_size = 22,height =60)) , row=1 , col=1) 
Defulat30_summary.add_trace(go.Table(header=dict(values=[column for column in df_forecast30.columns],align=['center','center'],font_size = 20,height =50), 
                       cells = dict(values=[df_forecast30[column] for column in df_forecast30.columns],align=['center','center'],font_size = 22,height =60)) , row=1 , col=2)


#figure_case_summary (每月上架數量及總量)
figure_case_summary.add_trace(go.Bar(x = case_summary['上架日期'],
                      y = case_summary['上架金額'],showlegend = True,name ='上架金額(左)'),row=1 , col=1)
figure_case_summary.add_trace(go.Scatter(x = case_summary['上架日期'],
                      y = case_summary['上架件數'],showlegend = True,name ='上架件數(右)',mode = 'lines+markers'),secondary_y=True,row=1 , col=1)
figure_case_summary.update_yaxes(minor=dict(tick0=0),showgrid=False,rangemode='tozero',constraintoward='bottom' ,secondary_y=True)
figure_case_summary.update_layout(legend=dict(orientation="h",yanchor='top',y=1.1,xanchor='auto',x=0), xaxis_showgrid=False, yaxis_showgrid=False)


#逾催30天明細
trance11 = go.Table(header=dict(values=[column for column in defualt_30_detail.columns],  align='center'), 
                        cells = dict(values=[defualt_30_detail[column] for column in defualt_30_detail.columns] , align='center'))
layout = go.Layout(title={'text':'逾催30天明細(包含已結案逾催)','y':0.85,'x':0.5,'xanchor':'center','yanchor': 'top'})
fig_defualt_30_detail = go.Figure(data = [trance11], layout=layout)
fig_defualt_30_detail.update_layout(xaxis_showgrid=False, yaxis_showgrid=False)

#by案件到期的逾催狀況(合併)
trancedefualtMaturity = go.Table(header=dict(values=[column for column in defualtMaturity_30_combine.columns],  align='center'), 
                        cells = dict(values=[defualtMaturity_30_combine[column] for column in defualtMaturity_30_combine.columns] , align='center'))
layout = go.Layout(title={'text':'以案件到期日計算信房合計逾催','y':0.85,'x':0.5,'xanchor':'center','yanchor': 'top'})
fig_defualtMaturity_30_combine = go.Figure(data = [trancedefualtMaturity], layout=layout)
fig_defualtMaturity_30_combine.update_layout(xaxis_showgrid=False, yaxis_showgrid=False)

#by案件到期的逾催狀況(信)
trancetrancedefualtMaturity_credit = go.Table(header=dict(values=[column for column in defualtMaturity_30_credit.columns],  align='center'), 
                        cells = dict(values=[defualtMaturity_30_credit[column] for column in defualtMaturity_30_credit.columns] , align='center'))
layout = go.Layout(title={'text':'以案件到期日計算信貸逾催','y':0.85,'x':0.5,'xanchor':'center','yanchor': 'top'})
fig_defualtMaturity_30_credit = go.Figure(data = [trancetrancedefualtMaturity_credit], layout=layout)

#by案件到期的逾催狀況(房)
trancetrancetrancedefualtMaturity_house = go.Table(header=dict(values=[column for column in defualtMaturity_30_house.columns],  align='center'), 
                        cells = dict(values=[defualtMaturity_30_house[column] for column in defualtMaturity_30_house.columns] , align='center'))
layout = go.Layout(title={'text':'以案件到期日計算房貸逾催','y':0.85,'x':0.5,'xanchor':'center','yanchor': 'top'})
fig_defualtMaturity_30_house = go.Figure(data = [trancetrancetrancedefualtMaturity_house], layout=layout)


principalAndInterestePayack_df_fig = principalAndInterestePayack_df[['交易手續費' ,'金流維護費','期數' ,'利率' ,'年化報酬率','IRR']]
maturityPayback_df_fig = maturityPayback_df[['交易手續費' ,'金流維護費','期數' ,'利率' ,'年化報酬率','IRR']]

#案件報酬率計算
about_return.add_trace(go.Table(header=dict(values=[column for column in principalAndInterestePayack_df_fig.columns],align=['center','center'],font_size = 20,height =50), 
                       cells = dict(values=[principalAndInterestePayack_df_fig[column] for column in principalAndInterestePayack_df_fig.columns],align=['center','center'],font_size = 22,height =60)) , row=1 , col=1) 
about_return.add_trace(go.Table(header=dict(values=[column for column in maturityPayback_df_fig.columns],align=['center','center'],font_size = 20,height =50), 
                       cells = dict(values=[maturityPayback_df_fig[column] for column in maturityPayback_df_fig.columns],align=['center','center'],font_size = 22,height =60)) , row=1 , col=2)
about_return.update_layout(title={'text':"報酬率統整表(內扣)",'y':0.95,'x':0.5,'xanchor':'center','yanchor': 'top'}) 