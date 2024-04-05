import dash
from dash import html,dcc
import plotly.io as pio
from dash.dependencies import Input,Output
import about_invester as invester
import about_sugerdaddy as suger
import about_borrower as borrower
import about_case as case
import about_platform as platform
import about_platform_group as platform_group
from data import *

import warnings
warnings.filterwarnings('ignore')

#################################################################################################

pio.renderers.default = 'browser'

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
#################################################################################################
app =dash.Dash()
app.layout = html.Div([
    
    #新組織用
    html.Div([
    html.H1('About Platform(GROUP) 含2.0',style={'textAlign': 'center','fontSize': 50,'backgroundColor': colors['background'],'color': colors['text']}), #,style={'textAlign': 'center','color': colors['text'],'fontSize': 40}
    html.Div(id='platform_group',children=['The Data For GROUP Performant'],style={'textAlign': 'center','fontSize': 30,'backgroundColor': colors['background'],'color': colors['text']}), #style={'textAlign': 'center','color': colors['text'],'fontSize': 30}
    ],style={'backgroundColor': colors['background']}),

    html.Div([
    dcc.Download(id="bunny-download"),
    dcc.Graph(id='bunny',figure=platform_group.figure_bunny), #財富管理部
    html.Button("Download Data", id="bunny_csv",n_clicks=0,style={'textAlign': 'right','fontSize': 25,
                                                                'position':'relative','left':'1600px','bottom':'60px',})
    ]),

    html.Div([
    dcc.Download(id="bunny_2-download"),
    dcc.Graph(id='bunny_2',figure=platform_group.figure_bunny_2), #財富管理部二部
    html.Button("Download Data", id="bunny_2_csv",n_clicks=0,style={'textAlign': 'right','fontSize': 25,
                                                                'position':'relative','left':'1600px','bottom':'60px',})
    ]),

    html.Div([
    dcc.Download(id="gina-download"),
    dcc.Graph(id='gina',figure=platform_group.figure_gina), #資金通路經營部
    html.Button("Download Data", id="gina_csv",n_clicks=0,style={'textAlign': 'right','fontSize': 25,
                                                                'position':'relative','left':'1600px','bottom':'60px',})
    ]),

    html.Div([
    dcc.Download(id="vip-download"),
    dcc.Graph(id='vip',figure=platform_group.figure_vip), #VIP會員經營部
    html.Button("Download Data", id="vip_csv",n_clicks=0,style={'textAlign': 'right','fontSize': 25,
                                                                'position':'relative','left':'1600px','bottom':'60px',})
    ]),

    html.Div([
    dcc.Download(id="mgm-download"),
    dcc.Graph(id='mgm',figure=platform_group.figure_mgm), #MGM經營部
    html.Button("Download Data", id="mgm_csv",n_clicks=0,style={'textAlign': 'right','fontSize': 25,
                                                                'position':'relative','left':'1600px','bottom':'60px',})
    ]),

    #####################################################################################################################################################################
    #業績
    html.Div([
    html.H1('About Platform',style={'textAlign': 'center','fontSize': 50,'backgroundColor': colors['background'],'color': colors['text']}), #,style={'textAlign': 'center','color': colors['text'],'fontSize': 40}
    html.Div(id='platform',children=['The Data For Sales Performant'],style={'textAlign': 'center','fontSize': 30,'backgroundColor': colors['background'],'color': colors['text']}), #style={'textAlign': 'center','color': colors['text'],'fontSize': 30}
    ],style={'backgroundColor': colors['background']}),
   
    html.Div([
        dcc.Download(id="important_event-download"),
        dcc.Graph(id='big_things',figure=platform.figure_big), #事件時間軸  #figure_big ,day_period_important
        html.Button("Download Data", id="important_event_csv",n_clicks=0,style={'textAlign': 'right','fontSize': 25,
                                                                    'position':'relative','left':'1600px','bottom':'65px',})
    ]),
    dcc.Graph(id='appropriation-credit',figure=platform.figure_amount), #撥款量

    html.Div([
    dcc.Download(id="reviewresult-download"),
    dcc.Graph(id='review_result',figure=platform.figure_examination), #初複審過件數
    html.Button("Download Data", id="reviewresult_csv",n_clicks=0,style={'textAlign': 'right','fontSize': 25,
                                                                'position':'relative','left':'1600px','bottom':'65px',})
    ]),

    dcc.Graph(id='fee',figure=platform.figure_fee),#交易手續費
    dcc.Graph(id='appropriation-about-fee',figure=platform.figure_about_fee), #對保費+開辦費
    html.Div([
        dcc.Download(id="path-download"),
        dcc.Graph(id='appropriation-path_amount',figure=platform.figure_apath_amount), #信通路撥款狀況
        html.Button("Download Data", id="appropriationpath_csv",n_clicks=0,style={'textAlign': 'right','fontSize': 25,
                                                                    'position':'relative','left':'1600px','bottom':'65px',})
    ]),
    dcc.Graph(id='totol_fee',figure=platform.figure_totalfee), #總手續費
    #####################################################################################################################################################################
    #小金
    html.Div([
    html.H1('About invester',style={'textAlign': 'center','fontSize': 50,'backgroundColor': colors['background'],'color': colors['text']}), #,style={'textAlign': 'center','color': colors['text'],'fontSize': 40}
    html.Div(id='invester',children=['The Data For All Invester (without Suger Daddy)'],style={'textAlign': 'center','fontSize': 30,'backgroundColor': colors['background'],'color': colors['text']}),  #style={'textAlign': 'center','color': colors['text'],'fontSize': 30}
    ],style={'backgroundColor': colors['background']}),
    html.Div([
        dcc.Download(id="invester_behave-download"),
        dcc.Graph(id='invester_behave',figure=invester.invester_behave),
        html.Button("Download Data", id="invester_behave_csv",n_clicks=0,style={'textAlign': 'right','fontSize': 25,
                                                                    'position':'relative','left':'1600px','bottom':'65px',})
    ]),

    html.Div([
        dcc.Download(id="speed-download"),
        dcc.Graph(id='speed',figure=invester.fig_speed),
        html.Button("Download Data", id="btn_csv",n_clicks=0,style={'textAlign': 'right','fontSize': 25,
                                                                    'position':'relative','left':'1600px','bottom':'65px',})
    ]),
    html.Div([
    dcc.Download(id="newMember_ws-download"),
    dcc.Graph(id='newMember_ws',figure=invester.fig_newMember_ws), #新增會員及廣告來源
    html.Button("Download Data", id="newMember_csv",n_clicks=0,style={'textAlign': 'right','fontSize': 25,
                                                                'position':'relative','left':'1600px','bottom':'65px',})
    ]),
    html.Div([
    dcc.Download(id="serviver-download"),
    dcc.Graph(id='servive-number',figure=invester.fig_servive), #客戶留存率
    html.Button("Download Data", id="serviver_csv",n_clicks=0,style={'textAlign': 'right','fontSize': 25,
                                                                'position':'relative','left':'1600px','bottom':'65px',})
    ]),

    # html.Div([
    # dcc.Download(id="memeber_classify-download"),
    # dcc.Graph(id='memeber_classify',figure=invester.fig_memberClass), #穩穩客戶分級
    # html.Button("Download Data", id="memeber_classify_csv",n_clicks=0,style={'textAlign': 'right','fontSize': 25,
    #                                                             'position':'relative','left':'1600px','bottom':'55px',})
    # ]),

    html.Div([
    dcc.Download(id="loyal_final_df-download"),
    dcc.Graph(id='loyalty-index',figure=invester.fig_loyalty), #忠誠客戶
    html.Button("Download Data", id="loyal_csv",n_clicks=0,style={'textAlign': 'right','fontSize': 25,
                                                                'position':'relative','left':'1600px','bottom':'65px',})
    ]),

    dcc.Graph(id='last_purchase-number',figure=invester.fig_last_purchase), #距離上次交易天數
    dcc.Graph(id='CAI-index',figure=invester.fig_cai), #CAI指標
    dcc.Graph(id='sleep-number',figure=invester.sleep), #沉睡客(距離上一次交易超過90天)
    dcc.Graph(id='buy-number',figure=invester.fig2),


    html.Div([
    dcc.Download(id="investerNetincome-download"),
    dcc.Graph(id='investerNetincome',figure=invester.fig4), #小金淨入金
    html.Button("Download Data", id="investerNetincome_csv",n_clicks=0,style={'textAlign': 'right','fontSize': 25,
                                                                'position':'relative','left':'1600px','bottom':'20px',})
    ]),

    html.Div([
    dcc.Download(id="investermoneyinorout-download"),
    dcc.Graph(id='invester-account-inorout',figure=invester.inorout),#小金出入金拆出來
    html.Button("Download Data", id="investermoneyinorout_csv",n_clicks=0,style={'textAlign': 'right','fontSize': 25,
                                                                'position':'relative','left':'1600px','bottom':'20px',})
    ]),
    
    dcc.Graph(id='invester-account-amount',figure=invester.fig5),#小金帳戶餘額
    dcc.Graph(id='week-buy',figure=invester.fig15), #小金每周購買狀況

    html.Div([
    dcc.Download(id="month-buy-download"),
    dcc.Graph(id='month-buy',figure=invester.fig16), #小金每月購買狀況
    html.Button("Download Data", id="month-buy_csv",n_clicks=0,style={'textAlign': 'right','fontSize': 25,
                                                                'position':'relative','left':'1600px','bottom':'35px',})
    ]),
    dcc.Graph(id='case_habit',figure=invester.inv_habit), #小金購買習性
    #####################################################################################################################################################################
    #大金
    html.Div([
    html.H1('Suger Daddy',style={'textAlign': 'center','fontSize': 50,'backgroundColor': colors['background'],'color': colors['text']}), #,style={'textAlign': 'center','color': colors['text'],'fontSize': 40}
    html.Div(id='big size',children=['The Data For Suger Daddy'],style={'textAlign': 'center','fontSize': 30,'backgroundColor': colors['background'],'color': colors['text']}), #style={'textAlign': 'center','color': colors['text'],'fontSize': 30}
    ],style={'backgroundColor': colors['background']}),
    html.Div([
        dcc.Download(id="suger-download"),
        dcc.Graph(id='suger',figure=suger.fig11),
        html.Button("Download Data", id="suger_csv",n_clicks=0,style={'textAlign': 'right','fontSize': 25,
                                                                      'position':'relative','left':'1600px','bottom':'65px',
                                                                      'verticalAlign':'top'})
    ]),
    # dcc.Graph(id='suger-pocket',figure=suger.fig12),
    #####################################################################################################################################################################
    #借款人
    html.Div([
    html.H1('About Borrower',style={'textAlign': 'center','fontSize': 50,'backgroundColor': colors['background'],'color': colors['text']}), #,style={'textAlign': 'center','color': colors['text'],'fontSize': 40}
    html.Div(id='borrow',children=['The Data For All Borrower'],style={'textAlign': 'center','fontSize': 30,'backgroundColor': colors['background'],'color': colors['text']}), #style={'textAlign': 'center','color': colors['text'],'fontSize': 30}
    ],style={'backgroundColor': colors['background']}),
    dcc.Graph(id='case_status_now',figure=borrower.case_typ_class), #案件狀態分類
    dcc.Graph(id='borrower-behavier-payment-status',figure=borrower.figure_paymoney_status), #借款人繳款狀況堆疊圖
    dcc.Graph(id='borrower-behavier-normal',figure=borrower.sperate_noraml_fig), #借款人正常繳款數
    dcc.Graph(id='borrower-behavier-late',figure=borrower.sperate_late_fig), #借款人遲繳繳款數
    dcc.Graph(id='borrower-behavier-prepaid',figure=borrower.sperate_prepay_fig), #提前清償圖
    dcc.Graph(id='borrower-behavier-nopay',figure=borrower.sperate_nopay_fig), #沒繳圖

    #####################################################################################################################################################################
    #案件狀態
    html.Div([
    html.H1('About Case',style={'textAlign': 'center','fontSize': 50,'backgroundColor': colors['background'],'color': colors['text']}), #,style={'textAlign': 'center','color': colors['text'],'fontSize': 40}
    html.Div(id='case',children=['The Data For Cases status'],style={'textAlign': 'center','fontSize': 30,'backgroundColor': colors['background'],'color': colors['text']}), #style={'textAlign': 'center','color': colors['text'],'fontSize': 30}
    ],style={'backgroundColor': colors['background']}),
    dcc.Graph(id='case_summary',figure=case.figure_case_summary),
    dcc.Graph(id='default',figure=case.fig),


    html.Div([
    dcc.Download(id="readyINTOdefualt-download"),
    dcc.Graph(id='default_30',figure=case.Defulat30_summary), #每月進入逾催及預計本月再增件數/量    以及下載即將逾催案件明細下載
    html.Button("Download Data", id="readyINTOdefualt_csv",n_clicks=0,style={'textAlign': 'right','fontSize': 25,
                                                                'position':'relative','left':'1600px','bottom':'65px',})
    ]),


    html.Div([
    dcc.Download(id="fig_defualt_30_detail-download"),
    dcc.Graph(id='default_30_detail',figure=case.fig_defualt_30_detail), #逾催30天明細
    html.Button("Download Data", id="30_detail_csv",n_clicks=0,style={'textAlign': 'right','fontSize': 25,
                                                                'position':'relative','left':'1600px','bottom':'65px',})
    ]),

    html.Div([
    dcc.Download(id="fig_defualtMaturity_30_combine-download"),
    dcc.Graph(id='defualtMaturity_combine',figure=case.fig_defualtMaturity_30_combine), #用到期日計算逾催(信房合計)
    html.Button("Download Data", id="defualtMaturity_combine_csv",n_clicks=0,style={'textAlign': 'right','fontSize': 25,
                                                                'position':'relative','left':'1600px','bottom':'65px',})
    ]),

    
    html.Div([
    dcc.Download(id="fig_defualtMaturity_30_credit-download"),
    dcc.Graph(id='defualtMaturity_credit',figure=case.fig_defualtMaturity_30_credit), #用到期日計算逾催(信)
    html.Button("Download Data", id="defualtMaturity_credit_csv",n_clicks=0,style={'textAlign': 'right','fontSize': 25,
                                                                'position':'relative','left':'1600px','bottom':'65px',})
    ]),

    
    html.Div([
    dcc.Download(id="fig_defualtMaturity_30_house-download"),
    dcc.Graph(id='defualtMaturity_house',figure=case.fig_defualtMaturity_30_house), #用到期日計算逾催(房)
    html.Button("Download Data", id="defualtMaturity_house_csv",n_clicks=0,style={'textAlign': 'right','fontSize': 25,
                                                                'position':'relative','left':'1600px','bottom':'65px',})
    ]),

    
    dcc.Graph(id='case_type',figure=case.fig7),
    dcc.Graph(id='return_summary',figure=case.about_return),  #報酬率統整


    
    ]) #,style={'backgroundColor': colors['background']}

