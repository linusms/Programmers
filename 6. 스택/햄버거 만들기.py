# 스택없이 계산
# 계산 속도가 매우 느림
# 중간에 포장된 햄버거 배열 제거하는 부분을 del로 간소화하지 않으면
# 런타임오류 발생

def solution(ingredient):
    idx,cnt=0,0
    while idx<len(ingredient)-3:
        if ingredient[idx:idx+4]==[1,2,3,1]:
            del ingredient[idx:idx+4]
            idx-=2
            cnt+=1
        else:
            idx+=1
        
    return cnt

# 스택 자료구조 사용
# 리스트 끝에서 원소 제거하는 pop()
# 리스트 끝에서부터 몇 개의 원소 제거하는 방법
# 끝에서부터 하는 정해진 개수만큼의 연산은 중간 인덱싱보다 훨씬 빠름 

def solution(ingredient):
    stack=[]
    cnt=0
    for food in ingredient:
        stack.append(food)
        if stack[-4:]==[1,2,3,1]:
            cnt+=1
            for i in range(4):
                stack.pop()
    return cnt
  
