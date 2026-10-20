import sys
 
def solve():
    n = int(sys.stdin.readline())
    res = [n]
    
    while n != 1:
        if n & 1 == 0:
            n >>= 1
        else:
            n = 3 * n + 1
        res.append(n)
        
    sys.stdout.write(' '.join(map(str, res)))
 
if __name__ == '__main__':
    solve()
