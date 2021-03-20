# Battleship-Python
Battleship game using OO Python

# Battleship Game Simulator

Back end of the battleship simulator
It's a single player game where you decide the number of ships, attacks and attack co-ordinates on a 10x10 board

## Getting Started
These instructions will get you a copy of the game up and running on your local machine for testing purposes.

### Prerequisites
All pre-requisites are met in standard library module (Python 3.7)

##### Dependencies
There are no dependencies for this game

## Running the app

```
path_to_source_code > python3 gameplay.py
```

## Playing the game
It will first ask how many ships you want to place on the board, then the co-ordinates, size and orientation of each ship.

```
Enter the number of ships you want to place on board: 3
Place your ship number 1 at 
Place ship at (row): 2
Place ship at (col): 2
Orientation (v/h): v
Ship size (max 8): 7

```
After doing so for the number of ships specified, enter the number of missiles and attack co-ordinates
```
Enter the number of missiles you want to fire: 3
Fire at (row): 2
Fire at (col): 3
```
If the missile makes contact with a ship, below message will be prompted
```
Missile hit a battleship!
```
else, in case of a miss
```
Missed the target!
```

If the missiles are unable to sink all the ships, a message will be prompted
```
Player won! 1 ship(s) survived!
```
else if all ships are destroyed
```
Player has lost!
```
## Authors
|Name | Email|
| --- | ---- |
| Kovid Sharma | kovid5293@gmail.com | 
