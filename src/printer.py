def longest_sublist_len(lst):
    list_len = [len(i) for i in lst]
    return max(list_len)

def convert_clues(clues):
    converted = [[],[]]
    row_col = clues.split('/')
    for i, item in enumerate(row_col):
        item = item.split(',')
        for clue in item:
            clue = clue.split('.')
            clue = [int(x) for x in clue]
            converted[i].append(clue)
    return converted

def drawpuzzle(clues, pix_grid):
    rows = clues[0]
    cols = clues[1]
    x_pad = longest_sublist_len(rows)
    col_clues = []

    for i in range(longest_sublist_len(cols)):
        col_fix = []
        for col in cols:
            col = list(reversed(col))
            if len(col) >= i+1:
                col_fix.append(col[i])
            else:
                col_fix.append(' ')
        col_clues.insert(0, col_fix)

    for col_clue in col_clues:
        print(' ' * (x_pad+1), *col_clue)

    ascii_grid = []
    for row in pix_grid:
        ascii_row = []
        for pix in row:
            if pix == 1:
                ascii_row.append('░')
            else:
                ascii_row.append('█')
        ascii_grid.append(ascii_row)

    row_clues = []
    for row in rows:
        while len(row) < x_pad:
            row.insert(0, ' ')
        row_clues.append(row)

    for i, row_clue in enumerate(row_clues):
        print(*row_clue, *ascii_grid[i])
    
def draw_grid(pix_grid):
    ascii_grid = []
    for row in pix_grid:
        ascii_row = []
        for pix in row:
            if pix == 1:
                ascii_row.append('░')
            else:
                ascii_row.append('█')
        ascii_grid.append(ascii_row)
    for row in ascii_grid:
        print(*row)