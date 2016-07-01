# -*- coding: utf-8 -*-

from nose.tools import *
from game.game import Game
from game.dictionary import Dictionary
from game.constants import alphabet

def setup():
  pass

def teardown():
  pass

def test_random():
  g = Game.random(3, None)
  assert_equal(len(g.state), 3)
  for s in g.state:
    assert_equal(len(s), 3)
    for c in s:
      assert_true(c in alphabet)

def test_solve():
  state = [['c', 'a', 't'],['d','o','g'],['p','i','n']]
  g = Game(state, Dictionary(['cat','dog','pin','con', 'top', 'kit']))
  solution = set([s for s in g.solve()])
  assert_equal(solution, {'cat','dog','pin','con', 'top'})
