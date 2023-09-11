def solution(array):
    answer=[max(array), array.index(max(array))]
    return answer

# max()의 시간복잡도 O(n), 따라서 쓰지 않는 방법도 알아두기

def solution(array):
    largest=0
    for i, num in enumerate(array):
        if num>largest:
            largest=num
            largest_idx=i
    return [largest, largest_idx]

# 정렬로 풀기

def solution(array):
    num, i = sorted(enumerate(array), key=lambda x: x[1])[-1]
    answer=[num,i]
