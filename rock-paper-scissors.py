#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    score = 0
    
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(move1, move2):
    ''' Returns True if player1 wins this round, False otherwise'''
    return ((move1 == 'rock' and move2 == 'scissors') or
            (move1 == 'scissors' and move2 == 'paper') or
            (move1 == 'paper' and move2 == 'rock'))


def valid_input(prompt):
    '''User input validation'''
    while True:
        response = input(prompt).lower()
        for move in moves:
            if move in response:
                return response



class RandomPlayer(Player):
    '''Computer Player that chooses its move at random.'''
    def move(self):
        move = random.choice(moves)
        return move



class HumanPlayer(Player):
    '''HumanPlayer whose move method asks the human user what move to make.'''
    def move(self):
        move = valid_input("Rock, paper, scissors? > ")
        return move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        while True:
            move1 = self.p1.move()
            move2 = self.p2.move()
            print(f"Player 1: {move1}\tPlayer 2: {move2}")
            if beats(move1, move2):
                print("Player 1 wins")
                self.p1.score +=1
                break
            elif move1 == move2:
                print("Draw... Replay this round")
                continue
            else:
                print("Player 2 wins")
                self.p2.score +=1
                break
            self.p1.learn(move1, move2)
            self.p2.learn(move2, move1)


    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
            print(f"Player 1: {self.p1.score}\tPlayer 2: {self.p2.score}\n")
        if self.p1.score > self.p2.score:
            print("PLAYER 1 is the WINNER!!! ")
        else:
            print("PLAYER 2 is the WINNER!!! ")
        print("Game over!")
    
    '''2 Update the Game class so that it displays the score of each round, 
    and keeps score for both players. You can use the provided beats function, 
    which tells whether one move beats another one.
    Make sure to handle ties — when both players make the same move!'''



if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()

