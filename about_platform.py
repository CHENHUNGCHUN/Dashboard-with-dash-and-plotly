from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import datetime
import pandas as pd
import sql_commond as sc

import warnings
warnings.filterwarnings('ignore')

##########################################################################################################################################
#day_period_important =>重要事件
day_period_important = make_subplots(rows=2,cols=2,
                    specs=[[{'type': 'domain', "rowspan": 2,"colspan": 1}, {'type': 'domain', "rowspan": 2,"colspan": 1}],
                            [None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=('重要事件',
                                    '重要事件時間軸',
                                    ),
                    )
day_period_important.update_layout(height=600,width=1900) #調整fig的大小
############################################################################################################################################
##########################################################################################################################################
#figure_amount =>撥款量
figure_amount = make_subplots(rows=3,cols=2,
                    specs=[[{'type': 'domain', "rowspan": 3,"colspan": 1}, {'type': 'domain', "rowspan": 3,"colspan": 1}],
                            [None, None],
                            [None, None]
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=('信撥款量及件數',
                                    '房撥款量及件數',
                                    )
                    )
figure_amount.update_layout(height=700,width=1900) #調整fig的大小
############################################################################################################################################

##########################################################################################################################################
#figure_about_fee =>開辦費+對保費
figure_about_fee = make_subplots(rows=2,cols=2,
                    specs=[[{'type': 'domain', "rowspan": 2,"colspan": 1}, {'type': 'domain', "rowspan": 2,"colspan": 1}],
                            [None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=('信營收',
                                    '房營收',
                                    ),
                    )
figure_about_fee.update_layout(height=600,width=1900) #調整fig的大小
############################################################################################################################################
#讀事件excel檔

day_period = pd.read_excel('day_period.xlsx')

fee = pd.read_excel('fee.xlsx')

appropriation_credit= pd.read_excel('appropriation_credit.xlsx')

appropriation_house = pd.read_excel('appropriation_house.xlsx')

main_case_data = pd.read_excel('main_case_data.xlsx')

fee_data = pd.read_excel('fee_data.xlsx')
fee_data_credit = fee_data.loc[fee_data['type']=='信']
fee_data_house = fee_data.loc[fee_data['type']=='房']
total_fee = fee_data.groupby('YM')['項目A','項目B','項目C','項目D'].agg('sum').reset_index()
total_fee['總營收'] = total_fee.iloc[:,1:].apply(lambda x:x.sum(),axis=1)

case_status2 = pd.read_excel('case_status2.xlsx')


#畫圖圖
#大事記的圖

figure_big =px.line(day_period,x='date',y = '累積淨入金',hover_name=day_period['事件'],hover_data=['date','事件'],
                   title='事件時間軸') #,symbol='事件'    title='事件時間軸'
figure_big.update_traces(showlegend=False,mode='markers',marker=dict(size=15)) #mode='markers'
figure_big.update_xaxes(showgrid=False)
figure_big.update_yaxes(showgrid=False)


#figure_fee (手續費的table)
trance0 = go.Table(header=dict(values=[column for column in fee.columns] ,font_size = 20,height =50, align='center'), 
                        cells = dict(values=[fee[column] for column in fee.columns],font_size = 22,height =60 , align='right'))
layout = go.Layout(title={'text':'總交易手續費收入','y':0.85,'x':0.5,'xanchor':'center','yanchor': 'top'})
figure_fee = go.Figure(data = [trance0],layout = layout)

#figure_amount (撥款量的table)
figure_amount.add_trace(go.Table(header=dict(values=[column for column in appropriation_credit.columns],align=['center'],font_size = 20,height =50,), 
                       cells = dict(values=[appropriation_credit[column] for column in appropriation_credit.columns],align=['right'],font_size = 22,height =60)) , row=1 , col=1)
figure_amount.add_trace(go.Table(header=dict(values=[column for column in appropriation_house.columns],align=['center'],font_size = 20,height =50,), 
                       cells = dict(values=[appropriation_house[column] for column in appropriation_house.columns],align=['right'],font_size = 22,height =60)) , row=1 , col=2)


#figure_apath_amount 
trance0 = go.Table(header=dict(values=[column for column in main_case_data.columns] ,align='center'), 
                        cells = dict(values=[main_case_data[column] for column in main_case_data.columns], align='center'))
layout = go.Layout(title={'text':'各通路撥款狀態','y':0.85,'x':0.5,'xanchor':'center','yanchor': 'top'})
figure_apath_amount = go.Figure(data = [trance0],layout = layout)



figure_about_fee.add_trace(go.Table(header=dict(values=[column for column in fee_data_credit.columns],align=['center'],font_size = 20,height =50), 
                       cells = dict(values=[fee_data_credit[column] for column in fee_data_credit.columns],align=['right'],font_size = 22,height =60)) , row=1 , col=1)
figure_about_fee.add_trace(go.Table(header=dict(values=[column for column in fee_data_house.columns],align=['center'],font_size = 20,height =50), 
                       cells = dict(values=[fee_data_house[column] for column in fee_data_house.columns],align=['right'],font_size = 22,height =60)) , row=1 , col=2)


#figure_totalfee (平台總收益的table)
trance0 = go.Table(header=dict(values=[column for column in total_fee.columns] ,font_size = 20,height =50, align='center'), 
                        cells = dict(values=[total_fee[column] for column in total_fee.columns],font_size = 22,height =60 , align='right'))
layout = go.Layout(title={'text':'平台總收入(僅1.0)','y':0.85,'x':0.5,'xanchor':'center','yanchor': 'top'})
figure_totalfee = go.Figure(data = [trance0],layout = layout)


#figure_examination (甄審平台的初複審過件數)
trance0 = go.Table(header=dict(values=[column for column in case_status2.columns] , align='center'), 
                        cells = dict(values=[case_status2[column] for column in case_status2.columns], align='right'))
layout = go.Layout(title={'text':'初複審過件數','y':0.85,'x':0.5,'xanchor':'center','yanchor': 'top'})
figure_examination = go.Figure(data = [trance0],layout = layout)

