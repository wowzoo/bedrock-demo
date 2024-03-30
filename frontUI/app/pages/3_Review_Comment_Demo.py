import streamlit as st
import requests
import os


ALB_URL = os.environ.get('ALB_URL')
API_URL = f'http://{ALB_URL}/comment'


st.set_page_config(page_title='Gen AI - Comment Generation')
st.title('상품 리뷰 답변 생성')
st.write('구매자 만족도를 POSITIVE, NEGATIVE, MIXED 로 구분하고, 이에 대응하는 답변을 생성해 줍니다.')
st.markdown('\n')
st.markdown('#### 예제는 I LOVE CANDY Crop Hoodie zip-up -[BEIGE] 상품의 리뷰입니다.')
st.write('https://www.musinsa.com/app/goods/3523892')

st.code("""제가 브라렛을 착용하고 찍었더니 뭔가 핏이 안예쁘게 나왔는데 잘잡아주는 속옷 착용하고 입으면 핏 이뻐요 !!
생각보다 더 크롭이에요
안에 뭐 받쳐입는거보단 단독으로 입을때 허리가 딱 이쁘게 보이는거같아요""")
st.code("""베이지 색상이 좀 독특한 베이진데 그래서 더 맘에 들어요 라벨 붙어 있는 원래 가격에는 안 살 거 같구요
쿠폰쓰고 적립금 쓰고 이정도 가격에도 살짝 뭔가 부족한 느낌이 있네요 재질이나 프린팅이야 그렇다치고 지퍼를 좀 잘 만들 수 없을까요ㅜ 급할때는 입지도 못하겠네요""")
st.code("""크롭후드원해서 산거랑 짧고 뭐 이런건 문제가 안되는데 지퍼가 너무 빡치네요 잠그고 올리기도 어렵고 다시 빼내기도어려워요 불량일까 반품할까도 했지만 5번중에 1번 되길래 걍 빡치면서 입게요""")


# Review
review_input = st.text_area('Review', '')

with st.form('comment_generation_form', clear_on_submit=True):
    submitted = st.form_submit_button('Submit')
    if submitted:
        with st.spinner('Loading...'):
            response = requests.post(API_URL, json={'body': review_input}) 

            data = response.json()
            st.info(f'구매자 만족도: {data["Sentiment"]}')
            st.info(f'AI가 생성한 답변: {data["Generated"]}')


