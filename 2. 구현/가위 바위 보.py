# 1. 가위 바위 보

def solution(rsp):
    answer_list=[]
    for i in rsp:
        if i=='2':
            answer_list.append("0")
        elif i=='0':
            answer_list.append("5")
        else:
            answer_list.append("2")
    answer=''.join(answer_list)
    return answer

# 더 나은 풀이 : 문자열은 +가 가능하다

def solution(rsp):
    answer = ''
    for i in rsp:
        if i == '2':
            answer+='0'
        elif i == '0':
            answer+='5'
        else :
            answer+='2'
    
    return answer
