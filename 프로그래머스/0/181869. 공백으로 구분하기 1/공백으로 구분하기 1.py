def solution(my_string):
    answer = []
    n=''
    for i in my_string:
        if i == ' ':
            answer.append(n)
            n=''
        else:
            n+=i
    
    answer.append(n)
    return answer