class Bingo:
    """
    This class lets you create a bingo board with your preferred width (row_length).
    It lets you to update drawn bingo numbers and has functions to test if you
    made a point vertically or horizontally.

    After a point has been made, drawn number hits are no longer updated, hence
    score stays as is after winning.
    """

    def __init__(self, board: list[list[int]], row_length=5):
        self.row_length = row_length
        self.board = []
        self.hits = []
        self.board_score = 0
        self.set_board(board)

    def set_board(self, data: list[list[int]]):
        if len(data) != self.row_length:
            raise ValueError('Length of data was not {}'.format(self.row_length))
        for row in data:
            if len(row) != self.row_length:
                raise ValueError('Length of a row was not {}'.format(self.row_length))
            self.board.append(row)
            self.board_score += sum(row)
            self.hits.append([0]*self.row_length)

    def is_hit(self, num: int):
        if self.has_point():
            return False
        
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if col == num:
                    self.hits[i][j] = 1
                    self.board_score -= num
                    return True
        return False

    def has_horizontal_point(self):
        for row in self.hits:
            if sum(row) == self.row_length:
                return True
        return False

    def has_vertical_point(self):
        for i in range(self.row_length):
            hit_sum = 0
            for row in self.hits:
                hit_sum += row[i]
            
            if hit_sum == self.row_length:
                return True
        return False

    def has_point(self):
        return self.has_vertical_point() or self.has_horizontal_point()

    def get_board_score(self, last_number: int):
        return self.board_score * last_number

    def __repr__(self):
        result = []
        for i, row in enumerate(self.board):
            line1 = "{:<2}{:>3}{:>3}{:>3}{:>3}".format(*row)
            line2 = "{:<1}{:>3}{:>3}{:>3}{:>3}".format(*self.hits[i])
            line3 = line1 + ' '*4 + line2
            result.append(line3)
        return '\n'.join(result)