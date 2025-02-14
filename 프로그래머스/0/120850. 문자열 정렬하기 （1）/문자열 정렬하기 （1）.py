def solution(my_string):
    answer = []
    for i in my_string:
        if i in ['0','1','2','3','4','5','6','7','8','9']:
            answer.append(i)
            answer.sort()
            answer1=list(map(int,answer))
    return answer1