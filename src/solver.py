from numpy import zeros
from numpy import ndarray
import numpy as np
from itertools import combinations
from picrosspuzzle import PicrossPuzzle


def create_combos(clue, length):
    num_groups = len(clue)
    num_empty = length - (sum(clue) + (len(clue)-1))
    combos = list(combinations(range(num_groups+num_empty), num_groups))

    pix_combos = []
    # pix_combos = zeros((len(length), len(combos)))
    # print(pix_combos)
    for i, combo in enumerate(combos):
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
    for i, _ in enumerate(combos[0]):
        pix = []
        for j, _ in enumerate(combos):
            pix.append(combos[j][i])
        pixs.append(pix)
    
    known = zeros(len(combos[0]))
    known = known.astype(int)

    for i, pix in enumerate(pixs):
        if pix.count(pix[0]) == len(pix):
            known[i] = pix[0]
    
    return known


def cull_combos(combos):
    for i, _ in enumerate(combos[0]):
        if combos[0][i] != 0:
            for j, _ in enumerate(combos):
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


def contradiction(pix_grid, clues):
    return None


def fill_pix(pix_grid, row_combos, col_combos):
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


def solve_puzzle(puzzle: PicrossPuzzle) -> ndarray:

    pix_grid = zeros((puzzle.width, puzzle.height))
    pix_grid_prev = zeros((puzzle.width, puzzle.height))

    row_combos = []
    col_combos = []

    for row in puzzle.row_clues:
        com = create_combos(row, puzzle.width)
        row_combos.append(com)
    for col in puzzle.col_clues:
        com = create_combos(col, puzzle.height)
        col_combos.append(com)

    n = 0
    while 0 in pix_grid:
        pix_grid = fill_pix(pix_grid, row_combos, col_combos)
        if np.array_equal(pix_grid, pix_grid_prev):
            print('fuck')
            break
        pix_grid_prev = pix_grid.copy()
        print(n)
        n += 1

        

    return pix_grid