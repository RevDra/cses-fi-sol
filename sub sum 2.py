import sys
from collections import defaultdict
data = sys.stdin.read().split()
n, x = int(data[0]), int(data[1])
arr = list(map(int, data[2 : 2 + n]))
cnt = defaultdict(int)
cnt[0] = 1
pref = ans = 0
for v in arr:
    pref += v
    ans += cnt[pref - x]
    cnt[pref] += 1
print(ans)