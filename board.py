# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 06:06:58 2021

@author: Kovid
"""


class Board:
    def __init__(self):
        self.board = [[u"\u2591" for _ in range(10)] for _ in range(10)]  # make board with water 10x10 matrix

    def __getitem__(self, point):  # getter and setter dunder methods
        row, col = point
        return self.board[row][col]

    def __setitem__(self, point, value):
        row, col = point
        self.board[row][col] = value

    def board_plot(self):
        print('  0 1 2 3 4 5 6 7 8 9')
        i = 0
        for row in self.board:
            print(f'{i} ', end='')
            print(' '.join(row), end='\n')
            i += 1

    # Check ship size and space validity

    def check_ship_placement(self, row, col, size, orientation):
        valid_coordinates = []
        for i in range(size):
            if row in range(10) and col in range(10):
                if self.board[row][col] == u"\u2591":  # check if open water
                    valid_coordinates.append((row, col))
                    if orientation:  # True = horizontal
                        col += 1
                    else:
                        row += 1
                else:
                    return False
            else:
                return False
        if size == len(valid_coordinates):
            return True
        else:
            return False

    # Make changes to board to show ship

    def place_ship(self, row, col, size, orientation):
        for _ in range(size):
            self.board[row][col] = u"\u2588"  # place solid square to represent ship
            if orientation:  # True = horizontal
                col += 1
            else:
                row += 1
