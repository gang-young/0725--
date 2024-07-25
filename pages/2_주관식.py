import streamlit as st

st.image('https://i.pinimg.com/originals/b5/9d/8f/b59d8f8cbb54368862109db8324dc6b8.jpg', use_column_width=True)

def short_answer_quiz():
    # 주관식 문제 정의
    questions = [
        {"question": "우리나라에서 가장 큰 화산섬으로 동서 73km, 남북 31km의 타원형으로 이루어진 이 섬의 이름은??", "answer": "제주도"},
        {"question": "동의보감을 집필한 사람은?", "answer": "허준"},
        {"question": "공공의 이익은 찬성하지만 자신이 속한 지역에 불이익이 되는 일은 반대하는 행동을 하는 이 현상은 무엇일까요?", "answer": "님비 현상"},
        {"question": "사람이 기계에 방대한 데이터를 입력하여 그 데이터를 기반으로 학습하고 일정한 패턴 값을 얻게끔 하는 것을 ○○러닝 이라고 한다.", "answer": "머신"}
    ]

    st.title('주관식 상식 퀴즈')

    responses = {}
    for idx, q in enumerate(questions):
        st.write(f"Question {idx + 1}: {q['question']}")
        response = st.text_area(f"Your Answer for Question {idx + 1}", key=idx)
        responses[idx] = response

    # 응답 수집 및 결과 계산
    def calculate_score(responses, questions):
        score = 0
        for idx, q in enumerate(questions):
            if responses[idx].strip().lower() == q['answer'].strip().lower():
                score += 1
        return score

    if st.button('Submit'):
        score = calculate_score(responses, questions)
        st.session_state.short_answer_score = score
        st.session_state.total_short_answer = len(questions)
        st.session_state.page = 'results'
        st.experimental_rerun()  # 세션 상태를 업데이트 후 새로 고침

if __name__ == "__main__":
    short_answer_quiz()
