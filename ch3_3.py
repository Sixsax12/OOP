def add_score(subject_score, subject, score):
    if subject == "":
        return subject_score

    if score < 0:
        return subject_score

    subject_score[subject] = score
    return subject_score


def calc_average_score(subject_score):
    if not subject_score:
        return "0.00"
    numeric_scores = map(float, subject_score.values())
    total_score = sum(numeric_scores)
    num_subjects = len(subject_score)
    return f"{(total_score / num_subjects):.2f}"


try:
    full = input("Input : ")
    if full.count(" | ") != 2:
        raise Exception

    part = full.split(" | ")
    if len(part) != 3:
        raise Exception

    raw_dict = part[0].strip()
    raw_key = part[1].strip()
    raw_val = part[2].strip()

    try:
        subject_score = eval(raw_dict)
        if not isinstance(subject_score, dict):
            raise Exception
    except:
        raise Exception

    if not ((raw_key.startswith("'") and raw_key.endswith("'")) or
            (raw_key.startswith('"') and raw_key.endswith('"'))):
        raise Exception

    key_no_quote = raw_key.strip()[1:-1]

    subject_in = key_no_quote.strip()

    val_clean = raw_val.replace("'", "").replace('"', "").strip()

    try:
        score_float = float(val_clean)
    except:
        raise Exception

    score_in = int(score_float) if score_float == int(score_float) else score_float

    add_all = add_score(subject_score, subject_in, score_in)

    avr_score = calc_average_score(add_all)
    print(f"{add_all}, Average score: {avr_score}")

except:
    print("Invalid")
