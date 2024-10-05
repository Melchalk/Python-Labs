def say_score(score):
    phrase = ""
    if score == 5:
        phrase = "Great"
    elif score == 4:
        phrase = "Good"
    else:
        phrase = "Not good."
    print(phrase)

def get_average_value(nums):
    average_value = 0
    for indexNum in range(len(nums)):
        average_value += nums[indexNum]
    average_value /= len(nums)
    return average_value
