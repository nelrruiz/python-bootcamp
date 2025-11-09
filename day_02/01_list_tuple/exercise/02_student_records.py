student_names = ("Juan", "Maria", "Joseph")
student_scores = (70, 90, 81)

# TODO: Print the student scores and names in the following format
""" 
    Student Records:
    Student: Juan scored 70 in the exam.
    Student: Maria scored 90 in the exam.
    Student: Joseph scored 81 in the exam.
"""
print(f"Student: name scored score in the exam")

######################################################### answer

for name, score in zip(student_names, student_scores):
    print(f"Student: {name} scored {score} in the exam.")

# challenge: get highest score


highest_scorer = None
highest_score = None

for name, score in zip(student_names, student_scores):
    if highest_score is None or score > highest_score:
        highest_scorer = name
        highest_score = score

print(f"{highest_scorer} had the highest score of {highest_score} in the exam.")
