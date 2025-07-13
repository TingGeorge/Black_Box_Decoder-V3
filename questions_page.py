import streamlit as st

st.image("smaller_logo.png")
tab_1, tab_2, tab_3 = st.tabs(["*Level 1*", "*Level 2*", "*Level3*"])

# level 1
with tab_1:
    st.write("""
        <div style='padding-left: 4em;'>目標： 觀察模式，推理加密邏輯，還原一組密碼，並將密碼輸入到輸入框內。</div>
        <div style='padding-left: 7.2em;'>(字母皆為小寫且空格和標點符號在加密前與加密後相同)</div>
    """, unsafe_allow_html=True)
    st.write("")

    left_space, main_content, right_space = st.columns([1, 3, 1])
    with main_content:
        with st.container(border=True):
            original, gap, cryption = st.columns([5, 1, 5])

            with original:
                st.markdown("<p style='text-align: center; text-decoration: underline;'>輸入字串</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>apple</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>hello1</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>openai8</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>cat123</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>hi</p>", unsafe_allow_html=True)

            with cryption:
                st.markdown("<p style='text-align: center; text-decoration: underline;'>加密結果</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>dssoh</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>khoor2</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>rshqdl9</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>fdw234</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>kl</p>", unsafe_allow_html=True)

    CORRECT_ANSWER_1 = "welcome to 118csie in nuk!"

    def on_submit_1():
        st.session_state.text_1 = st.session_state.answer_1
        if st.session_state.answer_1 == CORRECT_ANSWER_1:
            st.session_state.level_1_correct = True
            st.session_state.fail_answer_1 = False
            st.session_state.existing_data.loc[st.session_state.index, "Level 1"] = CORRECT_ANSWER_1
            st.session_state.conn.update(worksheet="Sheet1", data=st.session_state.existing_data)
            st.cache_data.clear()
        else:
            st.session_state.fail_answer_1 = True

    st.write("")

    with st.form("level_1", border=False):
        null0, left_element, null1, right_element, null2 = st.columns([1, 7, 0.5, 2, 1.5], vertical_alignment="bottom")

        with left_element:
            st.text_input(
                label="題目： zhofrph wr 229fvlh lq qxn!",
                placeholder="請在此輸入解碼後的答案...",
                key="answer_1",
                value=st.session_state.text_1,
                disabled=st.session_state.level_1_correct
            )

        with right_element:
            st.form_submit_button(label="送出", on_click=on_submit_1, disabled=st.session_state.level_1_correct)

    if st.session_state.level_1_correct:
        st.success("Level 1 已通過！", icon="✅")
    elif st.session_state.existing_data.loc[st.session_state.index, "Level 1"] == CORRECT_ANSWER_1:
        st.success("Level 1 已通過！", icon="✅")
    elif st.session_state.fail_answer_1:
        st.error("答案不正確，請再試一次！", icon="🚨")

