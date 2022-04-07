# 최댓값 구하기
# 입력: 숫자가 n개 들어 있는 리스트
# 출력: 숫자 n개 중 최댓값

def find_max(a,n):
    if n == 1:
        return a[0]
    re_max = find_max(a, n-1)
    if re_max < a[n-1]:
        return a[n-1]
    else:
        return re_max

a = [17, 92, 100, 33, 58, 7, 33, 42]
print(find_max(a,8))