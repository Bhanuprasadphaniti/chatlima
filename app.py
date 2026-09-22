import streamlit as st
from data_loader import load_data
from chatbot import get_answer

st.title("ChatLima 🤖")
st.write("Ask about a student's branch, marks, or attendance.")

df = load_data()

if "history" not in st.session_state:
    st.session_state.history = []

col1, col2 = st.columns([4, 1])

with col1:
    question = st.text_input("Ask me something:")

with col2:
    button_label = "Clear" if st.session_state.history else "Enter"
    st.write("")  # matches the label height above the input box
    st.write("")  # small extra nudge to line up with the input box border
    if st.button(button_label, use_container_width=True):
        if st.session_state.history:
            st.session_state.history = []
            st.rerun()

if question:
    answer = get_answer(question, df)
    st.session_state.history.append((question, answer))

for i, (q, a) in enumerate(reversed(st.session_state.history)):
    is_latest = (i == 0)

    if is_latest:
        style = "opacity:1; background-color:#FFFFFF; color:#000000; padding:10px; border-radius:8px; margin-bottom:8px; box-shadow: 0 1px 4px rgba(0,0,0,0.15);"
    else:
        style = "opacity:0.4; background-color:transparent; padding:10px; margin-bottom:8px;"

    st.markdown(
        f"""
        <div style="{style}">
            {a}
        </div>
        """,
        unsafe_allow_html=True
    )