student_scores = [98, 75, 100, 86, 100, 3]

# TODO: Print the average score
average_score = None
print(average_score)

# TODO: Print the rankings, highest to lowest
print()


######################################### answer

average_score = sum(student_scores) / len(student_scores)
print("The average score is", average_score)
print(sorted(student_scores, reverse=True))

for score in sorted(student_scores, reverse=True):
    print(score)