import sys
data = sys.stdin.read().split()
n, x = int(data[0]), int(data[1])
arr = list(map(int, data[2 : 2 + n]))
left = cur = ans = 0
for right in range(n):
    cur += arr[right]
    while cur > x:
        cur -= arr[left]
        left += 1
    if cur == x:
        ans += 1
print(ans)
