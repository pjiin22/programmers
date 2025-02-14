def solution(array, n):
    answer = 0
    d=100
    for i in array:
        if abs(n-i)==abs(n-d):
            d = min(i,d)
        if abs(n-i)<abs(n-d):
            d=i
    
        
    return d