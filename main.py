class Solution:
    def solve(self):
        n, m = input().strip().split()
        n, m = int(n), int(m)
        arr = []
        for i in range(m):
            a, b = input().split()
            a, b = int(a), int(b)
            arr.append((a, b))
        return arr
