def solution(num, total):
    answer = []
    num_sum=0
    for i in range(num):
        num_sum+=i
    start_num=int((total-num_sum)/num)
    for i in range(num):
        answer.append(start_num+i)
    
    return answer
