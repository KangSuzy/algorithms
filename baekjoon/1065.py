'''
한수 성공
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	117055	62633	52373	53.275%
문제
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
'''
n = int(input())
cnt = 0

for i in range(1, n+1):
    if i < 100:
        cnt += 1
    elif i == 1000:
        continue
    else:
        tmp = []
        for j in str(i):
            tmp.append(int(j))
            
        first = tmp[0] - tmp[1]
        second = tmp[1] - tmp[2]
        
        if first == second:
            cnt += 1
print(cnt)