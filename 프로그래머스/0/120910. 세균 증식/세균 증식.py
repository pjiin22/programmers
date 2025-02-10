def solution(n, t):
    if t == 0:
        return n
    else:
        return solution(2*n,t-1)