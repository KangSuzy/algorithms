# 최대공약수 구하기
# 입력 : a,b
# 출력 : a와 b의 최대공약수


def gcd(a,b):
    if b == 0 :
        return a
    return gcd(b, a%b)

print(gcd(60,24))