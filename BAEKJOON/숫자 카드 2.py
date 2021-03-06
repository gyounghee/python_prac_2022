# 10816번 - 숫자 카드 2

## 풀이 1
from sys import stdin
from collections import defaultdict

N, num = int(stdin.readline()), list(map(int, stdin.readline().split()))
M, find = int(stdin.readline()), list(map(int, stdin.readline().split()))

num_dict = defaultdict(int)
for n in num :
    num_dict[n] += 1

for f in find :
    print(num_dict[f],end=' ')


## 풀이 2
from sys import stdin
from collections import Counter

N, num = int(stdin.readline()), list(map(int, stdin.readline().split()))
M, find = int(stdin.readline()), list(map(int, stdin.readline().split()))

num_dict = Counter(num)

for f in find :
    print(num_dict[f],end=' ')
