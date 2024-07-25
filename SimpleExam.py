import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

# Firebase Admin SDK 초기화
cred = credentials.Certificate('secret.json')  # 실제 경로로 변경
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# Firestore 클라이언트 초기화
db = firestore.client()

def register_user(username, email):
    try:
        # Firestore의 'users' 컬렉션에 사용자 정보 저장
        doc_ref = db.collection('users').document(username)
        doc_ref.set({
            'username': username,
            'email': email,
            'registered_at': datetime.now().isoformat()  # 날짜 및 시간 저장
        })
        st.success("회원가입이 완료되었습니다!")
    except Exception as e:
        st.error(f"회원가입 중 오류가 발생했습니다: {e}")

def home():
    st.title('간단한 퀴즈를 풀어보세요!')
    st.write("초등학생도 풀 수 있는 쉬운 퀴즈입니다!.")

    st.image('https://img.freepik.com/premium-vector/quiz-logo-with-speech-bubble-icon_149152-811.jpg', use_column_width=True)
    
    st.subheader("회원가입")

    # 회원가입 폼
    username = st.text_input("사용자 이름")
    email = st.text_input("이메일 주소")

    if st.button("회원가입"):
        if username and email:
            register_user(username, email)
        else:
            st.warning("모든 필드를 입력해 주세요.")
    
    st.subheader("퀴즈 시작")
    text = st.text_input("이름을 입력해주세요!")
    if st.button("시험 시작!"):
        st.session_state.text = text
        st.session_state.page = "pages/1_객관식.py"
        st.write("시험을 시작합니다!")

if __name__ == "__main__":
    home()
