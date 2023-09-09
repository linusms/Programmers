# 빈 array=False
# 반복문이 끝나도 iteration을 위해 저장해둔 변수 값은 여전히 존재(i, idx 등)
# iterable 한 원소 제거시 비어있는 상태를 False로 두면 중지조건 만들기 쉬움

def solution(array):
    while array:
        for i,value in enumerate(set(array)):
            array.remove(value)
        if not i:
            return value
    return -1