#####################################################################################################################################################################
#download

#各通路撥款狀態的下載
@app.callback(Output('path-download' , 'data'),
              [Input('appropriationpath_csv','n_clicks')],
              prevent_initial_call=True)
def path_down(n_clicks_btn):
    return dcc.send_data_frame(platform.main_case_data.to_excel,'WinWin_path.xlsx', index=False)

#認購速度的下載
@app.callback(Output('speed-download' , 'data'),
              [Input('btn_csv','n_clicks')],
              prevent_initial_call=True)
def speed_down(n_clicks_btn):
    return dcc.send_data_frame(invester.fordownload.to_excel,'invester_speed.xlsx', index=False)

#小金占比的下載
@app.callback(Output('suger-download' , 'data'),
              [Input('suger_csv','n_clicks')],
              prevent_initial_call=True)
def suger_down(n_clicks_btn):
    sugger = suger.sugger
    sugger = sugger.sort_values(['year','month'])
    return dcc.send_data_frame(sugger.to_excel,'各類投資人待回收占比.xlsx', index=False)

#通路初複審過件數的下載
@app.callback(Output('reviewresult-download' , 'data'),
              [Input('reviewresult_csv','n_clicks')],
              prevent_initial_call=True)
def suger_down(n_clicks_btn):
    return dcc.send_data_frame(platform.case_status.to_excel,'reviewresult.xlsx', index=False)

