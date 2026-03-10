# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819


N = int(input())

arr = list(map(int, input().split()))
min = sorted(arr)
max = sorted(arr, reverse=True)
result = 0
for i in range(len(arr)):
    for j in range(len(arr) - 1):
        result += (-1) * (min[i] - max[i])

print(result)