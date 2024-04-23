#이번 내용은 pandas DataFrame을 웹 화면에 보여주는 방법

import streamlit as st
import pandas as pd

def main():
    df = pd.read_csv('./data/iris.csv')
    print(df)

    #화면에 DataFrame 나타내기
    st.dataframe(df)
    
    #species 컬럼의 고유값(unique)을 화면에 표시해보기
    st.write(df['species'].unique())
    st.text('아이리스 붓꽃' + df['species'].unique()+'로 되어 있다.')


if __name__ == '__main__':
    main()



#data folder 끌어올 때 선택 메뉴에서  -->  add to workspace..(x) <-> copy folder(o)