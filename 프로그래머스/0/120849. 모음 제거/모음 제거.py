def solution(my_string):
    k=''
    for i in my_string:
        if i != 'a' and i!='e'and i!='i' and i!='o' and i!='u':
            k+=i
            
    return k