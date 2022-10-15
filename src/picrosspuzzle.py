

def convert_clues(clues):
    converted = [[],[]]
    row_col = clues.split('/')
    for i, item in enumerate(row_col):
        item = item.split(',')
        for clue in item:
            clue = clue.split('.')
            clue = tuple(int(x) for x in clue)
            converted[i].append(clue)
    return converted

class PicrossPuzzle:

    def __init__(self, row_clues: "list[tuple]", col_clues: "list[tuple]") -> None:
        self.row_clues = row_clues 
        self.col_clues = col_clues
        self.width = len(self.row_clues)
        self.height = len(self.col_clues)
        

