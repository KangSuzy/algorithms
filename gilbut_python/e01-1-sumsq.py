# 연속한 숫자의 제곱의 합을 구하는 알고리즘
# 입력: n
# 출력: 1부터 n까지 연속한 숫자의 제곱을 더한 값
def sum_n(n):
    s = 0
    for i in range(1, n+1):
        s += i*i
    return s

print(sum_n(10))
print(sum_n(100))