#小金行為組合的下載
@app.callback(Output('invester_behave-download' , 'data'),
              [Input('invester_behave_csv','n_clicks')],
              prevent_initial_call=True)
def suger_down(n_clicks_btn):
    return dcc.send_data_frame(invester.behaviers_table.to_excel,'reviewresult.xlsx', index=False)

#重要事件的下載
@app.callback(Output('important_event-download' , 'data'),
              [Input('important_event_csv','n_clicks')],
              prevent_initial_call=True)
def suger_down(n_clicks_btn):
    return dcc.send_data_frame(platform.output_important.to_excel,'important_event.xlsx', index=False)

#新會員廣告來源的下載
@app.callback(Output('newMember_ws-download' , 'data'),
              [Input('newMember_csv','n_clicks')],
              prevent_initial_call=True)
def sleep_down(n_clicks_btn):
    return dcc.send_data_frame(invester.newMember_ws.to_excel,'newMember_ws.xlsx', index = False)

#客戶留存率的下載
@app.callback(Output('serviver-download' , 'data'),
              [Input('serviver_csv','n_clicks')],
              prevent_initial_call=True)
def servive_down(n_clicks_btn):
    return dcc.send_data_frame(invester.serviver_df.to_excel,'serviver.xlsx', index = False)

#逾催30天明細下載
@app.callback(Output('fig_defualt_30_detail-download' , 'data'),
              [Input('30_detail_csv','n_clicks')],
              prevent_initial_call=True)
