def add_score(subject_score, subject, score):
  subject_score[subject] = score
  return subject_score

def calc_average_score(subject_score):
  if not subject_score:
    return "0.00"
  
  total_score = sum(subject_score.values())

  num_subjects = len(subject_score)
  average = total_score / num_subjects

  return f"{average:.2f}"

num_subjects = int(input("Input :"))

for i in range(num_subjects):
  subject_input = input("Name subject : ").strip()

  score_input = int(input("Score : "))
  my_scores = add_score(my_scores,subject_input,score_input)
  print(f"Success score : {my_scores}")

print(f"aveerage score : {calc_average_score(my_scores)}")