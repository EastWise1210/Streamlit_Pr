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
#add to workspace : 해당 디렉토리의 경로만 조회하기 때문에 폴더가 삭제되면 경로가 무용지물이 됨
#copy folder : 해당 디렉토리를 복사해서 workspace에 적재하기 때문에 원본 폴더 삭제유무 상관 없음