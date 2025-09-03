class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)

        # 1) Coordinate compression
        xs = sorted({x for x, _ in points})
        ys = sorted({y for _, y in points})
        x_id = {x: i+1 for i, x in enumerate(xs)}  # 1-based
        y_id = {y: i+1 for i, y in enumerate(ys)}  # 1-based

        nx, ny = len(xs), len(ys)

        # 2) Grid and 2D prefix sum
        grid = [[0]*(ny+1) for _ in range(nx+1)]  # 1..nx, 1..ny
        comp = []
        for x, y in points:
            cx, cy = x_id[x], y_id[y]
            comp.append((cx, cy))
            grid[cx][cy] = 1

        ps = [[0]*(ny+1) for _ in range(nx+1)]
        for i in range(1, nx+1):
            row_sum = 0
            for j in range(1, ny+1):
                row_sum += grid[i][j]
                ps[i][j] = ps[i-1][j] + row_sum

        def rect_sum(x1, y1, x2, y2):
            if x1 > x2 or y1 > y2:
                return 0
            return (ps[x2][y2] - ps[x1-1][y2] - ps[x2][y1-1] + ps[x1-1][y1-1])

        # 3) Count valid (Alice,Bob) ordered pairs
        ans = 0
        for i in range(n):
            xi, yi = comp[i]
            for j in range(n):
                if i == j:
                    continue
                xj, yj = comp[j]
                # Alice upper-left, Bob lower-right
                if xi <= xj and yi >= yj:
                    # Rectangle [xi..xj] × [yj..yi] must contain only these two points
                    if rect_sum(xi, yj, xj, yi) == 2:
                        ans += 1
        return ans
