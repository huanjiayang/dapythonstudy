'''
Created on 12 May 2017

@author: huanjiayang
'''
from Carbon.Sound import freqCmd

#Question:
#Write a program to compute the frequency of the phrase from the input. The output should output after sorting the key alphanumerically.

def getAlphabet():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = alphabet + alphabet.upper()
    alphabet += "0123456789"
    alphabet += " "
    return alphabet


def trimPhraseWithAlpa(phrase):
    alphabet = getAlphabet()
    for character in phrase:
        if character not in alphabet:
            phrase = phrase.replace(character,"")
    return phrase


def splitPhrase(phrase):
    words = phrase.split();
    return words


def countWordFreq(words):
    freqs = {}
    for word in words:
        if freqs.get(word):
            freqs[word] = freqs[word] + 1
        else:
            freqs[word] = 1
    return freqs


def countWord(phrase):
    trimmed = trimPhraseWithAlpa(phrase)
    splitted = splitPhrase(trimmed)
    return countWordFreq(splitted)


def printDictSorted(f):
    for word in sorted(f, key=str.lower):
        print(word,":",f[word])

printDictSorted(countWord("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."))