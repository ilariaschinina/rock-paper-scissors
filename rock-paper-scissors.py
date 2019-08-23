#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
moves = ['rock', 'paper', 'scissors']


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


class Player:
    '''The Player class is the parent class for all of the Players
    in this game'''
    score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    '''Computer Player that chooses its move at random.'''
    def move(self):
        move = random.choice(moves)
        return move


class HumanPlayer(Player):
    '''HumanPlayer is played by the user'''
    def move(self):
        move = valid_input("Rock, paper, scissors? > ")
        return move


class ReflectPlayer(Player):
    '''ReflectPlayer remembers what move the opponent played last round,
    and plays that move this round.'''

    def __init__(self):
        self.opponent_move = 'rock'

    def learn(self, my_move, their_move):
        self.opponent_move = their_move

    def move(self):
        move = self.opponent_move
        return move


class CyclePlayer(Player):
    '''CyclePlayer remembers what move it played last round,
    and cycles through the different moves.'''

    def __init__(self):
        self.last_move = None

    def learn(self, my_move, their_move):
        self.last_move = my_move

    def move(self):
        if self.last_move is None:
            move = random.choice(moves)
            return move
        elif self.last_move == moves[2]:
            move = moves[0]
            return move
        else:
            index = moves.index(self.last_move)
            index += 1
            move = moves[index]
            return move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        while True:
            move1 = self.p1.move()
            move2 = self.p2.move()
            print(f"Player A played {move1}\nPlayer B played {move2}")
            if beats(move1, move2):
                print("Player A wins")
                self.p1.score += 1
                break
            elif move1 == move2:
                print("Draw... Replay this round")
                continue
            else:
                print("Player B wins")
                self.p2.score += 1
                break
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!\n")
        for round in range(3):
            print(f"Round {round+1}:")
            self.play_round()
            print("SCORE: Player A: {}\tPlayer B: {}\n"
                  .format(self.p1.score, self.p2.score))
        if self.p1.score > self.p2.score:
            print("***PLAYER A is the WINNER***")
        else:
            print("***PLAYER B is the WINNER***")
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
