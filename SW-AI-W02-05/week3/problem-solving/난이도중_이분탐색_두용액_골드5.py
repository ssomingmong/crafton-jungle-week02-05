# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470

import sys
input = sys.stdin.readline

N = int(input())
solution = list(map(int, input().split()))
solution.sort()

left = 0
right = N - 1
best = float('inf')
answer_left = solution[left]
answer_right = solution[right]

while left < right:
    total = solution[left] + solution[right]

    if abs(total) < best:
        best = abs(total)
        answer_left = solution[left]
        answer_right = solution[right]
    
    if total > 0:
        right -= 1
    elif total < 0:
        left += 1
    else:
        break

print(answer_left, answer_right)