import numpy as np
import itertools

def max_list(list):
    list_len = [len(i) for i in list]
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
    x_pad = max_list(rows)
    col_clues = []

    for i in range(max_list(cols)):
        col_fix = []
        for col in cols:
            col = list(reversed(col))
            if len(col) >= i+1:
                col_fix.append(col[i])
            else:
                col_fix.append(' ')
        col_clues.insert(0,col_fix)
    
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
        
def create_combos(clue, length):
    num_groups = len(clue)
    num_empty = length - (sum(clue) + (len(clue)-1))
    combos = list(itertools.combinations(range(num_groups+num_empty), num_groups))

    pix_combos = []
    for combo in combos:
        start = 0
        pix_line = []
        while combo[0] > start:
            pix_line.append(-1)
            start += 1
        for _ in range(clue[0]):
            pix_line.append(1)
        for i in range(1,len(combo)):
            for _ in range(combo[i]-combo[i-1]):
                pix_line.append(-1)
            for _ in range(clue[i]):
                pix_line.append(1)

        while len(pix_line) < length:
            pix_line.append(-1)
        pix_line = pix_line[:length]
        pix_combos.append(pix_line)

    return pix_combos


def mark_known(combos):
    pixs = []
    for i in range(len(combos[0])):
        pix = []
        for j in range(len(combos)):
            pix.append(combos[j][i])
        pixs.append(pix)
    
    known = np.zeros(len(combos[0]))
    known = known.astype(int)

    for i, pix in enumerate(pixs):
        if pix.count(pix[0]) == len(pix):
            known[i] = pix[0]
    
    return known


def cull_combos(combos):
    for i in range(len(combos[0])):
        if combos[0][i] != 0:
            for j in range(len(combos)):
                if combos[0][i] != combos[j][i]:
                    combos[j] = combos[0]
    culled = []
    for combo in combos:
        if combo not in culled:
            culled.append(combo)
    if len(culled) > 1:
        return culled[1:]
    else:
        return culled
    

def solve_puzzle(clues):
    rows = clues[0]
    cols = clues[1]

    pix_grid = np.zeros((len(cols), len(rows)))

    row_combos = []
    col_combos = []
    for row in rows:
        com = create_combos(row, len(cols))
        row_combos.append(com)
    for col in cols:
        com = create_combos(col, len(rows))
        col_combos.append(com)


    while 0 in pix_grid:
        for i, combo in enumerate(row_combos):
            combo.insert(0,list(pix_grid[i]))
            pix_line = cull_combos(combo)
            if len(pix_line[0]) > 1:
                pix_line = mark_known(pix_line)
                pix_grid[i] = pix_line

        for i, combo in enumerate(col_combos):
            combo.insert(0,list(pix_grid[:, i]))
            pix_line = cull_combos(combo)
            if len(pix_line[0]) > 1:
                pix_line = mark_known(pix_line)
                pix_grid[:,i] = pix_line

    return pix_grid

    


def main():
    # drawpuzzle([[[1,1,1],[5],[3],[1,1],[3]],[[2],[4],[3,1],[4],[2]]])
    # print(create_combos([1,2], 6))
    # print(mark_known([[0,0,0],[1,1,1]]))
    # print(cull_combos([[1, 1, 0, 0, 0], [1, 1, -1, -1, -1], [1, 1, -1, 1, -1], [-1, 1, 1, -1, -1]]))
    # clues = [[[1,1,1],[5],[3],[1,1],[3]],[[2],[4],[3,1],[4],[2]]]
    # clues = [[[2,1],[1,3],[1,2],[3],[4],[1]],[[1],[5],[2],[5],[2,1],[2]]]
    # clues = [[[2],[1,1],[4],[2,1],[3,1],[8],[8],[7],[5],[3]],[[1],[2],[1,6],[9],[6],[5],[5],[4],[3],[4]]]
    # pix_grid = solve_puzzle(clues)
    # drawpuzzle(clues, pix_grid)
    clues = '1.1.1,5,3,1.1,3/2,4,3.1,4,2'
    clues = convert_clues(clues)
    pix_grid = solve_puzzle(clues)
    drawpuzzle(clues, pix_grid)

main()
    
    



