#사용자에게 값(숫자, 문자, 시간, 색 등)을 입력받기

import streamlit as st

def main():
    #1. 이름 입력받기
    name = st.text_input('input your text')  #입력 받은 값의 타입은 문자열(str)
    if name == '':
        pass
    else :
        st.text(f'alright! your name is "{name}". it\'s glad to meet you!')


    #2. 입력 글자수 제한 : max_chars 속성 이용
    address = st.text_input(label='input your address', max_chars=10)
    st.text(address)


    #3. 여러 행을 입력 가능하도록 설정 : height 값은 한 번에 볼 수 있는 행 크기
    message = st.text_area(label='input your message', height=5)
    st.text(message)


    #4. 비밀번호 입력 받기(글자수 제한 12) : type='password' 속성 이용하면 입력 문자 가리기 / 안 가리기 설정 가능
    password = st.text_input(label='input your password', type='password', max_chars=12)
    st.text(password)


    #5. 숫자 입력받기
      #(1)정수 입력
    st.number_input(label='input integer numbers', min_value=-40, max_value=140)   #min_value, max_value 별도 지정 가능
    
      #(2)실수 입력
    st.number_input(label='input float numbers', min_value=-200.0, max_value=400.0, step=0.5)


    #6. 날짜 입력받기
    my_date = st.date_input(label='Choose Date')
    st.text(my_date)  #ISO 날짜 포맷으로 출력된다
    st.text(my_date.weekday())
    st.text(my_date.strftime('%A'))   #수정하고 싶으면 ISO 날짜 포맷에 부합한 코드 입력


    #7. 시간 입력받기
    my_time = st.time_input(label='input time')
    st.text(my_time.strftime('%H-%M-%S'))


    #8. 색(color) 입력받기
    my_color = st.color_picker(label='choose color')
    st.write(my_color)
    st.text(my_color)


if __name__ == '__main__':
    main()





#AWS Free tier는 용량 문제로 tensorflow 가동X  --> 로컬에서 tensorflow 설치한 다음에
#티처블 머신, 코랩 등으로 로컬에서 돌리는걸 동영상으로 찍어서 github에 올려두고
#기업 지원시 해당 상황에 대해 전문용어를 사용하여 일목요연하게 잘 설명해서 링크 첨부하면 됨










































