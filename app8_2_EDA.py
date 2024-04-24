import streamlit as st
import pandas as pd

#이용할 코드를 함수로 정의
def run_eda():
    st.subheader('EDA')
    st.text('Exercising Seperating-Files(2)')
    df = pd.read_csv('./data/iris.csv')
    user_select = st.multiselect(label='SELECT', options=df.columns)
    st.dataframe(df[user_select])
    df_corr = df[user_select]

    if user_select != []:
        st.dataframe(df_corr.corr(numeric_only=True))
    else :
        pass













