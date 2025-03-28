import streamlit as st
import random

st.set_page_config(page_title="CAN I BE YOUR BOYFRIEND or WILL YOU BE MY GIRLFRIEND ?", layout="centered")

st.markdown("""
<style>
.big-font {
    font-size:24px !important;
    font-weight: bold;
    color: white;
}
.subtext {
    font-size:16px;
    color: white;
}
.stButton>button {
    color: #E93030;
    background-color: white;
    border: none;
    padding: 10px 24px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">CAN I BE YOUR BOYFRIEND or<br>WILL YOU BE MY GIRLFRIEND ?</p>', unsafe_allow_html=True)
st.markdown('<p class="subtext">obv you wanna be my girlfriend shutup</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Yes"):
        st.success("Hurrayyyy!!")
        st.balloons()

with col3:
    if 'no_button_pos' not in st.session_state:
        st.session_state.no_button_pos = (0, 0)

    def move_no_button():
        x, y = st.session_state.no_button_pos
        new_x = (x + 50) % 300
        new_y = (y + 50) % 200
        st.session_state.no_button_pos = (new_x, new_y)

    no_button = st.empty()
    no_clicked = no_button.button("No", key=f"no_{random.randint(0, 1000)}", on_click=move_no_button)

st.markdown(f"""
<style>
    [data-testid="stHorizontalBlock"] > div:nth-of-type(3) {{
        transform: translate({st.session_state.no_button_pos[0]}px, {st.session_state.no_button_pos[1]}px);
        transition: transform 0.3s ease;
    }}
</style>
""", unsafe_allow_html=True)

