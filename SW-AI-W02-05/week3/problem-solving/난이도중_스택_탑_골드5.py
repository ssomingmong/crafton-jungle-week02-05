# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493

import sys
input = sys.stdin.readline

N = int(input())
height = list(map(int, input().split()))
stack = []
result = [0] * N

for i in range(N):

    while stack and stack[-1][1] < height[i]:
        stack.pop()

    if stack:
        result[i] = stack[-1][0] + 1

    stack.append((i, height[i]))

print(*result)