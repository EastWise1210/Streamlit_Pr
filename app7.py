#파일 업로드하는 방법


import streamlit as st

#현재 시간을 가져와서, 유저의 업로드 이미지 파일명을 고유 파일명으로 변경하기 위한 준비
from datetime import datetime

import pandas as pd

#디렉토리 정보와 파일을 파라미터로 전달하면, 해당 디렉토리에 파일을 저장하는 함수 정의
def save_upload_file(directory, file):
    #1. 디렉토리 경로 확인하여 없으면 디렉토리 생성
    import os
    if not os.path.exists(directory) :
        os.makedirs(directory)
    #2. 디렉토리가 존재하면 파일을 저장한다
    with open(os.path.join(directory, file.name), mode='wb') as f:
        f.write(file.getbuffer())
    #3. 저장이 완료되면 사용자에게 알려준다
    return st.success(f'It is success to save {file.name} to {directory}.')


def main():
    st.title('Uploading File Project')

    #사이드바 만들기
    side_sel_list = ['Uploading Image File', 'Uploading CSV File', 'More About']
    side_menu1 = st.sidebar.selectbox(label='MENU',
                                      options=side_sel_list)


    #사이드바의 MENU 선택사항에 따라 해당 내용 화면에 표시
    if side_menu1 == side_sel_list[0]:
        st.subheader('Uploading Image File')
        file1 = st.file_uploader(label='Choose your images', type=['JPG', 'JPEG', 'PNG', 'WebP', 'SVG', 'BMP', 'GIF'])
        
        #유저가 올린 파일이 있을 때 서버에 저장하기
        if file1 is not None:
            #file.name --> file의 이름 조회
            #file.size --> file의 크기 조회
            #file.type --> file의 데이터 타입 조회

            #파일을 서버에 저장하기 위해서는 먼저 파일 이름을 고유하게 바꿔줘야 한다
            #보편적인 실무 방법 -> 현재시간과 유저의 아이디를 조합해서 저장
            current_time = datetime.now()
            new_file_name = current_time.isoformat().replace(':', '_') + '.jpg'
            file1.name = new_file_name
            save_upload_file(directory='C:/Users/Fletcher/Documents/GitHub/Streamlit_Pr/user_image_storage', file=file1)
            
            #파일 업로드시 미리보기 제공해주기
            st.text('Preview Image')
            st.image(file1)


    elif side_menu1 == side_sel_list[1]:
        st.subheader('Uploading CSV File')
        file2 = st.file_uploader(label='Choose your csv file', type=['csv'])
        
        #유저가 올린 파일이 있을 때 서버에 저장하기
        if file2 is not None:
            current_time = datetime.now()
            new_file2_name = current_time.isoformat().replace(':', '_') + '.csv'
            file2.name = new_file2_name
            save_upload_file(directory='C:/Users/Fletcher/Documents/GitHub/Streamlit_Pr/user_csv_storage', file=file2)

            #파일 업로드시 미리보기 제공해주기
            st.text('Preview DataFrame')
            st.dataframe(pd.read_csv(file2))


    else :
        st.subheader('This is Uploading Project')
    


if __name__ == '__main__':
    main()




#commit이란, 본인이 작성(수정)한 코드가 온전히 작동함을 확인한 후에 하는 것
#소스코드 확인하지 않고 무조건 commit 했다가 협업 과정에서 차질이 생길 위험성↑




