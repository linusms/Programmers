def solution(i, j, k):
    num_cmp=[]
    for num in range(i,j+1):
        while True:
            if num//10!=0:
                num_cmp.append(num%10)
                num=num//10
            else:
                num_cmp.append(num)
                break
            
    answer=num_cmp.count(k)           
    return answer
