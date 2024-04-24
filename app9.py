#차트 그리는 방법


#기본 라이브러리 import
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


def main():
    st.title('Drawing chart')
    df = pd.read_csv('./data/iris.csv')
    st.dataframe(df)

    #ex)sepal_length와 sepal_width의 관계를 차트로 나타내기
    #1. pyplot으로 scatter 나타내기
    st.subheader('Pyplot을 이용한 Scatter 나타내기')
    fig1 = plt.figure()
    plt.scatter(data=df, x='sepal_length', y='sepal_width')
    plt.title('Sepal Length VS Sepal Width')
    st.pyplot(fig1)

    #2. seaborn으로 scatter 나타내기
    st.subheader('Seaborn을 이용한 Scatter 나타내기')
    fig2 = plt.figure()
    sb.scatterplot(data=df, x='sepal_length', y='sepal_width')
    plt.title('Sepal Length VS Sepal Width')
    st.pyplot(fig2)

    #3. seaborn으로 regplot 나타내기
    st.subheader('Seaborn을 이용한 regplot 나타내기')
    fig3 = plt.figure()
    sb.regplot(data=df, x='sepal_length', y='sepal_width')
    plt.title('Sepal Length VS Sepal Width')
    st.pyplot(fig3)

    #sepal_length로 히스토그램 나타내기 : bins의 개수는 20개로
    st.subheader('히스토그램 나타내기')
    fig4 = plt.figure()
    plt.hist(data=df, x='sepal_length', bins=20, rwidth=0.9)
    plt.title('Expression of Histogram about Sepal Length')
    plt.xlabel('Sepal Length')
    plt.ylabel('Counts')
    st.pyplot(fig4)


    #예제 : 두 차트의 bins를 각각 10과 20으로 설정하고 나열하여 나타내라
    st.subheader('히스토그램 나타내기2')
    fig5 = plt.figure(figsize=(10,4))
    plt.subplot(1,2,1)
    plt.hist(data=df, x='sepal_length', bins=10, rwidth=0.9)
    plt.title('Expression of Length')
    plt.xlabel('Sepal Length')

    plt.subplot(1,2,2)
    plt.hist(data=df, x='sepal_length', bins=20, rwidth=0.9)
    plt.title('Expression Sepal of Length')
    plt.xlabel('Sepal Length')

    st.pyplot(fig5)



    #판다스의 데이터프레임의 차트 그려보기
    fig6 = plt.figure()
    df['species'].value_counts().plot(kind='barh')
    plt.title('Graph about Number of Species')
    st.pyplot(fig6)


    #sepal_length 컬럼을 히스토그램으로 나타내보기
    fig7 = plt.figure()
    df['sepal_length'].plot(kind='hist', rwidth=0.9)
    plt.title('Graph about Number of Sepal Length1')
    st.pyplot(fig7)


    fig8 = plt.figure()
    df['sepal_length'].hist()
    plt.title('Graph about Number of Sepal Length2')
    st.pyplot(fig8)



    #데이터프레임 iris.csv의 상관계수를 구하여 차트로 표현하기
    df_corr = df.corr(numeric_only=True)
    fig10 = plt.figure()
    sb.heatmap(data=df_corr, vmin=-1, vmax=1, annot=True, fmt='.1f')
    st.pyplot(fig10)





if __name__ == '__main__':
    main()


