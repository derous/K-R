import os
import sys

__author__ = 'oleksandr'

class MeasureClassifier:

    def __init__(self, test_data_path, classifier):

        self.classifier = classifier
        self.test_data_path = test_data_path
        if not os.path.exists(test_data_path):
            print "couldn't find test data"
            return
        test_genres = os.listdir(test_data_path)

        self.test_data = {}

        for test_genre in test_genres:
            self.test_data[test_genre] = map(
                lambda name: os.path.normpath(test_data_path + '/' + test_genre + '/' + name),
                os.listdir(os.path.normpath(test_data_path + '/' + test_genre)))


    def evaluate(self):
        trues = 0
        falses = 0
        for test_genre in self.test_data:
            for doc in self.test_data[test_genre]:
                result = self.classifier.document_class(open(doc).read().lower()).upper()
                print result == test_genre.upper(), result, test_genre.upper()
                if result == test_genre.upper():
                    trues += 1
                else:
                    falses += 1
        print 'RESULT:', trues, falses, trues/float(trues+falses)