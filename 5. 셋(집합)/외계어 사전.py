# 같은 집합인지 확인은 먼저 두 배열을 set으로 변환후 가능

def solution(spell, dic):
    answer=2
    for word in dic:
        if set(word)==set(spell):
            for chr in set(word):
                word=word.replace(chr,"",1)
            if word=="":
                answer=1

    return answer
