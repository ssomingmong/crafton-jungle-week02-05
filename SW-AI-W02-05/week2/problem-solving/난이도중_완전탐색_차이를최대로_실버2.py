# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

N = int(input())
arr = list(map(int, input().split()))

result = []
used = [False] * N

def permutation(current):
    if len(current) == N:
        sum = 0
        for i in range(N - 1):
            sum += abs(current[i] - current[i+1])
        result.append(sum)
        return
    
    for i in range(N):
        if not used[i]:
            used[i] = True
            current.append(arr[i])
            permutation(current)
            
            current.pop()
            used[i] = False

permutation([])
print(max(result))