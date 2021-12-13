import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from streamlit.elements import multiselect, plotly_chart

st.set_page_config(page_title='안전장비 착용률',
                    page_icon=':chart_with_upwards_trend:',
                    layout='wide'
                    )



df = pd.read_csv('7time.csv')
df1 = pd.read_csv('m.csv')
df2 = pd.read_csv('q.csv')
df3 = pd.read_csv('yday.csv')





#--------SIDEBAR----------
st.sidebar.header('FILTER')
연도=st.sidebar.multiselect(
    '연도 선택',
    options=df['연도'].unique(),
    default=df['연도'].unique() 
)

분기=st.sidebar.multiselect(
    '분기 선택',
    options=df2['분기'].unique(),
    default=df2['분기'].unique()
)

월=st.sidebar.multiselect(
    '월 선택',
    options=df1['월'].unique(), 
    default=df1['월'].unique() 
    )

일=st.sidebar.multiselect(
    '일 선택',
    options=df['일'].unique(),
    default=df['일'].unique()
)

시간=st.sidebar.multiselect(
    '시간 선택',
    options=df['시간'].unique(),
    default=df['시간'].unique()
)

# 헬멧착용률=st.sidebar.multiselect(
#     '헬멧착용률 선택',
#     options=df['헬멧착용률'].unique()
# )

# 조끼착용률=st.sidebar.multiselect(
#     '조끼착용률 선택',
#     options=df['조끼착용률'].unique()
#     )

df_selection=df.query(
    '연도 == @연도 & 월 == @월 & 일 == @일 & 시간 == @시간'
)

df1_selection=df1.query(
    '연도 == @연도 & 월 == @월'
)

df2_selection=df2.query(
    '연도 == @연도 & 분기 == @분기'
)

df3_selection=df3.query(
    '연도 == @연도 & 월 == @월 & 일 == @일 & 시간 == @시간'
)




# st.dataframe(df_selection & df1_selection & df2_selection & df3_selection)

# -------MAINPAGE--------
st.title(':chart_with_upwards_trend:안전장비 착용률')
st.markdown('##')

# TOP KPI's
주간평균헬멧착용률 = round(df_selection['헬멧착용률(%)'].mean(),1)
주간평균조끼착용률 = round(df_selection['조끼착용률(%)'].mean(),1)
# 별표1 = ":star:" * int(round(평균헬멧착용률/10,0))
# 별표2 = ":star:" * int(round(평균조끼착용률/10,0))
월간평균헬멧착용률 = round(df1_selection['헬멧착용률(%)'].mean(),1)
월간평균조끼착용률 = round(df1_selection['조끼착용률(%)'].mean(),1)

분기평균헬멧착용률 = round(df2_selection['헬멧착용률(%)'].mean(),1)
분기평균조끼착용률 = round(df2_selection['조끼착용률(%)'].mean(),1)

어제평균헬멧착용률 = round(df3_selection['헬멧착용률(%)'].mean(),1)
어제평균조끼착용률 = round(df3_selection['조끼착용률(%)'].mean(),1)

left_column1, right_column1,left_column2, right_column2,left_column3, right_column3,left_column4, right_column4 = st.columns(8)
with left_column1:
    st.subheader('전일 헬멧착용률(%)') 
    st.subheader(f'{어제평균헬멧착용률}%')
with right_column1:
    st.subheader('전일 조끼착용률(%)')
    st.subheader(f'{어제평균조끼착용률}%')
with left_column2:
    st.subheader('주간 헬멧착용률(%)') 
    st.subheader(f'{주간평균헬멧착용률}%')
with right_column2:
    st.subheader('주간 조끼착용률(%)')
    st.subheader(f'{주간평균조끼착용률}%')
with left_column3:
    st.subheader('월간 헬멧착용률(%)') 
    st.subheader(f'{월간평균헬멧착용률}%')
with right_column3:
    st.subheader('월간 조끼착용률(%)')
    st.subheader(f'{월간평균조끼착용률}%')
with left_column4:
    st.subheader('분기 헬멧착용률(%)') 
    st.subheader(f'{분기평균헬멧착용률}%')
with right_column4:
    st.subheader('분기 조끼착용률(%)')
    st.subheader(f'{분기평균조끼착용률}%')



st.markdown('---')

# helmet line chart
yday_average_helmet = (
    df3_selection.groupby(['시간']).mean()[['헬멧착용률(%)']]
)

yday_helmet = px.line(
    yday_average_helmet,
    x=yday_average_helmet.index,
    y='헬멧착용률(%)',
    title = '<b>전일 헬멧착용률</b>',
    color_discrete_sequence=['#0083B8']*len(yday_average_helmet),
    template='plotly_white',
)



yday_helmet.update_layout(
    xaxis=dict(tickmode='linear'),
    plot_bgcolor='rgba(0,0,0,0)',
    yaxis=(dict(showgrid=False))
    )

# st.plotly_chart(yday_helmet)

# vest line chart
yday_average_vest = (
    df3_selection.groupby(['시간']).mean()[['조끼착용률(%)']]
)

yday_vest = px.line(
    yday_average_vest,
    x=yday_average_vest.index,
    y='조끼착용률(%)',
    title = '<b>전일 조끼착용률</b>',
    color_discrete_sequence=['#0083B8']*len(yday_average_vest),
    template='plotly_white',
)
yday_vest.update_layout(
    xaxis=dict(tickmode='linear'),
    plot_bgcolor='rgba(0,0,0,0)',
    yaxis=(dict(showgrid=False))
    )

# st.plotly_chart(yday_vest)

left_column, right_column = st.columns(2)
left_column.plotly_chart(yday_helmet, use_container_width=True)
right_column.plotly_chart(yday_vest, use_container_width=True)


