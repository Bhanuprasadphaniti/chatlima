import pandas as pd

def get_answer(question, df):
    q = question.lower()
    found = False
    response = ""

    for index, row in df.iterrows():
        name = row["name"].lower()
        if name in q:
            found = True

            marks = row["marks"] if pd.notna(row["marks"]) else "not available"
            attendance = row["attendance"] if pd.notna(row["attendance"]) else "not available"

            if "who" in q:
                response = f"{row['name']} is a {row['branch']} branch student."
            elif "marks" in q:
                response = f"{row['name']}'s marks: {marks}."
            elif "attendance" in q:
                response = f"{row['name']}'s attendance: {attendance}."
            else:
                response = f"{row['name']} is in {row['branch']} branch, marks: {marks}, attendance: {attendance}."

    if not found:
        response = "Sorry, I couldn't find anyone with that name."

    return response