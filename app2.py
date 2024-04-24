#streamlit은 데이터 분석용 프레임워크이다
#기타 웹 개발 언어(htrml, css 등)와 같이 구체적이고 미적인 표현은 애초에 이 라이브러리의 목적과 부합하지 않음


#기본 프레임
import streamlit as st

def main():
    #텍스트 표시 방법
    #title : 제목(큰 사이즈)
    st.title('Web Dashboard')
    
    #text : 내용(일반 가독 사이즈)
    st.text('Let\'s study about \"astreamlit\" programming framework')

    name = 'Fletcher Seth'
    st.text(f"My name is {name}. I'm your guidence for journy to wonderful streamlit world")

    #header : title보다 조금 작은 제목
    #subheader : header의 부제목
    st.header('This section is \'header\' \: smallest than title')
    st.subheader('Learning Basic-Grammar for ')
    
    #이 함수들은 글자 배경에 특정 color가 적용되어 표시됨 : 알림용이기 때문(인지성↑)
    st.success('작업이 성공 했을 때 사용')   #green
    st.warning('경고 문구를 보여주고 싶을 때 사용')   #yellow
    st.info('정보를 보여주고 싶을 때 사용')   #blue
    st.error('문제가 발생했다는 것을 알릴 때 사용')   #red


    #그럼 print()는 언제 사용?
    #print()는 debugging용이다!  -->  화면에 특정 문자열을 표시하기 위함이 절대 아님



    print(f'for example : {name}')  #print는 웹 페이지에 표시되지 않는다 -> 터미널에 찍히기 때문



if __name__ == '__main__':
    main()





#참고 : 화면(웹 페이지)에 표시하는건 모두 st.~가 담당한다





























