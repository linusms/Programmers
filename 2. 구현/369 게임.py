def solution(order):
    answer=0
    order_cmp=[]
    while True:
        if order//10!=0:
            order_cmp.append(order%10)
            order=order//10
        else:
            order_cmp.append(order)
            break
    for i in [3,6,9]:
        answer+=order_cmp.count(i)
    return answer
