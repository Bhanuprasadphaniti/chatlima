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

        if any(phrase in q for phrase in highest_marks_words):
            top = df.loc[df["marks"].idxmax()]
            return pd.DataFrame([{"Name": top["name"], "Branch": top["branch"], "Marks": int(top["marks"])}])

        if any(phrase in q for phrase in lowest_marks_words):
            bottom = df.loc[df["marks"].idxmin()]
            return pd.DataFrame([{"Name": bottom["name"], "Branch": bottom["branch"], "Marks": int(bottom["marks"])}])

        if any(phrase in q for phrase in highest_att_words):
            top = df.loc[df["attendance"].idxmax()]
            return pd.DataFrame([{"Name": top["name"], "Branch": top["branch"], "Attendance": int(top["attendance"])}])

        if any(phrase in q for phrase in lowest_att_words):
            bottom = df.loc[df["attendance"].idxmin()]
            return pd.DataFrame([{"Name": bottom["name"], "Branch": bottom["branch"], "Attendance": int(bottom["attendance"])}])

        for branch_name in df["branch"].unique():
            if branch_name.lower() in q:
                subset = df[df["branch"].str.lower() == branch_name.lower()]
                return subset[["roll_no", "name", "branch"]].rename(
                    columns={"roll_no": "Roll No", "name": "Name", "branch": "Branch"}
                )

        if any(word in q for word in student_words):
            return df[["roll_no", "name", "branch"]].rename(
                columns={"roll_no": "Roll No", "name": "Name", "branch": "Branch"}
            )

        if any(word in q for word in branch_words):
            branches = sorted(df["branch"].unique())
            return pd.DataFrame({"Branch": branches})

        if any(word in q for word in marks_words):
            table = df[["name", "marks"]].copy()
            table["marks"] = table["marks"].apply(lambda m: int(m) if pd.notna(m) else "N/A")
            return table.rename(columns={"name": "Name", "marks": "Marks"})

        return "Sorry, I couldn't find anyone with that name."

    row = matched_row
    marks = int(row["marks"]) if pd.notna(row["marks"]) else "N/A"
    attendance = int(row["attendance"]) if pd.notna(row["attendance"]) else "N/A"

    if "who" in q:
        return pd.DataFrame([{"Name": row["name"], "Branch": row["branch"]}])
    elif "marks" in q:
        return pd.DataFrame([{"Name": row["name"], "Marks": marks}])
    elif "attendance" in q:
        return pd.DataFrame([{"Name": row["name"], "Attendance": attendance}])
    else:
        return pd.DataFrame([{"Name": row["name"], "Branch": row["branch"], "Marks": marks, "Attendance": attendance}])