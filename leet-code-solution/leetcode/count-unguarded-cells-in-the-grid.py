class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        C = defaultdict(lambda: 1)
        for x, y in guards:
            C[x, y] = 'G'
        for x, y in walls:
            C[x, y] = 'W'
        # map all walls and guards

        for r in range(m):
            # right
            g = 0
            for c in range(n):
                if C[r, c] == 'G':
                    g = 1
                elif C[r, c] == 'W':
                    g = 0
                if g and C[r, c] != 'G':
                    C[r, c] = 0
            # left
            g = 0
            for c in range(n - 1, -1, -1):
                if C[r, c] == 'G':
                    g = 1
                elif C[r, c] == 'W':
                    g = 0
                if g and C[r, c] != 'G':
                    C[r, c] = 0

        for c in range(n):
            # down
            g = 0
            for r in range(m):
                if C[r, c] == 'G':
                    g = 1
                elif C[r, c] == 'W':
                    g = 0
                if g and C[r, c] != 'G':
                    C[r, c] = 0
            # up
            g = 0
            for r in range(m - 1, -1, -1):
                if C[r, c] == 'G':
                    g = 1
                elif C[r, c] == 'W':
                    g = 0
                if g and C[r, c] != 'G':
                    C[r, c] = 0
        return sum(int(C[x, y] == 1) for x in range(m) for y in range(n))