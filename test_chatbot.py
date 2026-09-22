import pandas as pd
from chatbot import get_answer

def sample_data():
    data = {
        "name": ["Ravi", "Sita"],
        "branch": ["CSE", "ECE"],
        "marks": [82, 91],
        "attendance": [91, 88]
    }
    return pd.DataFrame(data)

def test_who_question():
    df = sample_data()
    answer = get_answer("who is ravi", df)
    assert "CSE" in answer

def test_marks_question():
    df = sample_data()
    answer = get_answer("what are sita's marks", df)
    assert "91" in answer

def test_unknown_student():
    df = sample_data()
    answer = get_answer("who is john", df)
    assert "couldn't find" in answer