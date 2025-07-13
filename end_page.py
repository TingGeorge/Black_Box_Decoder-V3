import streamlit as st

st.image("end_title_stars.png")
st.write("")
st.write("")

CORRECT_ANSWER_1 = "welcome to 118csie in nuk!"
CORRECT_ANSWER_2 = "startwithhelloworld"
CORRECT_ANSWER_3 = "madeintaiwan"

if st.session_state.level_1_correct:
    if not st.session_state.score_calculated_1:
        st.session_state.score += 1
        st.session_state.score_calculated_1 = True
elif st.session_state.existing_data.loc[st.session_state.index, "Level 1"] == CORRECT_ANSWER_1:
    if not st.session_state.score_calculated_1:
        st.session_state.score += 1
        st.session_state.score_calculated_1 = True

    st.session_state.text_1 = CORRECT_ANSWER_1
    st.session_state.level_1_correct = True
    st.session_state.fail_answer_1 = False

if st.session_state.level_2_correct:
    if not st.session_state.score_calculated_2:
        st.session_state.score += 1
        st.session_state.score_calculated_2 = True
elif st.session_state.existing_data.loc[st.session_state.index, "Level 2"] == CORRECT_ANSWER_2:
    if not st.session_state.score_calculated_2:
        st.session_state.score += 1
        st.session_state.score_calculated_2 = True

    st.session_state.text_2 = CORRECT_ANSWER_2
    st.session_state.level_2_correct = True
    st.session_state.fail_answer_2 = False

if st.session_state.level_3_correct:
    if not st.session_state.score_calculated_3:
        st.session_state.score += 1
        st.session_state.score_calculated_3 = True
elif st.session_state.existing_data.loc[st.session_state.index, "Level 3"] == CORRECT_ANSWER_3:
    if not st.session_state.score_calculated_3:
        st.session_state.score += 1
        st.session_state.score_calculated_3 = True

    st.session_state.text_3 = CORRECT_ANSWER_3
    st.session_state.level_3_correct = True
    st.session_state.fail_answer_3 = False

images = ["score0.png", "score1.png", "score2.png", "score3.png"]
st.image(images[st.session_state.score])

if st.session_state.score == 3:
    st.balloons()