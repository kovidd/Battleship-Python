# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 06:17:31 2021

@author: Kovid
"""


class Ship:
    def __init__(self, size):
        self.size = size
        self.coordinates = []

    def add_to_fleet(self, row, col, orientation):
        for i in range(self.size):
            self.coordinates.append((row, col))
            if orientation:  # True = horizontal
                col += 1
            else:
                row += 1

    def check_status(self):
        if not self.coordinates:
            return True
        else:
            return False
