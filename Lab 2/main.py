from functions import say_score
from functions import get_average_value

print("Enter the scores")
scores = [int(i) for i in input().split()]

for i in range(len(scores)):
    say_score(scores[i])

print("Average score: ", get_average_value(scores))