from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import sql_commond as sc
from  datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta
import numpy as np

import warnings
warnings.filterwarnings('ignore')



##############################################################
#invester_behave(about invester)
invester_behave = make_subplots(rows=2,
                    cols=2,
                    specs=[
                            [{'type': 'domain', "rowspan": 2,"colspan": 1}, {'type': 'domain', "rowspan": 2,"colspan": 1}],
                            [None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=(
                                    '小金行為組合' ,
                                     '小金行為組合(百分比)' 
                                    )
                    )
##############################################################
#先組fig2框架(about invester)
fig2 = make_subplots(rows=3,cols=3,
                    specs=[
                            
                            [{'type': 'domain', "rowspan": 3,"colspan": 1}, {'type': 'xy', "rowspan": 3,"colspan": 2,"secondary_y": True}, None],
                            [None, None, None],
                            [ None, None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=(
                                    '小金月認購金額(包含2.0)',
                                    '小金月認購金額圖(包含2.0)'
                                    ),
                    )
##############################################################
#先組fig3框架(about invester)
fig3 = make_subplots(rows=3,cols=3,
                    specs=[
                            [{'type': 'domain', "rowspan": 3,"colspan": 1}, {'type': 'domain', "rowspan": 3,"colspan": 2}, None],
                            [None, None, None],
                            [ None, None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=(
                                    '小金購買案件傾向' ,
                                     '小金購買案件傾向圖' 
                                    )
                    )
##############################################################
#先組fig4框架(about invester)
fig4 = make_subplots(rows=3,cols=3,
                    specs=[
                            [{'type': 'domain', "rowspan": 3,"colspan": 1}, {'type': 'xy', "rowspan": 3,"colspan": 2,"secondary_y": True}, None],
                            [None, None, None],
                            [None, None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=(
                                    '小金每月出入金' ,
                                    '小金累積淨入金' 
                                    )
                    )
##############################################################
##############################################################
#先組inorout框架(about invester)
inorout = make_subplots(rows=3,cols=2,
                    specs=[
                            [{'type': 'xy', "rowspan": 3,"colspan": 1}, {'type': 'xy', "rowspan": 3,"colspan": 1}],
                            [None, None],
                            [None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=(
                                    '小金每月入金走勢' ,
                                    '小金每月出金走勢' 
                                    )
                    )
##############################################################
#先組fig5框架(about invester)
fig5 = make_subplots(rows=3,cols=3,
                    specs=[
                            [{'type': 'domain', "rowspan": 3,"colspan": 1}, {'type': 'xy', "rowspan": 3,"colspan": 2,"secondary_y": True}, None],
                            [None, None, None],
                            [ None, None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=(
                                    '小金帳戶餘額' ,
                                    '小金帳戶餘額圖' 
                                    )
                    )
##############################################################
#先組fig15框架(about invester)
fig15 = make_subplots(rows=3,cols=3,
                    specs=[
                            [{'type': 'domain', "rowspan": 3,"colspan": 1}, {'type': 'xy', "rowspan": 3,"colspan": 2}, None],
                            [None, None, None],
                            [ None, None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=(
                                    '小金週購買習慣' ,
                                    '小金週購買習慣圖' 
                                    )
                    )
##############################################################
#先組fig16框架(about invester)
fig16 = make_subplots(rows=3,
                    cols=3,
                    specs=[
                            [{'type': 'domain', "rowspan": 3,"colspan": 1}, {'type': 'xy', "rowspan": 3,"colspan": 2}, None],
                            [None, None, None],
                            [ None, None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=(
                                    '小金月購買習慣' ,
                                     '小金月購買習慣圖' 
                                    )
                    )
##############################################################
today = datetime.today().date()#今天日期
last_1 = today - relativedelta(months=1)#上個月
last_2 = today - relativedelta(months=2)#上上個月
last_3 = today - relativedelta(months=3)#上上上個月

last_0_y,last_0_m = today.strftime('%Y.%m.%d').split('.')[:2]
last_1_y,last_1_m = last_1.strftime('%Y.%m.%d').split('.')[:2]
last_2_y,last_2_m = last_2.strftime('%Y.%m.%d').split('.')[:2]
last_3_y,last_3_m = last_3.strftime('%Y.%m.%d').split('.')[:2]
#先組inv_habit框架(about invester)
inv_habit = make_subplots(rows=4,
                    cols=4,
                    specs=[
                            [{'type': 'xy', "rowspan": 2,"colspan": 2},None,{'type': 'xy', "rowspan": 2,"colspan": 2},None],
                            [None, None, None,None],
                            [{'type': 'xy', "rowspan": 2,"colspan": 2},None,{'type': 'xy', "rowspan": 2,"colspan": 2},None],
                            [ None, None, None,None],
                            ],
                    horizontal_spacing=0.08,vertical_spacing=0.18,
                    
                    subplot_titles=(
                                    f'{last_0_m}月' ,
                                    f'{last_1_m}月' ,
                                    f'{last_2_m}月' ,
                                    f'{last_3_m}月' 
                                    ),
                    )
##############################################################
##############################################################
#先組fig2框架(about invester)
sleep = make_subplots(rows=3,cols=3,
                    specs=[
                            
                            [{'type': 'domain', "rowspan": 3,"colspan": 1}, {'type': 'xy', "rowspan": 3,"colspan": 2,"secondary_y": True}, None],
                            [None, None, None],
                            [ None, None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=(
                                    '沉睡客戶表(包含2.0)',
                                    '沉睡客戶圖_距離上一次交易超過90天(包含2.0)'
                                    ),
                    )
##############################################################

#小金認購速度
fig2_data = pd.read_excel('fig2_data.xlsx')


#小金每月行為 
#每個投資人的每月的每項行為都只會認列一個,故組合也只會有一個。 ex:A 入金+交易,則僅會列入"入金+交易"的行為,不會再列入"入金"或"交易"
behaviers = pd.read_excel('behaviers.xlsx')
behaviers_table_pct = behaviers.copy().apply(lambda x :round(x/x['總人數']*100,2) ,axis=1)
behaviers_table_pct = behaviers_table_pct.iloc[:,:-1]

#小金每月認購金額
invest_1_bar_table = pd.read_excel('invest_1_bar_table.xlsx')

#小金購買案件傾向
df = pd.read_excel('pie.xlsx')
pie = []
for time in ("202312","202311","202310","202309"):
    pie.append(df.loc[df['銷帳時間']==time,])




########################################################################################################################################################
#畫圖圖 
invester_behave.add_trace(go.Table(header=dict(values=[column for column in behaviers.columns]), 
                                   cells = dict(values=[behaviers[column] for column in behaviers.columns])), row=1 , col=1)
invester_behave.add_trace(go.Table(header=dict(values=[column for column in behaviers.columns]), 
                                   cells = dict(values=[behaviers_table_pct[column] for column in behaviers_table_pct.columns])), row=1 , col=2)



#小金認購速度單獨一個dcc.Graph
trance0 = go.Table(header=dict(values=[column for column in fig2_data.columns] ,align='center'), 
                        cells = dict(values=[fig2_data[column] for column in fig2_data.columns], align='center'))
layout = go.Layout(title={'text':'小金認購速度(已含2.0)','y':0.85,'x':0.5,'xanchor':'center','yanchor': 'top'})
fig_speed = go.Figure(data = [trance0], layout=layout)


#fig2 當月小金認購總額
fig2.add_trace(go.Table(header=dict(values=[column for column in invest_1_bar_table.columns] , align='center'),  #fill_color = 'paleturquoise'
                        cells = dict(values=[invest_1_bar_table[column] for column in invest_1_bar_table.columns] , align='center')), row=1 , col=1) #fill_color = 'lavender' ,
fig2.add_trace(go.Bar(x = invest_1_bar_table['YM'],
                      y = invest_1_bar_table['當月小金認購總額'],showlegend = True,name ='當月認購金額'), row=1 , col=2)
fig2.add_trace(go.Scatter(x = invest_1_bar_table['YM'],
                      y = invest_1_bar_table['排重複_當月下單人數'],showlegend = True,name ='排重複_當月下單人數(右)',mode = 'lines'),secondary_y=True, row=1 , col=2)
fig2.update_yaxes(minor=dict(tick0=0),showgrid=False,rangemode='tozero',constraintoward='bottom' ,secondary_y=True)
fig2.update_yaxes(minor=dict(tick0=0),showgrid=False,rangemode='tozero',constraintoward='bottom' ,secondary_y=False)
fig2.update_layout(height=500,width=2000,legend=dict(orientation="h",yanchor='top',y=1.1,xanchor='right',x=0.48),
                   xaxis_showgrid=False, yaxis_showgrid=False)


#fig4 小金每月出入金
x0 = pd.read_excel('x0.xlsx')
x2 = x0.groupby('YM')['小金_總金額'].agg('sum').reset_index().sort_values('YM')
x2['cumsum'] = x2['小金_總金額'].cumsum()
x2['Color'] = np.where(x2['小金_總金額']<0,'red','rgb(0,0,255)')
fig4.add_trace(go.Table(header=dict(values=[column for column in x0.columns]), cells = dict(values=[x0[column] for column in x0.columns])), row=1 , col=1)
fig4.add_trace(go.Scatter(y =x2['cumsum'] ,x = x2['YM'],showlegend = True,mode = 'lines',name ='累積淨入金' ) , row=1 , col=2)
fig4.add_trace(go.Bar(y =x2['小金_總金額'] ,x = x2['YM'],showlegend = True,marker_color=x2['Color'] ,name ='當月淨流入/流出(右)', opacity=0.1 ),secondary_y=True , row=1 , col=2) #,mode = 'lines'
fig4.update_yaxes(minor=dict(tick0=0),showgrid=False,rangemode='tozero',constraintoward='bottom')
fig4.update_layout(legend=dict(orientation="h",yanchor='top',y=1.1,xanchor='right',x=0.47),
                   height=500,width=2000,xaxis_showgrid=False, yaxis_showgrid=False) #調整fig的大小


#inorout 小金每月出入金拆細節
inandout_df = pd.read_excel('x0.xlsx')
inandout_df = inandout_df.sort_values('YM')
inorout.add_trace(go.Bar(y =inandout_df.loc[inandout_df['remake']=='匯入資金','小金_總金額'] ,x = inandout_df.loc[inandout_df['remake']=='匯入資金','YM'],showlegend = False,name ='/month') , row=1 , col=1) # mode = 'lines'
inorout.add_trace(go.Scatter(y =inandout_df.loc[inandout_df['remake']=='匯入資金','小金_總金額'].rolling(6).mean() ,x = inandout_df.loc[inandout_df['remake']=='匯入資金','YM'],mode = 'lines',showlegend = False,name ='/month') , row=1 , col=1)
inorout.add_trace(go.Bar(y =inandout_df.loc[inandout_df['remake']=='退回資金','小金_總金額'] ,x = inandout_df.loc[inandout_df['remake']=='退回資金','YM'],showlegend = False,name ='/month',marker_color='red') , row=1 , col=2) # mode = 'lines'
inorout.add_trace(go.Scatter(y =inandout_df.loc[inandout_df['remake']=='退回資金','小金_總金額'].rolling(6).mean() ,x = inandout_df.loc[inandout_df['remake']=='退回資金','YM'],mode = 'lines',showlegend = False,name ='/month',marker_color='black') , row=1 , col=2) 
inorout.update_yaxes(minor=dict(tick0=0),showgrid=False,rangemode='tozero',constraintoward='bottom')
inorout.update_layout(height=500,width=1900,xaxis_showgrid=False, yaxis_showgrid=False)


#fig5 小金帳戶餘額
df3 = pd.read_excel('df3.xlsx')
fig5.add_trace(go.Table(header=dict(values=[column for column in df3.columns]), cells = dict(values=[df3[column] for column in df3.columns])),row=1 , col=1)
fig5.add_trace(go.Scatter(y =df3['小金帳戶餘額'] ,x = df3['date'],mode = 'lines',name ='小金帳戶餘額' ) , row=1 , col=2)
fig5.add_trace(go.Scatter(x = df3['date'],
                      y = df3['不為零的帳戶數'],showlegend = True,name ='不為零的帳戶數(右)',mode = 'lines'),secondary_y=True, row=1 , col=2)
fig5.update_yaxes(minor=dict(tick0=0),showgrid=False,rangemode='tozero',constraintoward='bottom' ,secondary_y=True)
fig5.update_yaxes(minor=dict(tick0=0),showgrid=False,rangemode='tozero',constraintoward='bottom' ,secondary_y=False)
fig5.update_layout(height=500,width=2000,legend=dict(orientation="h",yanchor='top',y=1.1,xanchor='right',x=0.47),
                   xaxis_showgrid=False, yaxis_showgrid=False) #height=500,width=2000


#fig15 小金週購買
week = pd.read_excel('week.xlsx')

week1 = week.loc[week['type'] == 1,['day_of_week','小金投資金額']]
week_las_week = week.loc[week['type'] == 2,['day_of_week','小金投資金額']]
week = week.loc[week['type'] == 0,['day_of_week','小金投資金額']]
fig15.add_trace(go.Table(header=dict(values=[column for column in week.columns]), 
                         cells = dict(values=[week[column] for column in week.columns])),row=1 , col=1)
fig15.add_trace(go.Scatter(y =week1['小金投資金額'] ,x = week1['day_of_week'],mode = 'lines',name ='average' ) , row=1 , col=2)
fig15.add_trace(go.Scatter(y =week_las_week['小金投資金額'] ,x = week1['day_of_week'],mode = 'lines',name ='last_week' ) , row=1 , col=2)
fig15.update_layout(legend=dict(orientation="h",yanchor='top',y=1.1,xanchor='right',x=0.45),
                    xaxis_showgrid=False, yaxis_showgrid=False) #height=500,width=1900


#fig16 小金月購買
month = pd.read_excel('month.xlsx')
fig16.add_trace(go.Table(header=dict(values=[column for column in month.columns]), cells = dict(values=[month[column] for column in month.columns])),row=1 , col=1)
fig16.add_trace(go.Scatter(y =month['小金投資金額'] ,x = month['M'],mode = 'lines',name ='mean' ) , row=1 , col=2)
year_list = month['Y'].unique()
year_list.sort()
for year in year_list:
    fig16.add_trace(go.Scatter(y =month.loc[month['Y']==year,'小金投資金額'] ,x = month.loc[month['Y']==year,'M'],mode = 'lines',name =str(year)) , row=1 , col=2)
fig16.update_yaxes(minor=dict(tick0=0),showgrid=False,rangemode='tozero',constraintoward='bottom' ,secondary_y=True)
fig16.update_yaxes(minor=dict(tick0=0),showgrid=False,rangemode='tozero',constraintoward='bottom' ,secondary_y=False)
fig16.update_layout(
                    legend=dict(orientation="h",yanchor='top',y=1.1,xanchor='right',x=0.60),
                    xaxis_showgrid=False, yaxis_showgrid=False) #height=500,width=1900,


#inv_habit 小金購買傾向
positions = [(1,1),(1,3),(3,1),(3,3)]
for trace,position in zip(pie,positions):
        inv_habit.add_trace(go.Bar(y=trace['案件上架日'] ,x=trace['占比'] ,orientation='h' , text=trace['占比'].apply(lambda x:str(x)+'%') ,textposition = 'inside',showlegend=False,marker=dict(color='rgba(18, 7, 80, 0.6)',
                                                                                                                                                                       line=dict(color='rgba(58, 71, 80, 1.0)', width=3)))
                        ,row =position[0] ,col =position[1])
inv_habit.update_layout(
                        title ={'text':'小金購買傾向',
                                'x':0.5,
                                'xanchor': 'center','yanchor': 'top',
                                },
                                xaxis_showgrid=False, yaxis_showgrid=False,
                                xaxis2_showgrid=False, yaxis2_showgrid=False,
                                xaxis3_showgrid=False, yaxis3_showgrid=False,
                                xaxis4_showgrid=False, yaxis4_showgrid=False) #font={'size':50}   #height=800,width=1900,


#sleep 沉睡客戶
sleep_cus = pd.read_excel('sleep_cus.xlsx')
sleep.add_trace(go.Table(header=dict(values=[column for column in sleep_cus.columns] , align='center'),  #fill_color = 'paleturquoise'
                        cells = dict(values=[sleep_cus[column] for column in sleep_cus.columns] , align='center')), row=1 , col=1) #fill_color = 'lavender' ,
sleep.add_trace(go.Scatter(x = sleep_cus['times'],
                      y = sleep_cus['count'],showlegend = True,name ='沉睡人數(左)',mode = 'lines'), row=1 , col=2)
sleep.add_trace(go.Scatter(x = sleep_cus['times'],
                      y = sleep_cus['pct'],showlegend = True,name ='沉睡人數占比(右)',mode = 'lines'),secondary_y=True, row=1 , col=2)
sleep.update_yaxes(minor=dict(tick0=0),showgrid=False,rangemode='tozero',constraintoward='bottom' ,secondary_y=True)
sleep.update_yaxes(minor=dict(tick0=0),showgrid=False,rangemode='tozero',constraintoward='bottom' ,secondary_y=False)
sleep.update_layout(height=500,width=2000,legend=dict(orientation="h",yanchor='top',y=1.1,xanchor='right',x=0.47),
                    xaxis_showgrid=False, yaxis_showgrid=False)


#每月新交易會員廣告來源
newMember_ws = pd.read_excel('newMember_ws.xlsx')
trance0 = go.Table(header=dict(values=[column for column in newMember_ws.columns] ,align='center'), 
                        cells = dict(values=[newMember_ws[column] for column in newMember_ws.columns], align='center'))
layout = go.Layout(title={'text':'每月新交易會員廣告來源','y':0.85,'x':0.5,'xanchor':'center','yanchor': 'top'})
fig_newMember_ws = go.Figure(data = [trance0], layout=layout)


#每月留存率
serviver_df = pd.read_excel('serviver_df.xlsx')
trance0 = go.Table(header=dict(values=[column for column in serviver_df.columns] ,align='center'), 
                        cells = dict(values=[serviver_df[column] for column in serviver_df.columns], align='center'))
layout = go.Layout(title={'text':'客戶留存率','y':0.85,'x':0.5,'xanchor':'center','yanchor': 'top'})
fig_servive = go.Figure(data = [trance0], layout=layout)


#最後一筆交易距離今天天數
last_purchase_df = pd.read_excel('last_purchase_df.xlsx')
trance0 = go.Bar(y = last_purchase_df['距離上次購買的天數'],
                      x = last_purchase_df['CNT'],
                      orientation='h' ,textposition = 'inside',showlegend=False ,text= last_purchase_df['CNT'],
                      marker=dict(color='rgba(18, 7, 80, 0.6)',line=dict(color='rgba(58, 71, 80, 1.0)', width=3)))
layout = go.Layout(title={'text':'距離上次購買天數分類(人數)','y':0.85,'x':0.5,'xanchor':'center','yanchor': 'top'})
fig_last_purchase = go.Figure(data = [trance0], layout=layout)
fig_last_purchase.update_layout(xaxis_showgrid=False, yaxis_showgrid=False)


#CAI
cai_df = pd.read_excel('cai_df.xlsx')
trance0 = go.Scatter(x = cai_df['date'],
                      y = cai_df['nagative'],showlegend = True,name ='nagative',mode = 'lines')
trance01 = go.Scatter(x = cai_df['date'],
                      y = cai_df['positive'],showlegend = True,name ='positive',mode = 'lines')
layout = go.Layout(title={'text':'CAI index','y':0.85,'x':0.5,'xanchor':'center','yanchor': 'top'})
fig_cai = go.Figure(data = [trance0,trance01], layout=layout)
fig_cai.update_yaxes(minor=dict(tick0=0),showgrid=False,rangemode='tozero',constraintoward='bottom')
fig_cai.update_layout(legend=dict(orientation="h",yanchor='top',y=1.1,xanchor='auto',x=0),
                         xaxis_showgrid=False, yaxis_showgrid=False)


#忠誠客戶
loyalty = pd.read_excel('loyalty.xlsx')
trance0 = go.Bar(y = loyalty['等級'],
                      x = loyalty['CNT'],
                      orientation='h' ,textposition = 'inside',showlegend=False ,text=loyalty.values,
                      marker=dict(color='rgba(18, 7, 80, 0.6)',line=dict(color='rgba(58, 71, 80, 1.0)', width=3)))
layout = go.Layout(title={'text':'忠誠客戶分類(by 交易頻率)','y':0.85,'x':0.5,'xanchor':'center','yanchor': 'top'})
fig_loyalty = go.Figure(data = [trance0], layout=layout)
fig_loyalty.update_layout(xaxis_showgrid=False, yaxis_showgrid=False)

