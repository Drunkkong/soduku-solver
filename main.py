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
        board[count] = line
    return board


def main():
    board = get_input()
    print(board)


if __name__ == '__main__':
    main()
