# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

N = int(input())

arr = list(map(int, input().split()))
arr.sort()
result = []

M = int(input())

arr2 = list(map(int, input().split()))

for i in arr2:
    
    left = 0
    right = N - 1
    found = False

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == i:
            found = True
            break
            
        elif arr[mid] > i:
            right = mid - 1
        
        else :
            left = mid + 1 

    if found:
        result.append('1')
    else:
        result.append('0')
        
        
print("\n".join(result))