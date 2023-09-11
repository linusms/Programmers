def solution(num_list, n):
    start=0
    end=0
    answer = []
    while start!=len(num_list):
        end+=n
        answer.append(list(num_list[start:end]))
        start+=n
    return answer

# 개선

def solution(num_list,n):
    idx=0
    answer=[]
    while idx<len(num_list):
        answer.append([num_list[idx:idx+n]])
    return answer

# list comprehension 사용

def solution(num_list,n):
    return [[num_list[idx:idx+n]] for idx in range(0, len(num_list), n)]
