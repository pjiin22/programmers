def solution(array):
    answer = 0
    array=str(array)
    n=''.join(map(str,array))
              
    for i in range(0,len(n)):
        if n[i] == '7':
            answer+=1
    
    return answer
              
              