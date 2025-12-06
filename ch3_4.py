def add_score(subject_score, student, subject, score):
    if student not in subject_score:
        subject_score[student] = {}
    subject_score[student][subject] = score
    return subject_score


def calc_average_score(subject_score):
    avg_dict = {}
    for student, subjects in subject_score.items():
        if len(subjects) == 0:
            avg = 0
        else:
            avg = sum(subjects.values()) / len(subjects)
        avg_dict[student] = f"{avg:.2f}"
    return avg_dict

try:
    raw = input("Input : ").split(" | ")

    subject_score = eval(raw[0])

    rest = raw[1:]

    if len(rest) % 3 != 0:
        exit()

    for i in range(0, len(rest), 3):

        student_raw = rest[i].strip()
        subject_raw = rest[i+1].strip()
        score_raw = rest[i+2].strip()

        if not student_raw.isdigit():
            exit()
        student = student_raw 

        if not (subject_raw.startswith("'") and subject_raw.endswith("'")):
            exit()
        subject = subject_raw[1:-1].strip()

        if subject == "":
            exit()

        if not score_raw.isdigit():
            exit()

        score = int(score_raw)
        if score < 0:
            exit()
        subject_score = add_score(subject_score, student, subject, score)

    avg = calc_average_score(subject_score)

    print(subject_score, end=", ")
    print("Average score:", avg)
except:
    print("Invalid")
