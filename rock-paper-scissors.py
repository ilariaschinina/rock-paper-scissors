#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


'''Computer Player that chooses its move at random.'''
class RandomPlayer(Player):
    def move(self):
        move = random.choice(moves)
        return move


'''HumanPlayer whose move method asks the human user what move to make.'''
class HumanPlayer(Player):
    def move(self):
        move = input("Rock, paper, scissors? > ")
        return move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
    
    '''2 Update the Game class so that it displays the score of each round, 
    and keeps score for both players. You can use the provided beats function, 
    which tells whether one move beats another one.
    Make sure to handle ties — when both players make the same move!'''

if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()