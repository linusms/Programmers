# 스택을 사용하지 않고도 풀 수 있다

def solution(arr):
    answer = [arr[0]]
    i=0
    while i<len(arr)-1:
        if arr[i]!=arr[i+1]:
            answer.append(arr[i+1])
        i+=1
    return answer

# (한 숫자씩만 저장하므로 굳이 리스트 형식으로 스택 필요없음)

def solution(arr):
  answer=[arr[0]]
  stack=None
  for num in arr:
    if stack is not None:
      previous_num=stack
      if previous_num!=num:
        answer.append(num)
    stack=num
  return answer

# 스택을 사용

def solution(arr):
  stack=[]
  answer=[arr[0]]
  for num in arr:
    if stack:
      previous_num=stack.pop()
      if previous_num!=num:
        answer.append(num)
      stack.append(num)
  return answer
  
