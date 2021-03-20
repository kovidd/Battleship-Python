# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 06:22:49 2021

@author: Kovid
"""

from board import Board
from ship import Ship


def validate_input(message):
    flag = True
    while flag:
        try:
            val = int(input(message))
            flag = False
        except ValueError:
            print('Invalid input, try again.')
    return val


class Player:
    def __init__(self, num_ships):
        self.board = Board()
        self.num_ships = num_ships
        self.fleet = []

    # Ship co-ordinates are added to a list in fleet

    def make_fleet(self):
        for ship in range(self.num_ships):
            flag = True
            while flag:
                try:
                    print(f'Place your ship number {ship + 1} at ')
                    row = validate_input('Place ship at (row): ')
                    col = validate_input('Place ship at (col): ')
                    orientation = (input('Orientation (v/h): ')).lower()  # default orientation is horizontal
                    direction = 0 if 'v' in orientation else 1  # 0 = vertical, 1 = horizontal(default)
                    max_size = 10-col if direction else 10-row  # calculate max size of ship based on location
                    size = validate_input(f'Ship size (max {max_size}): ')  # max ship-size at this location, orientation

                    if self.board.check_ship_placement(row, col, size, direction):
                        self.board.place_ship(row, col, size, direction)
                        ship_in_fleet = Ship(size)  # make Ship object
                        ship_in_fleet.add_to_fleet(row, col, direction)  # assign co-ordinates
                        self.fleet.append(ship_in_fleet)  # add ship to fleet
                        flag = False
                    else:
                        print('Ships overlapping, try again.')

                    self.board.board_plot()

                except ValueError:
                    print('Invalid input, try again.\n')

    # Checks status of a ship in the fleet

    def register_hit(self, row, col):
        for ship_in_fleet in self.fleet:
            if (row, col) in ship_in_fleet.coordinates:
                ship_in_fleet.coordinates.remove((row, col))
                if ship_in_fleet.check_status():
                    print(f'\x1b[30m\x1b[46mShip destroyed!\x1b[0m\n')
                    self.fleet.remove(ship_in_fleet)

    # Missile attack, check if it hits a battleship

    def attack(self):
        try:
            row = validate_input('Fire at (row): ')
            col = validate_input('Fire at (col): ')

            if row in range(10) and col in range(10):
                if self.board[row, col] == u"\u2588":  # check if solid square to represent ship
                    self.board[row, col] = u"\u259A"  # place checker square to represent hit
                    print('\033[4m\x1b[31mMissile hit a battleship!\033[0m\x1b[0m\n')
                    self.register_hit(row, col)
                else:
                    print('\033[4m\x1b[33mMissed the target!\033[0m\x1b[0m\n')

            else:
                print('Coordinates out of range, try again.\n')
                self.attack()

        except ValueError:
            print('Invalid input, try again.\n')
            self.attack()
        self.board.board_plot()
