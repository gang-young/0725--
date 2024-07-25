import streamlit as st

def display_results(multiple_choice_score, short_answer_score, total_multiple_choice, total_short_answer):
    # 결과만 표시
    st.write(f"**객관식 퀴즈 결과:**")
    st.write(f"정답 개수: {multiple_choice_score} / {total_multiple_choice}")

    st.write(f"**주관식 퀴즈 결과:**")
    st.write(f"정답 개수: {short_answer_score} / {total_short_answer}")

def results_page():
    # 세션 상태에서 데이터 가져오기
    multiple_choice_score = st.session_state.get('multiple_choice_score', 0)
    short_answer_score = st.session_state.get('short_answer_score', 0)
    total_multiple_choice = st.session_state.get('total_multiple_choice', 0)
    total_short_answer = st.session_state.get('total_short_answer', 0)

    # 페이지 제목 및 이미지
    st.title('Quiz Results')
    st.image('https://img.freepik.com/premium-vector/quiz-logo-with-speech-bubble-icon_149152-811.jpg', 
              use_column_width=True)


    # 결과 확인 버튼
    if st.button('결과 확인'):
        display_results(multiple_choice_score, short_answer_score, total_multiple_choice, total_short_answer)

if __name__ == "__main__":
    results_page()


st.write(f"{st.session_state.text}님 수고하셨습니다!")
