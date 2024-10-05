from functions import say_score
from functions import get_average_value

scores = [2, 5, 4, 3, 5, 5]

for i in range(len(scores)):
    say_score(scores[i])

print("Average score: ", get_average_value(scores))