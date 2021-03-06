#!/usr/bin/env python3

# Pielang
# Public domain

import sys, traceback
import re

def chop(thestring, ending):
  if thestring.startswith(ending):
    return thestring[len(ending):]
  return thestring

def rchop(thestring, ending):
  if thestring.endswith(ending):
    return thestring[:-len(ending)]
  return thestring

replacement_table = {"a": "ao",
                     "b": "c",
                     "c": "va",
                     "d": "t",
                     "e": "i",
                     "f": "g",
                     "g": "h",
                     "h": "y",
                     "i": "e",
                     "j": "k",
                     "k": "li",
                     "l": "p",
                     "m": "n",
                     "n": "m",
                     "o": "a",
                     "p": "q",
                     "q": "x",
                     "r": "sh",
                     "s": "ez",
                     "t": "d",
                     "u": "u",
                     "v": "w",
                     "w": "r",
                     "x": "j",
                     "y": "ie",
                     "z": "f"}

doubleReplace = {"hm": "hem",
                 "aao": "a",
                 "iee": "ie'e",
                 "ieau": "yao",
                 "hh": "h'h",
                 "tsh": "tash",
                 "csh": "cash",
                 "hup": "hurp",
                 "aomt": "ont",
                 "ryao": "rao",
                 "aoie": "aie"}

def decode(string):
    nstring = string.split()
    brf = []
    for string in nstring:
        lstring = list(string)
        for index in range(0, len(lstring)):
            char = lstring[index]
            try: char2 = lstring[index-1]
            except: char2 = ""
            else:
                if char2 != "e":
                    char2 = ""
            if char in replacement_table.keys():
                lstring[index] = replacement_table[char].replace(char2, "")
            elif char.lower() in replacement_table.keys():
                lstring[index] = replacement_table[char.lower()].replace(char2, "").title()
        lstring = "".join(lstring)
        for key in doubleReplace.keys():
            lstring = lstring.replace(key, doubleReplace[key])
            for k in ("title", "upper"):
                lstring = lstring.replace(eval("\"%s\".%s()" % (key, k)), eval("\"%s\".%s()" % (doubleReplace[key], k)))
        if lstring.endswith("i"):
            lstring += "r"
        elif lstring.endswith("I"):
            lstring += "R"
        if lstring == "E":
            lstring = "Nie"
        brf.append(lstring)
    return " ".join(brf)

def main(argv=[]):
    x = " ".join(argv)
    if len(x) == 0:
        x = input("Enter string here: ")
    print(decode(x))

if __name__ == "__main__":
    main(sys.argv[1::])
