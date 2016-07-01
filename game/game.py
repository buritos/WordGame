# -*- coding: utf-8 -*-

from random import randint
import math

from constants import alphabet

class Game:

  @staticmethod
  def random(dim, dictionary):
    return Game(
      [[alphabet[randint(0,len(alphabet)-1)] for i in range(dim)] for i in range(dim)], 
      dictionary)


  def __init__(self, state, dictionary):
    self.index = [(i,z) for i in range(len(state)) for z in range(len(state))]
    self.state = state
    self.dictionary = dictionary


  def neighbors(self, x, y):
    f = lambda p: not (p[0] == x and p[1] == y) and math.sqrt((x-p[0])**2+(y-p[1])**2) <= 1.5
    return filter(f, self.index)

  def solve(self):
    for cell in self.index:
      for result in self.search(cell):
        yield result

  def search(self, cell):
    stack = [(cell, self.state[cell[0]][cell[1]])]
    while stack:
      (p, word) = stack.pop()
      for next in self.neighbors(p[0], p[1]):
        next_word = word + self.state[next[0]][next[1]]
        words = self.dictionary.search(next_word)
        if next_word in words:
          if len(words) > 1:
            stack.append((next, next_word))
          yield next_word
        elif words:
          stack.append((next, next_word))
  
  def __str__(self):
    return ' ' + '_ '*len(self.state) + '\n|'+'|\n|'.join(['|'.join(s) for s in self.state])+'|'
