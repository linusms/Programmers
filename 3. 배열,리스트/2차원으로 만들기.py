def solution(num_list, n):
    start=0
    end=0
    answer = []
    while start!=len(num_list):
        end+=n
        answer.append(list(num_list[start:end]))
        start+=n
    return answer
