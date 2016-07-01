#! /usr/bin/python
# -*- coding: utf-8 -*-

from game.game import Game
from game.dictionary import Dictionary 
from timer import Timer

import sys


if sys.argv[1]:
  size = int(sys.argv[1])


def group(lst, n):
  for i in range(0, len(lst), n):
    val = lst[i:i+n]
    if len(val) == n:
      yield tuple(val)

game = Game.random(size, Dictionary.fromfile('dic/en'))
print game.__str__().encode('utf-8')
print ' ' + '= '*len(game.state)
print

with Timer() as t:
  s = set(game.solve())

count = len(s)
solution = group(list(s), 6)

print '\n'.join(['\t\t'.join(g) for g in solution])
print
print 'Found %s solutions in %.03f sec.' % (count, t.interval)
print

