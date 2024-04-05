import plotly.graph_objects as go
import sqlite3
import pandas as pd 

import warnings
warnings.filterwarnings('ignore')


#小金認購速度單獨一個dcc.Graph


sugger = pd.read_excel(r'data/sugger.xlsx')

#fig11 小金認購速度
trance11 = go.Table(header=dict(values=[column for column in sugger.columns],  align='center'), 
                        cells = dict(values=[sugger[column] for column in sugger.columns] , align='center'))
layout = go.Layout(title={'text':'各類投資人待回收本金','y':0.85,'x':0.5,'xanchor':'center','yanchor': 'top'})
fig11 = go.Figure(data = [trance11], layout=layout)
