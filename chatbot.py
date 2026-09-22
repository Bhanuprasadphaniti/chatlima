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
        highest_marks_words = ["highest marks", "top marks", "best marks"]
        lowest_marks_words = ["lowest marks", "least marks", "worst marks"]
        highest_att_words = ["highest attendance", "best attendance"]
        lowest_att_words = ["lowest attendance", "least attendance", "worst attendance"]

        # check specific "highest/lowest" phrases BEFORE generic "marks"/"branch" checks
        if any(phrase in q for phrase in highest_marks_words):
            top = df.loc[df["marks"].idxmax()]
            return f"{top['name']} scored the highest marks: {int(top['marks'])}."

        if any(phrase in q for phrase in lowest_marks_words):
            bottom = df.loc[df["marks"].idxmin()]
            return f"{bottom['name']} scored the lowest marks: {int(bottom['marks'])}."

        if any(phrase in q for phrase in highest_att_words):
            top = df.loc[df["attendance"].idxmax()]
            return f"{top['name']} has the highest attendance: {int(top['attendance'])}%."

        if any(phrase in q for phrase in lowest_att_words):
            bottom = df.loc[df["attendance"].idxmin()]
            return f"{bottom['name']} has the lowest attendance: {int(bottom['attendance'])}%."

        # branch search: "who is in ECE" / "students in CSE"
        for branch_name in df["branch"].unique():
            if branch_name.lower() in q:
                students_in_branch = df[df["branch"].str.lower() == branch_name.lower()]
                names = ", ".join(students_in_branch["name"].tolist())
                return f"{branch_name} students: {names}"

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