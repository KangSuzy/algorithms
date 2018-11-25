"""
Sum 성공
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	29349	21247	19153	73.643%
문제
John got a bad mark in math. The teacher gave him another task. John is to write a program which computes the sum of integers from 1 to n. If he manages to present a correct program, the bad mark will be cancelled.

Write a program which:

reads the number n from the standard input,
computes the sum of integers from 1 to n,
writes the answer to the standard output.
입력
The first and only line of the standard input contains one integer n (1 ≤ n ≤ 10 000).



출력
One integer is to be written to the standard output. This integer should be the sum of integers from 1 to n.

예제 입력 1
3
예제 출력 1
6
"""
N = int(input())
result = 0
for i in range(N+1):
    result += i
print(result)