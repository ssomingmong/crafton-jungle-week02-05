# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157


string = input().upper()
counts = {}

for i in string:
    counts[i] = counts.get(i, 0) + 1

max_value = max(counts.value())

result = []

for i in counts:
    if counts[i] == max_value:
        result.append(i)

if len(result) > 0:
    print("?")

else:
    print(result[0])