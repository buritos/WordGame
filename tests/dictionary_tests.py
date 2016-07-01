# -*- coding: utf-8 -*-

from nose.tools import *
from game.dictionary import Dictionary

def setup():
  pass

def teardown():
  pass


def test_fromfile():
  d = Dictionary.fromfile('dic/en')
  assert_equal(d.search('dogs'), {
    'dogstone', 'dogsleep', 'dogshore',
    'dogskin', 'dogship', 'dogs'
  })

def test_search():
  d = Dictionary(['cat','dog','dogs','con', 'top', 'kit'])
  assert_equal(d.search('c'), {'cat', 'con'})
  assert_equal(d.search('cat'), {'cat'})
  assert_equal(d.search('dog'), {'dog', 'dogs'})
