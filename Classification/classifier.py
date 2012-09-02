__author__ = 'Oleksandr'
import collections
import json
import math

class Classifier:
    def __init__(self, learnt_data):

        if learnt_data is not None:
            self.__load_learnt_data(learnt_data)

        self.genres = {}
        self.vocabulary = {}

    def __load_learnt_data(self, path):
        pass

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

    def classify(self, words):
        result = {}
        for g in self.genres:
            result[g] = 0
        #print result
        print len(self.vocabulary)
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


    def remember(self, name):
        g = json.dumps(self.genres)
        v = json.dumps(self.vocabulary)
        print g, v