# level 2
with tab_2:
    st.write("""
        <div style='padding-left: 4em;'>目標： 觀察模式，推理加密邏輯，還原一組密碼，並將密碼輸入到輸入框內。</div>
        <div style='padding-left: 7.2em;'>(字母皆為小寫)</div>
    """, unsafe_allow_html=True)
    st.write("")

    left_space, main_content, right_space = st.columns([1, 3, 1])
    with main_content:
        with st.container(border=True):
            original, gap, cryption = st.columns([5, 1, 5])

            with original:
                st.markdown("<p style='text-align: center; text-decoration: underline;'>輸入字串</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>cfa22k5j2ve</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>hdfknfj94h</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>bfui4fddx</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>oejhfo4hfj</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>lslslslslsl</p>", unsafe_allow_html=True)

            with cryption:
                st.markdown("<p style='text-align: center; text-decoration: underline;'>加密結果</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>ev2j5k22afc</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>h49jfnkfdh</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>xddf4iufb</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>jfh4ofhjeo</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>lslslslslsl</p>", unsafe_allow_html=True)

    CORRECT_ANSWER_2 = "startwithhelloworld"

    def on_submit_2():
        st.session_state.text_2 = st.session_state.answer_2
        if st.session_state.answer_2 == CORRECT_ANSWER_2:
            st.session_state.level_2_correct = True
            st.session_state.fail_answer_2 = False
            st.session_state.existing_data.loc[st.session_state.index, "Level 2"] = CORRECT_ANSWER_2
            st.session_state.conn.update(worksheet="Sheet1", data=st.session_state.existing_data)
            st.cache_data.clear()
        else:
            st.session_state.fail_answer_2 = True

    st.write("")

    with st.form("level_2", border=False):
        null0, left_element, null1, right_element, null2 = st.columns([1, 7, 0.5, 2, 1.5], vertical_alignment="bottom")

        with left_element:
            st.text_input(
                label="題目： dlrowollehhtiwtrats",
                placeholder="請在此輸入解碼後的答案...",
                key="answer_2",
                value=st.session_state.text_2,
                disabled=st.session_state.level_2_correct
            )

        with right_element:
            st.form_submit_button(label="送出", on_click=on_submit_2, disabled=st.session_state.level_2_correct)

    if st.session_state.level_2_correct:
        st.success("Level 2 已通過！", icon="✅")
    elif st.session_state.existing_data.loc[st.session_state.index, "Level 2"] == CORRECT_ANSWER_2:
        st.success("Level 2 已通過！", icon="✅")
    elif st.session_state.fail_answer_2:
        st.error("答案不正確，請再試一次！", icon="🚨")

# level 3
with tab_3:
    st.write("""
        <div style='padding-left: 4em;'>目標： 結合前２關的模式，推理加密邏輯，還原一組密碼，並將密碼輸入到輸入框內。</div>
        <div style='padding-left: 7.2em;'>(字母皆為小寫)</div>
    """, unsafe_allow_html=True)
    st.write("")

    left_space, main_content, right_space = st.columns([1, 3, 1])
    with main_content:
        with st.container(border=True):
            original, gap, cryption = st.columns([5, 1, 5])

            with original:
                st.markdown("<p style='text-align: center; text-decoration: underline;'>輸入字串</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>a1dven14ture</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>pr1ogr1amm8er</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>algorithm</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>alp2h0a1b5et</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>6june20</p>", unsafe_allow_html=True)

            with cryption:
                st.markdown("<p style='text-align: center; text-decoration: underline;'>加密結果</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>gtwv63pgxf3c</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>tg0ooc3tiq3tr</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>ojvktqinc</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>vg7d3c2j4rnc</p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>24gpwl8</p>", unsafe_allow_html=True)

    CORRECT_ANSWER_3 = "madeintaiwan"

    def on_submit_3():
        st.session_state.text_3 = st.session_state.answer_3
        if st.session_state.answer_3 == CORRECT_ANSWER_3:
            st.session_state.level_3_correct = True
            st.session_state.fail_answer_3 = False
            st.session_state.existing_data.loc[st.session_state.index, "Level 3"] = CORRECT_ANSWER_3
            st.session_state.conn.update(worksheet="Sheet1", data=st.session_state.existing_data)
            st.cache_data.clear()
        else:
            st.session_state.fail_answer_3 = True

    st.write("")

    with st.form("level_3", border=False):
        null0, left_element, null1, right_element, null2 = st.columns([1, 7, 0.5, 2, 1.5], vertical_alignment="bottom")

        with left_element:
            st.text_input(
                label="題目： pcykcvpkgfco",
                placeholder="請在此輸入解碼後的答案...",
                key="answer_3",
                value=st.session_state.text_3,
                disabled=st.session_state.level_3_correct
            )

        with right_element:
            st.form_submit_button(label="送出", on_click=on_submit_3, disabled=st.session_state.level_3_correct)

    if st.session_state.level_3_correct:
        st.success("Level 3 已通過！", icon="✅")
    elif st.session_state.existing_data.loc[st.session_state.index, "Level 3"] == CORRECT_ANSWER_3:
        st.success("Level 3 已通過！", icon="✅")
    elif st.session_state.fail_answer_3:
        st.error("答案不正確，請再試一次！", icon="🚨")


# welcome to 118csie in nuk!
# startwithhelloworld
# madeintaiwan