# 문자열 거꾸로 변환 : [::-1]
# 거꾸로 된 문자열을 iter 한 객체로 반환하기 : reversed(string) 

from collections import Counter

def solution(my_string):
    my_string=my_string[::-1]
    for chr in set(my_string):
        chr_iter=Counter(my_string)[chr]
        my_string=my_string.replace(chr,"",chr_iter-1)
    answer=my_string[::-1]
    return answer
