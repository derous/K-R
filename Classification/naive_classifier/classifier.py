import os

__author__ = 'Oleksandr'
import collections
import json
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

    def classify(self, words):
        result = {}
        for g in self.genres:
            result[g] = 0
        #print result
        #print len(self.vocabulary)
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
            #print g
            #print v[0]
            self.genres = json.loads(g)
            self.vocabulary = json.loads(v)
        except:
            pass
        finally:
            pass
            #print self.genres
            #print self.vocabulary

    def alreadyTrained(self):
        return len(self.genres) > 0 and len(self.vocabulary) > 0