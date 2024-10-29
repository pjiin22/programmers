def solution(my_string):
    answer = my_string
    for a in "aeiou":
        answer = answer.replace(a, "")
    return answer
