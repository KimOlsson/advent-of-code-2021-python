from bingo import Bingo
from sys import exit

ROW_LENGTH = 5

def read_file_to_list(fname: str, encoding='utf-8') -> list[str]:
    data = []
    with open(fname, 'r', encoding=encoding) as file:
        for line in file:
            data.append(line.strip())
    return data

def str_to_int(value: str) -> int:
    try:
        return int(value)
    except ValueError:
        exit('You attempted to convert value {} to int\nQuitting..'.format(value))

def parse_bingo_boards(raw_boards: list[str]) -> list[list[int]]:
    boards_without_empty_lines = [x for x in raw_boards if len(x.strip())]
    board = []
    boards = []
    for row in boards_without_empty_lines:
        board_row = row.split()
        board_row_int = [str_to_int(x) for x in board_row]
        board.append(board_row_int)
        
        is_board_full = len(board) == ROW_LENGTH
        if is_board_full:
            boards.append(board)
            board = []
    return boards


def draw_all_numbers(bingo_objects: list[Bingo], numbers: list[int]) -> list[tuple[Bingo, int]]:
    all_winners = []
    for number in numbers:
        for board in bingo_objects:
            if not board.is_hit(number):
                continue
            if not board.has_point():
                continue
            all_winners.append((board, number))
    return all_winners


def run():
    raw_bingo_data = read_file_to_list('bingo_data')
    drawn_numbers = raw_bingo_data[0].split(',')
    drawn_numbers_int = [str_to_int(x) for x in drawn_numbers]
    raw_bingo_boards = raw_bingo_data[1:]
    bingo_boards = parse_bingo_boards(raw_bingo_boards)
    bingo_objects = [Bingo(x, ROW_LENGTH) for x in bingo_boards]

    all_winners_in_order = draw_all_numbers(bingo_objects, drawn_numbers_int)
    winner, winner_with_number = all_winners_in_order[0]
    print(f"\nWinner was board:\n\n{str(winner)}\n\nWith score {winner.get_board_score(winner_with_number)}")

    last_winner, last_winner_with_number = all_winners_in_order[-1]
    print(f"\nLast to win board:\n\n{str(last_winner)}\n\nWith score {last_winner.get_board_score(last_winner_with_number)}")

if __name__ == '__main__':
    run()