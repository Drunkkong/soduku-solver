#!usr/bin/env python
# Author: Brandon

def get_input() -> {}:
    """This function returns the array of input from user"""
    print('Input the puzz line by line')
    board = {}
    for count in range(9):
        line = input()
        if len(line) != 9:
            raise ValueError('Size of Line must be 9')
        board[f'{count}'] = line
    return board


def create_squares(board) -> {}:
    square_00 = {"0": [None, None, None], "1": [None, None, None], "2": [None, None, None]}
    square_01 = {"0": [None, None, None], "1": [None, None, None], "2": [None, None, None]}
    square_02 = {"0": [None, None, None], "1": [None, None, None], "2": [None, None, None]}
    square_10 = {"0": [None, None, None], "1": [None, None, None], "2": [None, None, None]}
    square_11 = {"0": [None, None, None], "1": [None, None, None], "2": [None, None, None]}
    square_12 = {"0": [None, None, None], "1": [None, None, None], "2": [None, None, None]}
    square_20 = {"0": [None, None, None], "1": [None, None, None], "2": [None, None, None]}
    square_21 = {"0": [None, None, None], "1": [None, None, None], "2": [None, None, None]}
    square_22 = {"0": [None, None, None], "1": [None, None, None], "2": [None, None, None]}

    for row in board:
        for letter in board[row]:
            if row == 0:
                square_00["0"] = letter

    return {"00": square_00, "01": square_01, "02": square_02, "10": square_10, "11": square_11, "12": square_12,
            "20": square_20, "21": square_21, "22": square_22}


def main():
    board = get_input()
    squares = create_squares(board)
    print(board)
    print(squares)


if __name__ == '__main__':
    main()
