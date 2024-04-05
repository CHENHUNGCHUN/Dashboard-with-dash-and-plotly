import sqlite3
import pandas as pd
import numpy as np
from  datetime import datetime
from dateutil.relativedelta import relativedelta
import sql_commond as sc
import warnings
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from tqdm.contrib import tzip
import glob

warnings.filterwarnings('ignore')


##########################################################################################################################################
#財富管理部
figure_bunny = make_subplots(rows=2,cols=2,
                    specs=[[{'type': 'domain', "rowspan": 2,"colspan": 1}, {'type': 'xy', "rowspan": 2,"colspan": 1,"secondary_y": True}],
                            [None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=('',
                                    '新資金/新增人數走勢圖',
                                    ),
                    )
figure_bunny.update_layout(height=800,width=1900) #調整fig的大小
############################################################################################################################################
##########################################################################################################################################
#財富管理部二部
figure_bunny_2 = make_subplots(rows=2,cols=2,
                    specs=[[{'type': 'domain', "rowspan": 2,"colspan": 1}, {'type': 'xy', "rowspan": 2,"colspan": 1,"secondary_y": True}],
                            [None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=('',
                                    '新資金/新增人數走勢圖',
                                    ),
                    )
figure_bunny.update_layout(height=800,width=1900) #調整fig的大小
############################################################################################################################################
##########################################################################################################################################
#資金通路經營部
figure_gina = make_subplots(rows=2,cols=2,
                    specs=[[{'type': 'domain', "rowspan": 2,"colspan": 1}, {'type': 'xy', "rowspan": 2,"colspan": 1,"secondary_y": True}],
                            [None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=('',
                                    '新資金/新增人數走勢圖',
                                    ),
                    )
figure_gina.update_layout(height=800,width=1900) #調整fig的大小
############################################################################################################################################
##########################################################################################################################################
#VIP會員經營部
figure_vip = make_subplots(rows=2,cols=2,
                    specs=[[{'type': 'domain', "rowspan": 2,"colspan": 1}, {'type': 'xy', "rowspan": 2,"colspan": 1,"secondary_y": True}],
                            [None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=('',
                                    '新資金/新增人數走勢圖',
                                    ),
                    )
figure_vip.update_layout(height=800,width=1900) #調整fig的大小
############################################################################################################################################
##########################################################################################################################################
#VIP會員經營部
figure_mgm = make_subplots(rows=2,cols=2,
                    specs=[[{'type': 'domain', "rowspan": 2,"colspan": 1}, {'type': 'xy', "rowspan": 2,"colspan": 1,"secondary_y": True}],
                            [None, None],
                            ],
                    horizontal_spacing=0.03,vertical_spacing=0.08,
                    subplot_titles=('',
                                    '新資金/新增人數走勢圖',
                                    ),
                    )
figure_mgm.update_layout(height=800,width=1900) #調整fig的大小
#######################################################################################################################################
buuny_df3 = pd.read_excel(r'data/buuny_df3.xlsx')
buuny_df3_2 =pd.read_excel(r'data/buuny_df3_2.xlsx')
gina_df3 =pd.read_excel(r'data/gina_df3.xlsx')
vip_df3 = pd.read_excel(r'data/vip_df3.xlsx')
mgm_df =pd.read_excel(r'data/mgm_df.xlsx')

#######################################################################################################################################


figure_bunny.add_trace(go.Table(header=dict(values=[column for column in buuny_df3.columns] , align='center'), 
                        cells = dict(values=[buuny_df3[column] for column in buuny_df3.columns] , align='center')), row=1 , col=1)
figure_bunny.add_trace(go.Bar(x = buuny_df3['日期'],
                      y = buuny_df3['新增資金'],showlegend = True,name ='新資金',marker_color='blue'), row=1 , col=2) #,marker_color=buuny_df2['Color']
figure_bunny.add_trace(go.Scatter(x = buuny_df3['日期'],
                      y = buuny_df3['第一次交易'],showlegend = True,name ='新增客戶(右)',mode = 'lines',marker_color='red'),secondary_y=True, row=1 , col=2)
figure_bunny.update_yaxes(minor=dict(tick0=0),showgrid=False,rangemode='tozero',constraintoward='bottom' ,secondary_y=True)
figure_bunny.update_layout(title={'text':f"一部(總交易人數 {buuny_df3['第一次交易'].sum()}人)",'y':0.9,'x':0.205,'xanchor':'center','yanchor': 'top','font':dict(size=50)},
                           height=500,width=2000,
                           legend=dict(orientation="h",yanchor='top',y=1.1,xanchor='right',x=0.58),
                           xaxis_showgrid=False, yaxis_showgrid=False) #xaxis_showgrid=False, yaxis_showgrid=False 關掉x跟y軸的網格


figure_bunny_2.add_trace(go.Table(header=dict(values=[column for column in buuny_df3_2.columns] , align='center'), 
                        cells = dict(values=[buuny_df3_2[column] for column in buuny_df3_2.columns] , align='center')), row=1 , col=1)
figure_bunny_2.add_trace(go.Bar(x = buuny_df3_2['日期'],
                      y = buuny_df3_2['新增資金'],showlegend = True,name ='新資金',marker_color='blue'), row=1 , col=2) #,marker_color=buuny_df2['Color']
figure_bunny_2.add_trace(go.Scatter(x = buuny_df3_2['日期'],
                      y = buuny_df3_2['第一次交易'],showlegend = True,name ='新增客戶(右)',mode = 'lines',marker_color='red'),secondary_y=True, row=1 , col=2)
figure_bunny_2.update_yaxes(minor=dict(tick0=0),showgrid=False,rangemode='tozero',constraintoward='bottom' ,secondary_y=True)
figure_bunny_2.update_layout(title={'text':f"二部(總交易人數 {buuny_df3_2['第一次交易'].sum()}人)",'y':0.9,'x':0.205,'xanchor':'center','yanchor': 'top','font':dict(size=50)},
                           height=500,width=2000,
                           legend=dict(orientation="h",yanchor='top',y=1.1,xanchor='right',x=0.58),
                           xaxis_showgrid=False, yaxis_showgrid=False) #xaxis_showgrid=False, yaxis_showgrid=False 關掉x跟y軸的網格



gina_df2 = gina_df3.copy().sort_values('日期')
gina_df2['ma_6'] = gina_df2['新增資金'].rolling(6).mean().fillna(0) #會少6期,先補0
gina_df2 = gina_df2.sort_values('日期',ascending=False)
# print(gina_df2)
figure_gina.add_trace(go.Table(header=dict(values=[column for column in gina_df3.columns] , align='center'),  
                        cells = dict(values=[gina_df3[column] for column in gina_df3.columns] , align='center')), row=1 , col=1) 
figure_gina.add_trace(go.Bar(x = gina_df2['日期'],
                      y = gina_df2['新增資金'],showlegend = True,name ='新資金',marker_color='blue'), row=1 , col=2)  #,marker_color=gina_df2['Color']
figure_gina.add_trace(go.Scatter(x = gina_df2['日期'],
                      y = gina_df2['ma_6'],showlegend = True,name ='6個月平均新資金',mode = 'lines',marker_color='green'), row=1 , col=2)
figure_gina.update_layout(title={'text':f"通路部(總交易人數 {gina_df3['第一次交易'].sum()}人)",'y':0.9,'x':0.21,'xanchor':'center','yanchor': 'top','font':dict(size=50)},
                           height=500,width=2000,
                           legend=dict(orientation="h",yanchor='top',y=1.1,xanchor='right',x=0.60),
                           xaxis_showgrid=False, yaxis_showgrid=False) #xaxis_showgrid=False, yaxis_showgrid=False 關掉x跟y軸的網格


figure_vip.add_trace(go.Table(header=dict(values=[column for column in vip_df3.columns] , align='center'),  
                        cells = dict(values=[vip_df3[column] for column in vip_df3.columns] , align='center')), row=1 , col=1) 
figure_vip.add_trace(go.Bar(x = vip_df3['日期'],
                      y = vip_df3['新增資金'],showlegend = True,name ='新資金',marker_color='blue'), row=1 , col=2) #,marker_color=vip_df2['Color']
figure_vip.add_trace(go.Scatter(x = vip_df3['日期'],
                      y = vip_df3['第一次交易'],showlegend = True,name ='新增客戶(右)',mode = 'lines',marker_color='red'),secondary_y=True, row=1 , col=2)
figure_vip.update_yaxes(minor=dict(tick0=0),showgrid=False,rangemode='tozero',constraintoward='bottom' ,secondary_y=True)
figure_vip.update_layout(title={'text':f"客服部(總交易人數 {vip_df3['第一次交易'].sum()}人)",'y':0.9,'x':0.21,'xanchor':'center','yanchor': 'top','font':dict(size=50)},
                           height=500,width=2000,
                           legend=dict(orientation="h",yanchor='top',y=1.1,xanchor='right',x=0.58),
                           xaxis_showgrid=False, yaxis_showgrid=False) #xaxis_showgrid=False, yaxis_showgrid=False 關掉x跟y軸的網格


figure_mgm.add_trace(go.Table(header=dict(values=[column for column in mgm_df.columns] , align='center'),  
                        cells = dict(values=[mgm_df[column] for column in mgm_df.columns] , align='center')), row=1 , col=1) 
figure_mgm.add_trace(go.Bar(x = mgm_df['日期'],
                      y = mgm_df['新增資金'],showlegend = True,name ='新資金',marker_color='blue'), row=1 , col=2) #,marker_color=vip_df2['Color']
figure_mgm.add_trace(go.Scatter(x = mgm_df['日期'],
                      y = mgm_df['第一次交易'],showlegend = True,name ='新增客戶(右)',mode = 'lines',marker_color='red'),secondary_y=True, row=1 , col=2)
figure_mgm.update_yaxes(minor=dict(tick0=0),showgrid=False,rangemode='tozero',constraintoward='bottom' ,secondary_y=True)
figure_mgm.update_layout(title={'text':f"員工(總交易人數 {mgm_df['第一次交易'].sum()}人)",'y':0.9,'x':0.19,'xanchor':'center','yanchor': 'top','font':dict(size=50)},
                           height=500,width=2000,
                           legend=dict(orientation="h",yanchor='top',y=1.1,xanchor='right',x=0.58),
                           xaxis_showgrid=False, yaxis_showgrid=False) #xaxis_showgrid=False, yaxis_showgrid=False 關掉x跟y軸的網格



#######################################################################################################################################
