# 연속한 숫자의 합을 구하는 알고리즘
# 입력: n
# 출력: 1부터 n까지 연속한 숫자를 더한 값

def sum_n(n):
    if n == 0:
        return 0
    return sum_n(n-1)+n

print(sum_n(3))
print(sum_n(1))