def defulat30Detail_down(n_clicks_btn):
    return dcc.send_data_frame(case.defualt_30_detail.to_excel,'defualt_30_detail.xlsx', index = False)

#忠誠客戶下載
@app.callback(Output('loyal_final_df-download' , 'data'),
              [Input('loyal_csv','n_clicks')],
              prevent_initial_call=True)
def loyal_down(n_clicks_btn):
    return dcc.send_data_frame(invester.loyal_final_df.to_excel,'loyal_final_df.xlsx', index = False)

#小金淨入金下載
@app.callback(Output('investerNetincome-download' , 'data'),
              [Input('investerNetincome_csv','n_clicks')],
              prevent_initial_call=True)
def investerNetincome_down(n_clicks_btn):
    return dcc.send_data_frame(invester.output_investerNetincome.to_excel,'investerNetincome.xlsx', index = False)

#小金拆出來入金跟出金
@app.callback(Output('investermoneyinorout-download' , 'data'),
              [Input('investermoneyinorout_csv','n_clicks')],
              prevent_initial_call=True)
def investerNetincome_down(n_clicks_btn):
    return dcc.send_data_frame(invester.x0.to_excel,'investermoneyinorout.xlsx', index = False)


#用到期日判斷逾催下載(信房合併)
@app.callback(Output('fig_defualtMaturity_30_combine-download' , 'data'),
              [Input('defualtMaturity_combine_csv','n_clicks')],
              prevent_initial_call=True)
