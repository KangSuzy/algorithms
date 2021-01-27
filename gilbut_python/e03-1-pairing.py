# n명에서 두 명을 뽑아 짝으로 만드는 모든 경우를 찾는 알고리즘
# 입력: n명의 이름이 들어 있는 리스트
# 출력: 두 명을 뽑아 만들 수 있는 모든 짝

def find_mate(a):
    n = len(a)
    for i in range(0, n-1):
        for j in range(i+1, n):
            print(a[i], "-", a[j])

a = ["Tom", "Jerry", "Mike", "Rain"]
print(find_mate(a))