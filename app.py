import streamlit as st
import pandas as pd
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
    st.write("")
    st.write("")
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
        st.markdown(
            "<div style='background-color:#FFFFFF; padding:10px; border-radius:8px; "
            "box-shadow: 0 1px 4px rgba(0,0,0,0.15); margin-bottom:8px;'>",
            unsafe_allow_html=True
        )
        if isinstance(a, pd.DataFrame):
            st.dataframe(a, hide_index=True, use_container_width=True)
        else:
            st.markdown(f"<span style='color:#000000;'>{a}</span>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div style='opacity:0.4; margin-bottom:8px;'>", unsafe_allow_html=True)
        if isinstance(a, pd.DataFrame):
            st.dataframe(a, hide_index=True, use_container_width=True)
        else:
            st.write(a)
        st.markdown("</div>", unsafe_allow_html=True)