def defualtMaturity_combine_down(n_clicks_btn):
    return dcc.send_data_frame(case.defualtMaturity_30_combine.to_excel,'defualtMaturity_30_combine.xlsx', index = False)

#用到期日判斷逾催下載(信)
@app.callback(Output('fig_defualtMaturity_30_credit-download' , 'data'),
              [Input('defualtMaturity_credit_csv','n_clicks')],
              prevent_initial_call=True)
def defualtMaturity_combine_credit(n_clicks_btn):
    return dcc.send_data_frame(case.defualtMaturity_30_credit.to_excel,'defualtMaturity_30_credit.xlsx', index = False)

#用到期日判斷逾催下載(房)
@app.callback(Output('fig_defualtMaturity_30_house-download' , 'data'),
              [Input('defualtMaturity_house_csv','n_clicks')],
              prevent_initial_call=True)
def defualtMaturity_combine_dhouse(n_clicks_btn):
    return dcc.send_data_frame(case.defualtMaturity_30_house.to_excel,'defualtMaturity_30_house.xlsx', index = False)

#財富管理部下載
@app.callback(Output('bunny-download' , 'data'),
              [Input('bunny_csv','n_clicks')],
              prevent_initial_call=True)
def defualtMaturity_combine_dhouse(n_clicks_btn):
    return dcc.send_data_frame(platform_group.buuny_df.to_excel,'財富管理部.xlsx', index = False)

