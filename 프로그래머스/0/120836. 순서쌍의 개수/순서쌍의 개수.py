def solution(n):
    count = 0
    
    for i in range(n+1):
        if n/(i+1) == int(n/(i+1)):
            count+=1
    
    return count