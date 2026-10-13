def flood_fill(grid, r, c, color):
    original = grid[r][c]
    if original == color:
        return grid
    rows, cols = len(grid), len(grid[0])

    def fill(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] != original:
            return
        grid[r][c] = color
        fill(r + 1, c)
        fill(r - 1, c)
        fill(r, c + 1)
        fill(r, c - 1)

    fill(r, c)
    return grid
