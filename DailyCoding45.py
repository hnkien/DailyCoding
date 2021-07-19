from random import randint


def rand5():
    return randint(1, 5)


def rand7():
    i = 5*rand5() + rand5() - 5  # uniformly samples between 1-25
    if i < 22:
        return i % 7 + 1
    return rand7()
    # return i % 7 + 1


num_experiments = 1000000
result_dict = dict()
for _ in range(num_experiments):
    number = rand7()
    if number not in result_dict:
        result_dict[number] = 0
    result_dict[number] += 1

desired_probability = 1 / 7
print("desired_probability", desired_probability)
for number in result_dict:
    # result_dict[number] = result_dict[number] / num_experiments
    # assert round(desired_probability, 2) == round(result_dict[number], 2)
    print("Number of appear ", number, " ", result_dict[number] / num_experiments)