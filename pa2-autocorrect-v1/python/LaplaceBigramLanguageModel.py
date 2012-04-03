import math, collections

class Bigram:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __hash__(self):
        return hash((self.first, self.second))

    def print_self(self):
        print self.first, self.second

    def __str__( self ):
        return str(self.first + " " + self.second)

    def __eq__(self, other):
        return (self.first, self.second) == (other.first, other.second)

class LaplaceBigramLanguageModel:

    bigrams = {}

    def __init__(self, corpus):
        self.unigramCounts = collections.defaultdict(lambda: 0)
        self.total = 0
        self.train(corpus)
        #self.bigrams = {}

    def train(self, corpus):
        for sentence in corpus.corpus:
            word_index = 0
            while word_index < len(sentence.data) - 1:
                b = Bigram(sentence.data[word_index].word, sentence.data[word_index + 1].word)
                if b in self.bigrams:
                    self.bigrams[b] += 1
                else:
                    self.bigrams[b] = 1
                word_index += 1
        #print self.bigrams

        for sentence in corpus.corpus:
            for datum in sentence.data:
                token = datum.word
                self.unigramCounts[token] = self.unigramCounts[token] + 1
                self.total += 1

    def score(self, sentence):
        score = 0.0
        local_bigrams = []
        word_index = 0

        l = len(self.unigramCounts)

        while word_index < len(sentence) - 1:
            b = Bigram(sentence[word_index], sentence[word_index + 1])
            local_bigrams.append(b)
            word_index += 1

            if b in self.bigrams:

                count_b = self.bigrams[b] + 1
                score += math.log(count_b)
                count_u = self.unigramCounts[b.first] + l
                score -= math.log(count_u)
                #print score
            else:
                count_b = 1
                score += math.log(count_b)
                if b.first in self.unigramCounts:
                    count_u = self.unigramCounts[b.first] + l
                else:
                    count_u = l
                score -= math.log(count_u)

        return score
