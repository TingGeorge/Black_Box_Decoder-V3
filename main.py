import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.logo("sidebar_logo.png", icon_image="uc_logo.png")

# main.py
if "user" not in st.session_state:
    st.session_state.user = ""
if "score" not in st.session_state:
    st.session_state.score = 0
if "index" not in st.session_state:
    st.session_state.index = 0
if "conn" not in st.session_state:
    st.session_state.conn = None
if "existing_data" not in st.session_state:
    st.session_state.existing_data = None
if "username_input" not in st.session_state:
    st.session_state.username_input = ""

# questions_page.py
# level 1
if "answer_1" not in st.session_state:
    st.session_state.answer_1 = ""
if "level_1_correct" not in st.session_state:
    st.session_state.level_1_correct = False
if "fail_answer_1" not in st.session_state:
    st.session_state.fail_answer_1 = False
if "score_calculated_1" not in st.session_state:
    st.session_state.score_calculated_1 = False
if "text_1" not in st.session_state:
    st.session_state.text_1 = ""

#level 2
if "answer_2" not in st.session_state:
    st.session_state.answer_2 = ""
if "level_2_correct" not in st.session_state:
    st.session_state.level_2_correct = False
if "fail_answer_2" not in st.session_state:
    st.session_state.fail_answer_2 = False
if "score_calculated_2" not in st.session_state:
    st.session_state.score_calculated_2 = False
if "text_2" not in st.session_state:
    st.session_state.text_2 = ""

#level 3
if "answer_3" not in st.session_state:
    st.session_state.answer_3 = ""
if "level_3_correct" not in st.session_state:
    st.session_state.level_3_correct = False
if "fail_answer_3" not in st.session_state:
    st.session_state.fail_answer_3 = False
if "score_calculated_3" not in st.session_state:
    st.session_state.score_calculated_3 = False
if "text_3" not in st.session_state:
    st.session_state.text_3 = ""

# this name "gsheets" must match [connections.gsheets] in your secrets.toml
st.session_state.conn = st.connection("gsheets", type=GSheetsConnection)
st.session_state.existing_data = st.session_state.conn.read(worksheet="Sheet1")

# Replace empty strings with NaN
# 'inplace=True' means the replacement happens directly in the original DataFrame
st.session_state.existing_data["Name"].replace("", None, inplace=True)
# Now drop rows where Name is missing
st.session_state.existing_data.dropna(subset=["Name"], inplace=True)

def login():
    for i in range(10):
        st.write("")
    st.image("user_logo.png", use_container_width=True)

    def login_contents():
            st.session_state.user = st.session_state.username_input
            if st.session_state.user not in st.session_state.existing_data["Name"].values:
                new_data = pd.DataFrame(
                    [
                        {
                            "Name": st.session_state.user,
                            "Level 1": "",
                            "Level 2": "",
                            "Level 3": ""
                        }
                    ]
                )
                new_pd = pd.concat([st.session_state.existing_data, new_data], ignore_index=True)
                st.session_state.conn.update(worksheet="Sheet1", data=new_pd)
                st.session_state.existing_data = new_pd  # <-- update session state immediately
                st.session_state.index = new_pd.shape[0] - 1  # number of rows
            else:
                st.session_state.index = st.session_state.existing_data.index[st.session_state.existing_data["Name"] == st.session_state.user].tolist()[0]

            st.cache_data.clear()

    with st.form("login_form", border=False):
        null0, left_element, null1, right_element, null2 = st.columns([8, 8, 0.5, 2, 8], vertical_alignment="bottom")

        with left_element:
            st.text_input(label="", placeholder="請輸入組別：", key="username_input")

        with right_element:
            st.form_submit_button("", icon=":material/line_end_arrow_notch:", on_click=login_contents)

def logout():
    st.session_state.user = ""
    st.session_state.score = 0
    st.session_state.index = 0

    st.session_state.answer_1 = ""
    st.session_state.level_1_correct = False
    st.session_state.fail_answer_1 = False
    st.session_state.score_calculated_1 = False
    st.session_state.text_1 = ""

    st.session_state.answer_2 = ""
    st.session_state.level_2_correct = False
    st.session_state.fail_answer_2 = False
    st.session_state.score_calculated_2 = False
    st.session_state.text_2 = ""

    st.session_state.answer_3 = ""
    st.session_state.level_3_correct = False
    st.session_state.fail_answer_3 = False
    st.session_state.score_calculated_3 = False
    st.session_state.text_3 = ""

    st.rerun()

login_page = st.Page(login)
logout_page = st.Page(logout, title="登出", icon=":material/logout:")
first_page = st.Page("first_page.py", title="首頁", icon=":material/home:")
questions_page = st.Page("questions_page.py", title="題目", icon=":material/menu:")
end_page = st.Page("end_page.py", title="解題進度", icon=":material/flag:")

login_interface = [login_page]
logout_interface = [logout_page]
contents = [first_page, questions_page, end_page]

if len(st.session_state.user):
    pages = st.navigation({"遊戲": contents} | {"帳號": logout_interface})
else:
    pages = st.navigation(login_interface)

pages.run()

# st.session_state
