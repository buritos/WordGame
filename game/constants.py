# -*- coding: utf-8 -*-

character_freq = {
  'e': 12,  't': 9, 'a': 8, 'o': 8,
  'i': 7,   'n': 7, 's': 6, 'r': 6,
  'h': 6,   'd': 4, 'l': 4, 'u': 3,
  'c': 3,   'm': 3, 'f': 2, 'y': 2,
  'w': 2,   'g': 2, 'p': 2, 'b': 2,
  'v': 1,   'k': 1, 'x': 1, 'q': 1,
  'j': 1,   'z': 1
}

alphabet = ''.join([c*character_freq[c] for c in character_freq]).decode('utf-8')
