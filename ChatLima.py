import pandas as pd

df = pd.read_csv("students.csv")
print(df)

while True:
    question = input("Ask me something (or type 'bye' to stop): ")

    if question.strip() == "":
        print("Please ask something! You typed nothing.")
        continue

    if question.lower() == "bye":
        print("Goodbye!")
        break

    q = question.lower()
    found = False

    for index, row in df.iterrows():
        name = row["name"].lower()
        if name in q:
            found = True
            if "who" in q:
                print(f"{row['name']} is a {row['branch']} branch student.")
            elif "marks" in q:
                print(f"{row['name']} scored {row['marks']} marks.")
            else:
                print(f"{row['name']} is in {row['branch']} branch with {row['marks']} marks.")

    if not found:
        print("Sorry, I couldn't find anyone with that name.")