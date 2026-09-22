import streamlit as st
from data_loader import load_data
from chatbot import get_answer

st.title("ChatLima 🤖")
st.write("Ask about a student's branch, marks, or attendance.")

df = load_data()

if "history" not in st.session_state:
    st.session_state.history = []

question = st.text_input("Ask me something:")

if question:
    answer = get_answer(question, df)
    st.session_state.history.append((question, answer))

for q, a in reversed(st.session_state.history):
    st.write(f"**You:** {q}")
    st.write(f"**ChatLima:** {a}")