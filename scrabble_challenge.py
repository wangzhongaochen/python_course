#!/usr/bin/python
#-*- coding: UTF-8 -*-
import sys
import argparse
from collections import defaultdict

#Read the sowpods word file.
def construct_word_list():
    word_list = []
    with open('sowpods.txt','r') as f:
        for word in f:
            word_list.append(word.strip().lower())
    return word_list

"""
Find all words from the word list that are made of letters 
that are a subset of the rack letters.
"""
def find_valid_words(words_list,word_rack):
    words_valid_list = []
    for word in words_list:
        word_rack_b = word_rack
        flag = True
        for c in word:
            if not c in word_rack_b:
                flag = False
                break
            else:
                word_find_index = word_rack_b.index(c)
                word_rack_b = word_rack_b[:word_find_index]+word_rack_b[word_find_index+1:]
        if flag:
            words_valid_list.append(word)
    return words_valid_list

#Determine the Scrabble scores for each valid word.
def get_score(*args):
    scrabble_scores = defaultdict(int) 
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
              "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
              "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
              "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
              "x": 8, "z": 10}
    for word in args:
        for c in word:
            scrabble_scores[word] += scores[c]
    return scrabble_scores

def main():
    if len(sys.argv) == 1:
        print "Usage: scrabble_challenge.py [-h] [RACK]"
        sys.exit(2)
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('rack',action="store")

    word_rack = parser.parse_args().rack.lower()
    words_list = construct_word_list()
    word_valid_list = find_valid_words(words_list,word_rack)
    scrabble_scores = get_score(*word_valid_list)
    result = sorted(zip(scrabble_scores.values(),scrabble_scores.keys()),reverse=True)
    for val,key in result:
        print val,',',key

if __name__ == '__main__':
    main()

