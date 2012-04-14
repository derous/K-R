import math, collections

class Trigram:

    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third

    def __hash__(self):
        return hash((self.first, self.second, self.third))

    def print_self(self):
        print self.first, self.second, self.third

    def __str__( self ):
        return str(self.first + " " + self.second + " " + self.third)

    def __eq__(self, other):
        return (self.first, self.second, self.third) == (other.first, other.second, other.third)

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

class CustomLanguageModel:

    bigrams = {}
    trigrams = {}

    def __init__(self, corpus):
        self.unigramCounts = collections.defaultdict(lambda: 0)
        self.total = 0
        self.train(corpus)
        #self.bigrams = {}

    def train(self, corpus):

        for sentence in corpus.corpus:
            word_index = 0
            while word_index < len(sentence.data) - 2:
                tr = Trigram(
                        sentence.data[word_index].word,
                        sentence.data[word_index + 1].word,
                        sentence.data[word_index + 2].word
                )
                if tr in self.trigrams:
                    self.trigrams[tr] += 1
                else:
                    self.bigrams[tr] = 1
                word_index += 1

        ######################

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

        ######################

        for sentence in corpus.corpus:
            for datum in sentence.data:
                token = datum.word
                self.unigramCounts[token] = self.unigramCounts[token] + 1
                self.total += 1

    def score(self, sentence):
        score = 0.0
        local_bigrams = []
        local_trigrams = []
        word_index = 0

        l = len(self.unigramCounts)

        while word_index < len(sentence) - 2:
            tr = Trigram(sentence[word_index], sentence[word_index + 1], sentence[word_index + 2])
            local_trigrams.append(tr)
            word_index += 1

            if tr in self.trigrams:

                count_tr = self.trigrams[tr]
                score += math.log(count_tr)

            else:
                b = Bigram(tr.first, tr.second)
                if b in self.bigrams:
                    count_tr = self.bigrams[b] * 0.4
                    score += math.log(count_tr)
                else:
                    count_tr = self.unigramCounts[tr.first] * (0.4 ** 2)
                    if count_tr == 0:
                        score += math.log(0.4 ** 2)
                        score -= math.log(self.total+l)
                    else:
                        score += math.log(count_tr)

        return score
