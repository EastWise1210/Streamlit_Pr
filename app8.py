#파일을 분리해서 개발하는 방법

#파일을 분리하는 이유?
#1. 업무 분담 가능  -->  생산성 증대
#2. 효율적인 디버깅 가능  -->  개발 기간 단축


import streamlit as st
from app8_1_Home import run_home
from app8_2_EDA import run_eda
from app8_3_ML import run_ml
from app8_4_MAbout import run_ma


def main():
    st.title('Seperating Files')
    menu = ['Home', 'EDA', 'ML', 'More About']
    side_sel_menu = st.sidebar.selectbox(label='MENU', options=menu)


    #선택 사항에 따라 조건 흐름
    if side_sel_menu == menu[0]:
        run_home()

    elif side_sel_menu == menu[1]:
        run_eda()

    elif side_sel_menu == menu[2]:
        run_ml()

    else :
        run_ma()



if __name__ == '__main__':
    main()