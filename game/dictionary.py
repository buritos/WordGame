# -*- coding: utf-8 -*-

import codecs

from bisect import bisect_left

class Dictionary:

  @staticmethod
  def fromfile(filename):
    return Dictionary([line.rstrip('\n') for line in codecs.open(filename, encoding='utf-8')])


  def __init__(self, words):
    self.words = words
    self.words.sort()


  def search(self, prefix):
    pos = bisect_left(self.words, prefix)
    results = set()
    while pos < len(self.words):
      currentWord = self.words[pos]
      if currentWord.startswith(prefix):
        results.add(currentWord)
        pos = pos+1
      else:
        break
    return results