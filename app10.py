#streamlit의 내장 차트 함수
#plotly 차트 : Python의 유명한 웹 페이지용 라이브러리



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


def main():
    #스트림릿에서 제공해주는 차트
    #line_chart, area_chart


    df = pd.read_csv('./data/lang_data.csv')
    
    column_list = df.columns[1:]
    sel_col_list = st.multiselect(label='Choose your language', options=column_list)

    if len(sel_col_list) != 0:
        df_sel = df[sel_col_list]
        st.dataframe(df_sel)

        #line[선] 그래프 형태
        st.line_chart(df_sel)

        #area[영역, 범위] 그래프 형태
        st.area_chart(df_sel)


    df2 = pd.read_csv('./data/iris.csv')
    #streamlit이 제공하는 <bar chart>
    df_iris = df2.iloc[:,0:-1]
    st.bar_chart(df_iris)

    #streamlit이 제공하는 <map>
    df3 = pd.read_csv('./data/location.csv', index_col=0)
    st.map(df3)


    #plotly의 pie chart
    df4 = pd.read_csv('./data/prog_languages_data.csv', index_col=0)
    fig1 = px.pie(data_frame=df4, names='lang', values='Sum', title='Using ratio about prog-lang')
    st.plotly_chart(fig1)


    #plotly의 bar chart
    df5 = df4.sort_values('Sum', ascending=False)
    fig2 = px.bar(data_frame=df5, x='lang', y='Sum', title='Bar Chart Expression about prog-lang')
    st.plotly_chart(fig2)


if __name__ == '__main__':
    main()