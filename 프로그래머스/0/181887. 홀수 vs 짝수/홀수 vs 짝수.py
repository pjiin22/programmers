def solution(num_list):
    n1=0
    n2=0
    for i, j in enumerate(num_list):
        if i%2==0:
            n1+=j
        else:
            n2+=j
    
    
    
    return max(n1,n2)