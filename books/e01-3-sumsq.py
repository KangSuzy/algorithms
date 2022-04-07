# 연속한 숫자의 제곱의 합을 구하는 알고리즘
# 입력: n
# 출력: 1부터 n까지 연속한 숫자의 제곱을 더한 값
def sum_sq(n):
    return n*(n+1)*(2*n+1)//6

print(sum_sq(10))
print(sum_sq(100))