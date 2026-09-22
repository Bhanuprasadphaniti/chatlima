def get_answer(question, df):
    q = question.lower()
    found = False
    response = ""

    for index, row in df.iterrows():
        name = row["name"].lower()
        if name in q:
            found = True
            if "who" in q:
                response = f"{row['name']} is a {row['branch']} branch student."
            elif "marks" in q:
                response = f"{row['name']} scored {row['marks']} marks."
            elif "attendance" in q:
                response = f"{row['name']} has {row['attendance']}% attendance."
            else:
                response = f"{row['name']} is in {row['branch']} branch, {row['marks']} marks, {row['attendance']}% attendance."

    if not found:
        response = "Sorry, I couldn't find anyone with that name."

    return response