# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675


T = int(input())
list = {}

for i in range(T):
    R, S = input().split()
    R = int(R)

    for ch in S:
        print(R * ch, end="")
    print()
