from plotly.subplots import make_subplots
import plotly.graph_objects as go
import sql_commond as sc
import pandas as pd
import warnings

warnings.filterwarnings('ignore')




#先組fig8框架
fig8 = make_subplots(rows=3,cols=3,
                    specs=[[{'type': 'domain', "rowspan": 3,"colspan": 1}, {'type': 'xy', "rowspan": 3,"colspan": 2}, None],
                            [None, None, None],
                            [None, None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=('正常繳款',
                                    '正常繳款圖'
                                    )
                    )
fig8.update_layout(height=500,width=1900) #調整fig的大小
############################################################
#先組fig9框架
fig9 = make_subplots(rows=3,cols=3,
                    specs=[[{'type': 'domain', "rowspan": 3,"colspan": 1}, {'type': 'xy', "rowspan": 3,"colspan": 2},None],
                            [None, None, None],
                            [None, None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=('遲繳',
                                    '遲繳圖',
                                    )
                    )
fig9.update_layout(height=500,width=1900) #調整fig的大小
############################################################
#先組fig10框架
fig10 = make_subplots(rows=3,cols=3,
                    specs=[[{'type': 'domain', "rowspan": 3,"colspan": 1}, {'type': 'xy', "rowspan": 3,"colspan": 2}, None],
                            [None, None, None],
                            [None, None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=('提前清償',
                                    '提前清償圖'
                                    )
                    )
fig10.update_layout(height=500,width=1900) #調整fig的大小
############################################################
############################################################
sperate_prepay_fig = make_subplots(rows=2,cols=4,
                    specs=[[{'type': 'xy', "rowspan": 2,"colspan": 2},None, {'type': 'xy', "rowspan": 2,"colspan": 2}, None],
                            [None, None, None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=('提前清償案件(信)',
                                    '提前清償案件(房)'
                                    )
                    )
sperate_prepay_fig.update_layout(height=500,width=1900) #調整fig的大小
############################################################
############################################################
sperate_nopay_fig = make_subplots(rows=2,cols=4,
                    specs=[[{'type': 'xy', "rowspan": 2,"colspan": 2},None, {'type': 'xy', "rowspan": 2,"colspan": 2}, None],
                            [None, None, None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=('未繳款案件(信)',
                                    '未繳款案件(房)'
                                    )
                    )
sperate_nopay_fig.update_layout(height=500,width=1900) #調整fig的大小
############################################################
############################################################
sperate_noraml_fig = make_subplots(rows=2,cols=4,
                    specs=[[{'type': 'xy', "rowspan": 2,"colspan": 2},None, {'type': 'xy', "rowspan": 2,"colspan": 2}, None],
                            [None, None, None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=('正常繳款案件(信)',
                                    '正常繳款案件(房)'
                                    )
                    )
sperate_noraml_fig.update_layout(height=500,width=1900) #調整fig的大小
############################################################
############################################################
sperate_late_fig = make_subplots(rows=2,cols=4,
                    specs=[[{'type': 'xy', "rowspan": 2,"colspan": 2},None, {'type': 'xy', "rowspan": 2,"colspan": 2}, None],
                            [None, None, None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=('遲繳案件(信)',
                                    '遲繳案件(房)'
                                    )
                    )
sperate_late_fig.update_layout(height=500,width=1900) #調整fig的大小
############################################################


#叫資料
#借款人行為
nomal = pd.read_excel(r'data/normal.xlsx')
nomal = nomal.groupby('YM')['CNT'].agg('sum').reset_index()
late = pd.read_excel(r'data/late.xlsx')
late = late.groupby('YM')['CNT'].agg('sum').reset_index()
no_pay = pd.read_excel(r'data/nopay.xlsx')
no_pay = no_pay.groupby('YM')['CNT'].agg('sum').reset_index()
Prepaid = pd.read_excel(r'data/prepay.xlsx')
Prepaid = Prepaid.groupby('YM')['CNT'].agg('sum').reset_index()




#案件按照最後一次繳款狀態分類

case_status_now = pd.read_excel(r'data/case_status.xlsx')



#借款人行為2 (拆信房)
separate_normal = pd.read_excel(r'data/normal.xlsx')
separate_late = pd.read_excel(r'data/late.xlsx')
separate_no_pay = pd.read_excel(r'data/nopay.xlsx')
separate_Prepaid = pd.read_excel(r'data/prepay.xlsx')

#正常繳款
credit_normal = separate_normal.loc[separate_normal['type']=='信',['YM','CNT']]
house_normal = separate_normal.loc[separate_normal['type']=='房',['YM','CNT']]
#遲繳
credit_late = separate_late.loc[separate_late['type']=='信',['YM','CNT']]
house_late = separate_late.loc[separate_late['type']=='房',['YM','CNT']]
#沒繳
credit_nopay = separate_no_pay.loc[separate_no_pay['type']=='信',['YM','CNT']]
house_nopay = separate_no_pay.loc[separate_no_pay['type']=='房',['YM','CNT']]
#提前清償
credit_Prepaid = separate_Prepaid.loc[separate_Prepaid['type']=='信',['YM','CNT']]
house_Prepaid = separate_Prepaid.loc[separate_Prepaid['type']=='房',['YM','CNT']]





# #fig8 正常繳款
# fig8.add_trace(go.Table(header=dict(values=[column for column in nomal.columns],align=['center','center'],font_size = 20,height =50), 
#                        cells = dict(values=[nomal[column] for column in nomal.columns],align=['center','center'],font_size = 22,height =60)) , row=1 , col=1) #違約機率分布(by 件數)
# fig8.add_trace(go.Scatter(y =nomal['正常繳款件數'] ,x = nomal['YM'],mode = 'lines',name ='times' ) , row=1 , col=2) 

# #fig9 遲繳
# fig9.add_trace(go.Table(header=dict(values=[column for column in late.columns],align=['center','center'],font_size = 20,height =50), 
#                        cells = dict(values=[late[column] for column in late.columns],align=['center','center'],font_size = 22,height =60)) , row=1 , col=1) #違約機率分布(by 件數)
# fig9.add_trace(go.Scatter(y =late['遲繳件數'] ,x = late['YM'],mode = 'lines',name ='times' ) , row=1 , col=2) 

# #fig10 提前清償
# fig10.add_trace(go.Table(header=dict(values=[column for column in Prepaid.columns],align=['center','center'],font_size = 20,height =50), 
#                        cells = dict(values=[Prepaid[column] for column in Prepaid.columns],align=['center','center'],font_size = 22,height =60)) , row=1 , col=1) #違約機率分布(by 件數)
# fig10.add_trace(go.Scatter(y =Prepaid['提前清償案件數'] ,x = Prepaid['YM'],mode = 'lines',name ='times' ) , row=1 , col=2) 

#正常繳款
sperate_noraml_fig.add_trace(go.Scatter(y =credit_normal['CNT'] ,x = credit_normal['YM'],mode = 'lines',name ='times' ) , row=1 , col=1) 
sperate_noraml_fig.add_trace(go.Scatter(y =house_normal['CNT'] ,x = house_normal['YM'],mode = 'lines',name ='times' ) , row=1 , col=3) 
sperate_noraml_fig.update_yaxes(minor=dict(tick0=0),showgrid=False,rangemode='tozero',constraintoward='bottom' )
sperate_noraml_fig.update_layout(showlegend=False, xaxis_showgrid=False, yaxis_showgrid=False,xaxis2_showgrid=False, yaxis2_showgrid=False)

#提前清償
sperate_prepay_fig.add_trace(go.Scatter(y =credit_Prepaid['CNT'] ,x = credit_Prepaid['YM'],mode = 'lines',name ='times' ) , row=1 , col=1)
sperate_prepay_fig.add_trace(go.Scatter(y =house_Prepaid['CNT'] ,x = house_Prepaid['YM'],mode = 'lines',name ='times' ) , row=1 , col=3) 
sperate_prepay_fig.update_yaxes(minor=dict(tick0=0),showgrid=False,rangemode='tozero',constraintoward='bottom' )
sperate_prepay_fig.update_layout(showlegend=False, xaxis_showgrid=False, yaxis_showgrid=False,xaxis2_showgrid=False, yaxis2_showgrid=False)

#遲繳
sperate_late_fig.add_trace(go.Scatter(y =credit_late['CNT'] ,x = credit_late['YM'],mode = 'lines',name ='times' ) , row=1 , col=1) 
sperate_late_fig.add_trace(go.Scatter(y =house_late['CNT'] ,x = house_late['YM'],mode = 'lines',name ='times' ) , row=1 , col=3) 
sperate_late_fig.update_yaxes(minor=dict(tick0=0),showgrid=False,rangemode='tozero',constraintoward='bottom' )
sperate_late_fig.update_layout(showlegend=False, xaxis_showgrid=False, yaxis_showgrid=False,xaxis2_showgrid=False, yaxis2_showgrid=False)

#未繳
sperate_nopay_fig.add_trace(go.Scatter(y =credit_nopay['CNT'] ,x = credit_nopay['YM'],mode = 'lines',name ='times' ) , row=1 , col=1) 
sperate_nopay_fig.add_trace(go.Scatter(y =house_nopay['CNT'] ,x = house_nopay['YM'],mode = 'lines',name ='times' ) , row=1 , col=3)
sperate_nopay_fig.update_yaxes(minor=dict(tick0=0),showgrid=False,rangemode='tozero',constraintoward='bottom' ) 
sperate_nopay_fig.update_layout(showlegend=False, xaxis_showgrid=False, yaxis_showgrid=False,xaxis2_showgrid=False, yaxis2_showgrid=False)



#fig11 正常、遲繳、無還款比例
trace0 = go.Bar(x = nomal['YM'],y = nomal['CNT'],name = '正常繳款件數')
trace1 = go.Bar(x = late['YM'],y = late['CNT'],name='遲繳件數')
trace2 = go.Bar(x = no_pay['YM'],y = no_pay['CNT'],name='尚未繳款簡述')

layout = go.Layout(title = '借款人繳款狀況',barmode='stack',xaxis={'title':'時間'} ,yaxis={'title':'繳款狀況百分比'})
figure_paymoney_status = go.Figure(data = [trace0,trace1,trace2],layout = layout)
figure_paymoney_status.update_layout(legend=dict(orientation="h",yanchor='top',y=1.1,xanchor='auto',x=0),
                                     xaxis_showgrid=False, yaxis_showgrid=False)

trance0 =go.Bar(y=case_status_now['case_type'] ,x=case_status_now['數量'] ,orientation='h' , text=case_status_now['數量'],textposition = 'inside',showlegend=False,
                marker=dict(color='rgba(18, 7, 80, 0.6)',line=dict(color='rgba(58, 71, 80, 1.0)', width=3)))
layout_case_status = go.Layout(title={'text':'案件狀態','y':0.85,'x':0.5,'xanchor':'center','yanchor': 'top'})
case_typ_class = go.Figure(data = [trance0],layout=layout_case_status)
case_typ_class.update_layout(xaxis_showgrid=False, yaxis_showgrid=False)

