# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 07:14:59 2021

@author: Kovid
"""

from player import Player, validate_input
from time import time


def play():
    p1 = Player(validate_input('Enter the number of ships you want to place on board: '))  # Select number of ships to be placed on board
    p1.make_fleet()

    missiles = (validate_input('Enter the number of missiles you want to fire: '))  # Input the number of missiles to be fired
    counter = 1
    while p1.fleet and counter <= missiles:  # Play till not all ships are destroyed
        p1.attack()
        counter += 1

    if not p1.fleet:
        print('\033[4m\x1b[31mPlayer has lost!\033[0m\x1b[0m')  # No ships left on board, player lost
    else:
        print(f'\033[4m\x1b[32mPlayer won! {len(p1.fleet)} ship(s) survived!\033[0m\x1b[0m')  # Player won


if __name__ == '__main__':
    start_main = time()
    play()
    print(f'Run time: {round((time() - start_main) / 60, 2)} mins')
