#미디어(이미지, 비디오, 오디오 등)를 화면에 나타내는 방법

import streamlit as st

#이미지 처리를 위한 라이브러리
from PIL import Image


def main():
    #1. 저장된 이미지 파일을 화면에 표시하는 방법
    #내 컴퓨터 상의 이미지 파일 --> 디렉토리 저장 경로 지정
    img = Image.open(fp='./data/image_03.jpg')
    st.image(img)
    st.image(img, width=800)  #가로 길이만 조정하면 세로는 비율대로 자동 조정됨
    st.image(img, use_column_width=True)


    #2. 웹 상의 이미지 파일을 화면에 표시하는 방법
    #웹 상의 이미지  -->  URL 경로 지정
    url = 'https://image.dongascience.com/Photo/2019/09/1568191092998.jpg'
    st.image(url)


    #3. 비디오 파일을 화면에 표시하는 방법
    video_file = open(file='./data/video1.mp4', mode='rb')
    st.video(video_file)
    #유튜브 동영상을 가져올 때는 특정 플러그인이 있음


    #4. 오디오 파일을 화면에 표시하는 방법
    audio_file = open(file='./data/song.mp3', mode='rb')
    st.audio(audio_file.read(), format='audio/mp3')





if __name__ == '__main__':
    main()



























