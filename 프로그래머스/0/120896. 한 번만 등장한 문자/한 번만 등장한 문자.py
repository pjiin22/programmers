def solution(s):
    answer = ''
    n=list(s)
    n.sort()
    n.append(" ")
    n.insert(0," ")
    print(n)
    
    for i in range(1,len(n)-1):
        if n[i]!=n[i-1] and n[i]!=n[i+1]:
            answer+=n[i]
            
    return answer