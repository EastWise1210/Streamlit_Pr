#UI(User Interface) 관련 함수들(checkbox, buttonm text 등등)

import streamlit as st
import pandas as pd


def main():
    df = pd.read_csv('./data/iris.csv')
    
    #버튼 만들기  -->  버튼 누르면 데이터프레임 보여주는 기능 추가
    if st.button(label='Show DataFrame'):
        st.dataframe(df)


    #'대문자' 버튼을 만들고, 버튼 누르면 species 컬럼의 값들을 대문자로 변경한 DataFrame 보여주기
    if st.button(label='CAPITAL'):
        df['species'] = df['species'].str.upper()
        st.dataframe(df)


    #버튼을 안 눌렀을 때 동작 설정하기
    if st.button(label='TEST'):
        df['species'] = df['species'].str.upper()
        st.dataframe(df)
    else :
        st.text('Click to this')
    

    #라디오 버튼 : (나열형) 여러개 중에 단일 선택
    #my_order = ['오름차순 정렬', '내림차순 정렬', '선택 없음']
    #st.radio(label='SELECT', options=my_order)


    #라디오 버튼 선택사항 중 택일 시 이벤트 부여하기  -->  ex) petal_length 컬럼으로 정렬해서 df 보여주기
    my_order = ['오름차순 정렬', '내림차순 정렬', '선택 없음']
    status = st.radio(label='SELECT', options=my_order)
    if status == my_order[0]:
        st.dataframe(df.sort_values('petal_length'))
    elif status == my_order[1]:
        st.dataframe(df.sort_values('petal_length', ascending=False))
    else : 
        st.dataframe(df)


    #체크박스 : 둘 중 하나만 선택(체크 / 해제)
    #ex)체크하면 헤드 5개 보여주고, 해제하면 안 보여주기
    check = st.checkbox(label='SHOW HEAD(5)')  #bool=True 설정해놓으면 기본적으로 자동 체크되어 있음
    if check == True:
        st.dataframe(df.head(5))
    else :
        pass

    
    #셀렉트 박스 : (목록형) 여러개 중 단일 선택  -->  ex)선택 항목에 따라 메세지 표시하기
    my_select_list = ['Python', 'Java', 'C', 'C++', 'C#', 'Go', 'PHP', 'JavaScript', 'Kotlin']
    sel_box = st.selectbox(label='Choose Your Favorite Programming Language', options=my_select_list)
    if sel_box == my_select_list[0]:
        st.text('Your Choice is ' + my_select_list[0] + ' I like too!')
    elif sel_box == my_select_list[1]:
        st.text('Your Choice is ' + my_select_list[1] + ' I like too!')
    elif sel_box == my_select_list[2]:
        st.text('Your Choice is ' + my_select_list[2] + ' I like too!')
    elif sel_box == my_select_list[3]:
        st.text('Your Choice is ' + my_select_list[3] + ' I like too!')
    elif sel_box == my_select_list[4]:
        st.text('Your Choice is ' + my_select_list[4] + ' I like too!')
    elif sel_box == my_select_list[5]:
        st.text('Your Choice is ' + my_select_list[5] + ' I like too!')
    elif sel_box == my_select_list[6]:
        st.text('Your Choice is ' + my_select_list[6] + ' I like too!')
    elif sel_box == my_select_list[7]:
        st.text('Your Choice is ' + my_select_list[7] + ' I like too!')
    else :
        st.text('Your Choice is ' + my_select_list[8] + ' I like too!')


    #멀티 셀렉트 : 여러개 중 다중 선택
    my_choice_list = st.multiselect(label='Choose Your All Favorite Thing', options=df.columns)
    if my_choice_list == []: #이하와 상등 len(my_choice_list) == 0
        pass
    else :
        st.text('This DataFrame shows your selected items')
        st.dataframe(df[my_choice_list])
    #if문 코드 구성할 때 : 1.프론트엔드->정상 case부터 설정  /  2.백엔드->비정상 case부터 설정


    #슬라이더 : 주로 숫자 조정할 때 사용된다
    #st.slider(label='Data', min_value=-5.0, max_value=10.5, value=0.0, step=0.5)   #min_value:최솟값  max_value:최댓값  value:초깃값  step:오프셋 크기
    #ex) 1세부터 120세까지 범위 중 사용자 선택 슬라이더 만들기
    age = st.slider(label='Age', min_value=1, max_value=120, value=1, step=1)  #변수에 할당해서 print() 찍어보면 해당 값이 들어오는걸 알 수 있음
    #ex)"선택한 나이는 00세입니다" 출력해보기
    st.info(f'선택한 나이는 {age}세입니다.')


    #익스펜더 : 선택하면 보이고 안 선택하면 감추기
    with st.expander('show'):
        st.text('this is a simple sentence for testing')
        st.dataframe(df)


#취업 Tip -> 면접관이 지원자의 코드를 열람할 때 중점으로 보는 사항>>> 1.변수 이름이 직관적인지?  2.예외처리에 꼼꼼한지?
#면접관은 그 코드 직접 다운받아보지 않는다





if __name__ == '__main__':
    main()



