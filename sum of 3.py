import sys
data = sys.stdin.read().split()
n, x = int(data[0]), int(data[1])
arr = list(map(int, data[2 : 2 + n]))
idx = []
for index, value in enumerate(arr):
    idx.append((value, index + 1))
idx.sort()

for i in range(n):
    left = i + 1
    right = n - 1
    while left < right:
        total = idx[i][0] + idx[left][0] + idx[right][0]
        if total < x:
            left += 1
        elif total > x:
            right -= 1
        else:
            print(idx[i][1], idx[left][1], idx[right][2])
            exit()
print('IMPOSSIBLE')