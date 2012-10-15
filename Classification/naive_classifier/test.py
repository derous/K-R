__author__ = 'Oleksandr Korobov'
import os
import re
import string
import sys
from classifier import  Classifier
from measurement import MeasureClassifier

classify = Classifier()

def process_genres(path):
    genres = os.listdir(path)
    print "Found genres:", genres
    for genre in genres:
        files = os.listdir(os.path.join(path, genre))
        #print files
        for file in files:
            words = classify.do_pre_processing(open(os.path.join(path, genre, file)).read().lower())
            classify.learn(genre, words)


import argparse

parser = argparse.ArgumentParser(description='Genre classifier')
parser.add_argument('--path', help='Folder to load genres learning data from')

args = parser.parse_args()
path =  args.path


if not classify.is_already_trained():
    if path is None:
        print """    Please specify root with genres folder"""
    else:
        process_genres(path)
    print classify.genres
else:
    print 'using loaded data'

test_text = open('../test_data/test_fan.txt').read()
#test_text = 'he has kill her. she was in love'
#test_text = 'it was the best trip in my life. a lot of new countries apes parrots following'

print classify.document_class(test_text.lower())

classify.remember()

# measurement script
evaluate_data_path = path + '_measure'
print evaluate_data_path
measure = MeasureClassifier(evaluate_data_path, classify)
measure.evaluate()
