# 효율성 테스트 30ms
# 스택 사용

def solution(s):
    answer = True
    stack=[]
    for chr in s:
        stack.append(chr)
        if stack[-2:]==["(",")"]:
            for i in range(2):
                stack.pop()
    if stack!=[]:
        answer=False
    
    return answer

# 효율성 테스트 7ms
# ( 먼저 오지 않은 상태에서 )가 들어오면 무조건 False
# 실질적으로 stack에 들어가는 원소는 ( 하나. )가 오면 (를 없애 빈 스택 만들기

def solution(s):
    stack=[]
    for chr in s:
        if chr=="(":
            stack.append(chr)
        elif chr==")":
            if not stack:
                return False
            stack.pop()
    return len(stack)==0
    
 
