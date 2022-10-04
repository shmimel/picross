from solver import solve_puzzle
from printer import drawpuzzle
from picrosspuzzle import PicrossPuzzle

def main():
    # drawpuzzle([[[1,1,1],[5],[3],[1,1],[3]],[[2],[4],[3,1],[4],[2]]])
    # print(create_combos([1,2], 6))
    # print(mark_known([[0,0,0],[1,1,1]]))
    # print(cull_combos([[1, 1, 0, 0, 0], [1, 1, -1, -1, -1], [1, 1, -1, 1, -1], [-1, 1, 1, -1, -1]]))
    # clues = [[[1,1,1],[5],[3],[1,1],[3]],[[2],[4],[3,1],[4],[2]]]
    # clues = [[[2,1],[1,3],[1,2],[3],[4],[1]],[[1],[5],[2],[5],[2,1],[2]]]
    clues = [[[2],[1,1],[4],[2,1],[3,1],[8],[8],[7],[5],[3]],[[1],[2],[1,6],[9],[6],[5],[5],[4],[3],[4]]]
    row_clues = [(2,),(1,1),(4,),(2,1),(3,1),(8,),(8,),(7,),(5,),(3,)]
    col_clues = [(1,),(2,),(1,6),(9,),(6,),(5,),(5,),(4,),(3,),(4,)]
    puzzle = PicrossPuzzle(row_clues, col_clues)
    pix_grid = solve_puzzle(puzzle)
    print(pix_grid)
    drawpuzzle(clues, pix_grid)
    

if __name__ == "__main__":
    main()
    
    



