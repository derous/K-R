import os
import re
import string
import sys
from classifier import  Classifier
__author__ = 'Oleksandr'

classify = Classifier()

def isAscii(s):
    for c in s:
        if c not in string.ascii_letters:
            return False
    return True

def do_split(text):
    return filter(
        lambda w: len(w)>1 and isAscii(w), re.split(
        '[\n!?/\\\(\).,` :;\-\[\]\'_"0-9@#$%\^&\*\t]' , text))

def process_genres(path):
    genres = os.listdir(path)
    print "Found genres:", genres
    for genre in genres:
        files = os.listdir(os.path.join(path, genre))
        #print files
        for file in files:
            words = do_split(open(os.path.join(path, genre, file)).read().lower())
            classify.learn(genre, words)


import argparse

parser = argparse.ArgumentParser(description='Genre classifier')
parser.add_argument('--path', help='Folder to load genres learning data from')

args = parser.parse_args()
path =  args.path


if not classify.alreadyTrained():
    if path is None:
        print """    Please specify root with genres folder"""
    else:
        process_genres(path)
    print classify.genres
else:
    print 'using loaded data'

test_text = open('tst_cur.txt').read()

#print test_text

result = classify.classify(do_split(test_text.lower()))

decision_value = -sys.float_info.max
decision = ''

for r in result:
    if result[r] > decision_value:
        decision_value = result[r]
        decision = str(r)

print decision, decision_value

for genre in result:
    result[genre] -= decision_value

print result

classify.remember()