def solution(arr1, arr2):
    
    answer = []
    for row, row_array in enumerate(arr1):
        for col, col_value in enumerate(row_array):
            row_array[col]=col_value+arr2[row][col]
        answer.append(row_array)
            
    return answer

# zip 함수 사용시 더 간단히 정리가능
# 여러 배열에 zip -> 여러개의 원소 가지는 튜플들 생성(iterable)
# n

def solution(arr1, arr2):
  answer=[[c+d for c,d in zip(a,b)] for a,b in zip(arr1,arr2)]
