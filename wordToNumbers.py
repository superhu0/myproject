#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Super Hu'

#手机的九宫格输入法中，输入数字的键位是可以和字母键位对应的。如“2”对应“ABC”，“9”对应“WXYZ”，现假设“1”和“0”为空字符，以此规则试设计一个程序，将单词用一串数字来进行表示。
#举例：
#输入：cat（不区分大小写）
#输出：228

def wordToNumber(word):
    alphabeta = {'a':2, 'b':2, 'c':2, 'd':3, 'e':3, 'f':3, 'g':4, 'h':4, 'i':4, 'j':5, 'k':5, 'l':5, 'm':6, 'n':6, 'o':6, 'p':7, 'q':7, 'r':7, 's':7, 't':8, 'u':8, 'v':8, 'w':9, 'x':9, 'y':9, 'z':9, ' ':0}
    word = word.lower().strip()
    num = 0
    for a in word:
        num = alphabeta[a] + num * 10
    return num

if __name__ == '__main__':
    word = input('Please input a word: ')
    result = wordToNumber(word)
    print(result)