#財富管理部二部下載
@app.callback(Output('bunny_2-download' , 'data'),
              [Input('bunny_2_csv','n_clicks')],
              prevent_initial_call=True)
def defualtMaturity_combine_dhouse(n_clicks_btn):
    return dcc.send_data_frame(platform_group.buuny_df_2.to_excel,'財富管理部二部.xlsx', index = False)

#資金通路經營部下載
@app.callback(Output('gina-download' , 'data'),
              [Input('gina_csv','n_clicks')],
              prevent_initial_call=True)
def defualtMaturity_combine_dhouse(n_clicks_btn):
    return dcc.send_data_frame(platform_group.gina_df.to_excel,'資金通路部.xlsx', index = False)

#VIP會員經營部下載
@app.callback(Output('vip-download' , 'data'),
              [Input('vip_csv','n_clicks')],
              prevent_initial_call=True)
def defualtMaturity_combine_dhouse(n_clicks_btn):
    return dcc.send_data_frame(platform_group.vip_df.to_excel,'VIP部.xlsx', index = False)

#員工MGM經營部下載
@app.callback(Output('mgm-download' , 'data'),
              [Input('mgm_csv','n_clicks')],
              prevent_initial_call=True)
def defualtMaturity_combine_dhouse(n_clicks_btn):
    return dcc.send_data_frame(platform_group.mgm_df.to_excel,'員工MGM.xlsx', index = False)

# #穩穩客戶分級下載
# @app.callback(Output('memeber_classify-download' , 'data'),
#               [Input('memeber_classify_csv','n_clicks')],
#               prevent_initial_call=True)
# def defualtMaturity_combine_dhouse(n_clicks_btn):
#     return dcc.send_data_frame(invester.member_calssify_df.to_excel,'穩穩客戶分級.xlsx', index = False)

#即將進入逾催細項下載
@app.callback(Output('readyINTOdefualt-download' , 'data'),
              [Input('readyINTOdefualt_csv','n_clicks')],
              prevent_initial_call=True)
def defualtMaturity_combine_dhouse(n_clicks_btn):
    return dcc.send_data_frame(case.payoffLate_list.to_excel,'即將進入於催明細.xlsx', index = False)

#小金每月購買下載
@app.callback(Output('month-buy-download' , 'data'),
              [Input('month-buy_csv','n_clicks')],
              prevent_initial_call=True)
def defualtMaturity_combine_dhouse(n_clicks_btn):
    return dcc.send_data_frame(invester.month.to_excel,'小金每月購買金額.xlsx', index = False)





if __name__ =='__main__':
    app.run_server("0.0.0.0", 8000)  #8000是port ,"0.0.0.0"是ip  ,debug=True






