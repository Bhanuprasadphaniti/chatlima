import logging
from data_loader import load_data
from chatbot import get_answer

logging.basicConfig(
    filename="chatlima.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

df = load_data()
logging.info("ChatLima started")

while True:
    question = input("Ask me something (or type 'bye' to stop): ")

    if question.strip() == "":
        print("Please ask something! You typed nothing.")
        continue

    if question.lower() == "bye":
        print("Goodbye!")
        logging.info("ChatLima stopped by user")
        break

    answer = get_answer(question, df)
    logging.info(f"Q: {question} | A: {answer}")
    print(answer)