def start_program():
    print("Hello. Block 'Student' was started.\nWhat is your name?" , end=' ')
    return input()

def acquaint(name):
    print(f"{name}, lets tell me your age:", end=' ')
    age = int(input())
    print("What is your status?", end=' ')
    status = input()
    return age, status

def get_organization_information(status="Student", organization="Mospolytech"):
    print(f"Your status {status} in {organization}")

def get_scores(name:str, status:str):
    print(f"{name} ({status}) say three your scores")
    scores = [int(i) for i in input().split()]
    return scores[0], scores[1], scores[2]

def get_scores_count(*scores):
    scores_count = dict()
    for score in scores:
        if score not in scores_count:
            scores_count[score] = 0
        scores_count[score] += 1
    return scores_count

def say_scores_count(scores_count):
    def say_score(score_type):
        if score_type == 5:
            phrase = "Great"
        elif score_type == 4:
            phrase = "Good"
        else:
            phrase = "Not good"
        return phrase

    for score in scores_count.keys():
        print(f"Count {say_score(score)} = {scores_count.get(score)}")
