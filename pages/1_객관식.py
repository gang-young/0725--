import streamlit as st

st.image('https://i.pinimg.com/736x/7a/64/d1/7a64d16d82e1bc56a6607d4a7f13625b.jpg', use_column_width=True)

def multiple_choice_quiz():
    # 객관식 문제 정의
    questions = [
        {"question": "프랑스의 수도는?", "options": ["파리", "런던", "베를린", "마드리드"], "answer": "파리"},
        {"question": "2 + 2의 결과는?", "options": ["3", "4", "5", "6"], "answer": "4"}
    ]

    st.title('객관식 상식 퀴즈')

    responses = {}
    for idx, q in enumerate(questions):
        st.write(f"Question {idx + 1}: {q['question']}")
        response = st.radio(f"Select answer for Question {idx + 1}", q['options'], key=idx)
        responses[idx] = response

    # 응답 수집 및 결과 계산
    def calculate_score(responses, questions):
        score = 0
        for idx, q in enumerate(questions):
            if responses[idx] == q['answer']:
                score += 1
        return score

    if st.button('Submit'):
        score = calculate_score(responses, questions)
        st.session_state.multiple_choice_score = score
        st.session_state.total_multiple_choice = len(questions)
        st.session_state.page = 'short_answer'
        st.experimental_rerun()  # 세션 상태를 업데이트 후 새로 고침

if __name__ == "__main__":
    multiple_choice_quiz()
