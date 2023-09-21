# 리스트의 모든 원소에 -1 곱하는것
# a*=-1 같은 해괴한 문법 시도해보았으나 빈 리스트만 반환
# 정석적인 list(map()) 적용
# heap에는 list 자료형만 들어갈 수 있다
# 작업량보다 남은 일 시간이 많은 경우 예외처리 신경쓰기(works[0]==0:)
# 가장 중요한 발상 : heap 자료형에서 가장 큰 수를 빼서 1씩 빼는것 반복하면 최적의 works가 완성됨
# heap의 가장 중요한 기능 : 안에 있는 원소를 뺏다 넣었다 해도 항상 정렬해줌

import heapq

def solution(n, works):
    answer = 0
    works=list(map(lambda x: -1*x, works))
  
    heapq.heapify(works)
    for _ in range(n):
        popwork=heapq.heappop(works)+1
        heapq.heappush(works, popwork)
        if works[0]==0:
            break
    for work in works:
        answer+=work**2
      
    return answer

# 같은 논리지만 더 pythonic 하게 코드 정리

import heapq

def solution(n, works):
    answer = 0
    works=[-work for work in works]
  
    heapq.heapify(works)
    for _ in range(n):
        popwork=heapq.heappop(works)
        heapq.heappush(works, popwork)
        if works[0]==0:
            break
          
    return sum([work**2 for work in works])
