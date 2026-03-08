# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

C = int(input())

for i in range(C):
    data = list(map(int, input().split()))
    N = data[0]
    scores = data[1:]
    avg = sum(scores) / N
    counts = 0
    for s in scores:
        if s > avg:
            counts += 1
    ratio = (counts / N) * 100
    print(f"{ratio:.3f}%")