

class PicrossPuzzle:

    def __init__(self, row_clues: "list[tuple]", col_clues: "list[tuple]") -> None:
        self.row_clues = row_clues 
        self.col_clues = col_clues
        self.width = len(self.row_clues)
        self.height = len(self.col_clues)
        

