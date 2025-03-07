def solution(M, N):
    answer = 0
    answer+=min(M,N)-1
    answer+=min(M,N)*(max(M,N)-1)
    return answer