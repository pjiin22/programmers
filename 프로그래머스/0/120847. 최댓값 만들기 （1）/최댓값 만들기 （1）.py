def solution(numbers):
    m=0
    for i in range(0, len(numbers)-1):
        for j in range(i+1,len(numbers)):
            if numbers[i]*numbers[j] > m:
                m=numbers[i]*numbers[j]
    
    return m