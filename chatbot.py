import pandas as pd

def get_answer(question, df):
    q = question.lower()

    matched_row = None
    for index, row in df.iterrows():
        if row["name"].lower() in q:
            matched_row = row
            break

    if matched_row is None:
        student_words = ["students", "student", "names", "name"]
        branch_words = ["branches", "branch"]
        marks_words = ["marks"]

        if any(word in q for word in student_words):
            names = ", ".join(df["name"].tolist())
            return f"Students: {names}"

        if any(word in q for word in branch_words):
            branches = ", ".join(sorted(df["branch"].unique()))
            return f"Branches: {branches}"

        if any(word in q for word in marks_words):
            parts = []
            for index, row in df.iterrows():
                m = int(row["marks"]) if pd.notna(row["marks"]) else "not available"
                parts.append(f"{row['name']}: {m}")
            return "Marks — " + ", ".join(parts)

        return "Sorry, I couldn't find anyone with that name."

    row = matched_row
    marks = int(row["marks"]) if pd.notna(row["marks"]) else "not available"
    attendance = int(row["attendance"]) if pd.notna(row["attendance"]) else "not available"

    if "who" in q:
        return f"{row['name']} is a {row['branch']} branch student."
    elif "marks" in q:
        return f"{row['name']}'s marks: {marks}."
    elif "attendance" in q:
        return f"{row['name']}'s attendance: {attendance}."
    else:
        return f"{row['name']} is in {row['branch']} branch, marks: {marks}, attendance: {attendance}."