# helmet line chart
weekly_average_helmet = (
    df_selection.groupby(['일']).mean()[['헬멧착용률(%)']]
)

weekly_helmet = px.line(
    weekly_average_helmet,
    x=weekly_average_helmet.index,
    y='헬멧착용률(%)',
    title = '<b>주간 헬멧착용률</b>',
    color_discrete_sequence=['#0083B8']*len(weekly_average_helmet),
    template='plotly_white',
)
weekly_helmet.update_layout(
    xaxis=dict(tickmode='linear'),
    plot_bgcolor='rgba(0,0,0,0)',
    yaxis=(dict(showgrid=False))
    )

# st.plotly_chart(week_helmet)

# vest line chart
weekly_average_vest = (
    df_selection.groupby(['일']).mean()[['조끼착용률(%)']]
)

weekly_vest = px.line(
    weekly_average_vest,
    x=weekly_average_vest.index,
    y='조끼착용률(%)',
    title = '<b>주간 조끼착용률</b>',
    color_discrete_sequence=['#0083B8']*len(weekly_average_vest),
    template='plotly_white',
)
weekly_vest.update_layout(
    xaxis=dict(tickmode='linear'),
    plot_bgcolor='rgba(0,0,0,0)',
    yaxis=(dict(showgrid=False))
    )

# st.plotly_chart(week_vest)
left_column, right_column = st.columns(2)
left_column.plotly_chart(weekly_helmet, use_container_width=True)
right_column.plotly_chart(weekly_vest, use_container_width=True)

# helmet line chart
monthly_average_helmet = (
    df1_selection.groupby(['월']).mean()[['헬멧착용률(%)']]
)

monthly_helmet = px.line(
    monthly_average_helmet,
    x=monthly_average_helmet.index,
    y='헬멧착용률(%)',
    title = '<b>월간 헬멧착용률</b>',
    color_discrete_sequence=['#0083B8']*len(monthly_average_helmet),
    template='plotly_white',
)
monthly_helmet.update_layout(
    xaxis=dict(tickmode='linear'),
    plot_bgcolor='rgba(0,0,0,0)',
    yaxis=(dict(showgrid=False))
    )

# st.plotly_chart(week_helmet)

# vest line chart
monthly_average_vest = (
    df1_selection.groupby(['월']).mean()[['조끼착용률(%)']]
)

monthly_vest = px.line(
    monthly_average_vest,
    x=monthly_average_vest.index,
    y='조끼착용률(%)',
    title = '<b>월간 조끼착용률</b>',
    color_discrete_sequence=['#0083B8']*len(monthly_average_vest),
    template='plotly_white',
)
monthly_vest.update_layout(
    xaxis=dict(tickmode='linear'),
    plot_bgcolor='rgba(0,0,0,0)',
    yaxis=(dict(showgrid=False))
    )

# st.plotly_chart(week_vest)
left_column, right_column = st.columns(2)
left_column.plotly_chart(monthly_helmet, use_container_width=True)
right_column.plotly_chart(monthly_vest, use_container_width=True)

# helmet line chart
quarterly_average_helmet = (
    df2_selection.groupby(['분기']).mean()[['헬멧착용률(%)']]
)

quarterly_helmet = px.line(
    quarterly_average_helmet,
    x=quarterly_average_helmet.index,
    y='헬멧착용률(%)',
    title = '<b>분기 헬멧착용률</b>',
    color_discrete_sequence=['#0083B8']*len(quarterly_average_helmet),
    template='plotly_white',
)
quarterly_helmet.update_layout(
    xaxis=dict(tickmode='linear'),
    plot_bgcolor='rgba(0,0,0,0)',
    yaxis=(dict(showgrid=False))
    )

# st.plotly_chart(week_helmet)

# vest line chart
quarterly_average_vest = (
    df2_selection.groupby(['분기']).mean()[['조끼착용률(%)']]
)

quarterly_vest = px.line(
    quarterly_average_vest,
    x=quarterly_average_vest.index,
    y='조끼착용률(%)',
    title = '<b>분기 조끼착용률</b>',
    color_discrete_sequence=['#0083B8']*len(quarterly_average_vest),
    template='plotly_white',
)
quarterly_vest.update_layout(
    xaxis=dict(tickmode='linear'),
    plot_bgcolor='rgba(0,0,0,0)',
    yaxis=(dict(showgrid=False))
    )

# st.plotly_chart(week_vest)
left_column, right_column = st.columns(2)
left_column.plotly_chart(quarterly_helmet, use_container_width=True)
right_column.plotly_chart(quarterly_vest, use_container_width=True)

# # vest line chart
# monthly_average_vest = (
#     df_selection.groupby(['월']).mean()[['조끼착용률']]
# )

# fig_vest = px.line(
#     monthly_average_vest,
#     x=monthly_average_vest.index,
#     y='조끼착용률',
#     title = '<b>월별 조끼착용률</b>',
#     color_discrete_sequence=['#0083B8']*len(monthly_average_vest),
#     template='plotly_white',
# )

# fig_vest.update_layout(
#     xaxis=dict(tickmode='linear'),
#     plot_bgcolor='rgba(0,0,0,0)',
#     yaxis=(dict(showgrid=False))
# )

# # st.plotly_chart(fig_vest)

# left_column, right_column = st.columns(2)
# left_column.plotly_chart(fig_helmet, use_container_width=True)
# right_column.plotly_chart(fig_vest, use_container_width=True)

#---------HIDE STREAMLIT STYLE ----------
hide_st_style = '''
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                '''
st.markdown(hide_st_style, unsafe_allow_html=True)