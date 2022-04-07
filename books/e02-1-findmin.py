# 최솟값 구하기
# 입력: 숫자 n 개가 들어있는 리스트
# 출력: 숫자 n개 중 최솟값

def find_min(a):
    n = len(a)
    min_n = a[0]
    for i in range(1, n):
        if min_n > a[i]:
            min_n = a[i]
    return min_n

a = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_min(a))