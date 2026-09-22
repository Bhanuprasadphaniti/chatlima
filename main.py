from data_loader import load_data
from chatbot import get_answer

df = load_data()

while True:
    question = input("Ask me something (or type 'bye' to stop): ")

    if question.strip() == "":
        print("Please ask something! You typed nothing.")
        continue

    if question.lower() == "bye":
        print("Goodbye!")
        break

    answer = get_answer(question, df)
    print(answer)