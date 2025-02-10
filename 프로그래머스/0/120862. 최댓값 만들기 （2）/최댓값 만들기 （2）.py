def solution(numbers):

    m=-10000000000
    for i in range(0,len(numbers)-1):
        for j in range(i+1,len(numbers)):
            m=max(m,numbers[i]*numbers[j])
              
    return m