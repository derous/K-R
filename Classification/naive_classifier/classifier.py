__author__ = 'Oleksandr Korobov'

import string
import sys

import json
import re
import math

class Classifier:
    def __init__(self):

        self.genres = {}
        self.vocabulary = {}
        self.__load_learnt_data()

    def learn(self, genre, words):
        if genre not in self.genres:
            self.genres[genre] = 0
        self.genres[genre] += len(words)

        for word in words:
            if not word in self.vocabulary:
                self.vocabulary[word] = {}
            if not genre in self.vocabulary[word]:
                self.vocabulary[word][genre] = 1
            else:
                self.vocabulary[word][genre] += 1

    def classify(self, evaluated_text):
        words = self.do_pre_processing(evaluated_text)
        result = {}
        for g in self.genres:
            result[g] = 0
        for word in words:
            if word in self.vocabulary:
                for genre in self.genres:
                    if genre in self.vocabulary[word]:
                        k = (self.vocabulary[word][genre] + 1.0) / (self.genres[genre] + len(self.vocabulary))
                        result[genre] += math.log(k)
                    else:
                        result[genre] += math.log(1.0 / (self.genres[genre] + len(self.vocabulary)))
            else:
                for genre in self.genres:
                    result[genre] += math.log(1.0 / (self.genres[genre] + len(self.vocabulary)))

        sigma = 0

        for g in self.genres:
            sigma += self.genres[g]

        for g in self.genres:
            result[g] += math.log(self.genres[g]/float(sigma))
        # print result
        return result


    def remember(self):
        g = json.dumps(self.genres)
        v = json.dumps(self.vocabulary)
        #print g, v
        gnr = open('./genre.dat', 'w')
        vcb = open('./vocabulary.dat', 'w')
        #print os.system('ls')
        gnr.write(g)
        vcb.write(v)
        gnr.close()
        vcb.close()
        print "saved..."

    def __load_learnt_data(self):
        try:
            g = open('./genre.dat', 'r').read()
            v = open('./vocabulary.dat', 'r').read()
            self.genres = json.loads(g)
            self.vocabulary = json.loads(v)
        except:
            pass
        finally:
            pass

    def is_already_trained(self):
        return len(self.genres) > 0 and len(self.vocabulary) > 0

    def isAscii(self, s):
        for c in s:
            if c not in string.ascii_letters:
                return False
        return True

    def do_pre_processing(self, text):
        return filter(
            lambda w: 20 > len(w) > 1 and self.isAscii(w), re.split(
                '[\n!?/\\\(\).,` :;\-\[\]\'_"0-9@#$%\^&\*\t]' , text))

    def document_class(self, doc):
        genres_values = self.classify(doc)
        decision_value = -sys.float_info.max
        decision = ''

        for r in genres_values:
            if genres_values[r] > decision_value:
                decision_value = genres_values[r]
                decision = str(r)
        return decision