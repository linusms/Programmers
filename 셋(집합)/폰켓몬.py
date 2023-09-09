def solution(nums):
    if len(set(nums))<=len(nums)/2:
        answer=len(set(nums))
    else:
        answer=len(nums)/2
    return answer

# 더 간단한 풀이

def solution(nums):
  return min(len(set(nums)), len(nums)/2)
