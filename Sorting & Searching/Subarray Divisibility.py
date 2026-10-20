import sys
from collections import defaultdict
data = sys.stdin.read().split()
n, x = int(data[0]), int(data[1])
arr = list(map(int, data[2 : 2 + n]))
pref = ans = 0
cnt = defaultdict(int)
cnt[0] = 1
for v in arr:
    pref += v
    mod = pref % n
    ans += cnt[mod]
    cnt[mod] += 1
print(ans)
