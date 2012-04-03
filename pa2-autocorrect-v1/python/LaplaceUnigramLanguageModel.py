import math, collections

class LaplaceUnigramLanguageModel:

    def __init__(self, corpus):
        self.unigramCounts = collections.defaultdict(lambda: 0)
        self.total = 0
        self.train(corpus)

    def train(self, corpus):
        """Takes a HolbrookCorpus corpus, does whatever training is needed."""
        for sentence in corpus.corpus:
            for datum in sentence.data:
                token = datum.word
                self.unigramCounts[token] = self.unigramCounts[token] + 1
                self.total += 1

    def score(self, sentence):
        """Takes a list of strings, returns a score of that sentence."""
        score = 0.0
        l = len(self.unigramCounts)

        for token in sentence:
            count = self.unigramCounts[token]
            if count > 0:
                score += math.log(count+1)
                score -= math.log(self.total+l)
            else:
                score += math.log(1)
                score -= math.log(self.total+l)

        return score
