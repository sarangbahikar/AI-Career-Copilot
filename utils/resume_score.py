def calculate_score(skills):

    if len(skills) >= 10:
        return 90

    elif len(skills) >= 5:
        return 70

    else:
        return 40