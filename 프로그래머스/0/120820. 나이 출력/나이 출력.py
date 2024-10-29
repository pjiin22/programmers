def solution(age):
    answer = 0
    if age <= 23:
        answer = 2022 - age + 1
    else:
        age1 = age - 22
        answer = 2000 - age1 + 1
    return answer