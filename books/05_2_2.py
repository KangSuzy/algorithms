sit_min = 2
sit_max = 10
total = 100
memo = {}

def problem(remain, sitin):
    key = str([remain, sitin])
    # 종료조건
    if key in memo:
        return memo[key]
    if remain < 0: # 무효이므로 0을 리턴
        return 0
    if remain == 0: # 유효하므로 1을 리턴
        return 1

    # 재귀 처리
    count  = 0
    for i in range(sitin, sit_max + 1):
        count += problem(remain-i, i)

    # 메모화 처리
    memo[key] = count

    # 종료
    return count

print(problem(total,sit_min))