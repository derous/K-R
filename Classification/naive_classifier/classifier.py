#!/usr/bin/python
# -*- coding: utf8 -*-


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

        stop_text = '''
        a’s, able, about, above, according, accordingly, across, actually, after, afterwards, again, against, ain’t,
        all, allow, allows, almost, alone, along, already, also, although, always, am, among, amongst, an, and,
        another, any, anybody, anyhow, anyone, anything, anyway, anyways, anywhere, apart, appear, appreciate,
        appropriate, are, aren’t, around, as, aside, ask, asking, associated, at, available, away, awfully, be, became,
        because, become, becomes, becoming, been, before, beforehand, behind, being, believe, below, beside, besides,
        best, better, between, beyond, both, brief, but, by, c’mon, c’s, came, can, can’t, cannot, cant, cause, causes,
        certain, certainly, changes, clearly, co, com, come, comes, concerning, consequently, consider, considering,
        contain, containing, contains, corresponding, could, couldn’t, course, currently, definitely, described,
        despite, did, didn’t, different, do, does, doesn’t, doing, don’t, done, down, downwards, during, each, edu, eg,
        eight, either, else, elsewhere, enough, entirely, especially, et, etc, even, ever, every, everybody, everyone,
        everything, everywhere, ex, exactly, example, except, far, few, fifth, first, five, followed, following,
        follows, for, former, formerly, forth, four, from, further, furthermore, get, gets, getting, given, gives, go,
        goes, going, gone, got, gotten, greetings, had, hadn’t, happens, hardly, has, hasn’t, have, haven’t, having,
        he, he’s, hello, help, hence, her, here, here’s, hereafter, hereby, herein, hereupon, hers, herself, hi, him,
        himself, his, hither, hopefully, how, howbeit, however, i’d, i’ll, i’m, i’ve, ie, if, ignored, immediate, in,
        inasmuch, inc, indeed, indicate, indicated, indicates, inner, insofar, instead, into, inward, is, isn’t, it,
        it’d, it’ll, it’s, its, itself, just, keep, keeps, kept, know, knows, known, last, lately, later, latter,
        latterly, least, less, lest, let, let’s, like, liked, likely, little, look, looking, looks, ltd, mainly, many,
        may, maybe, me, mean, meanwhile, merely, might, more, moreover, most, mostly, much, must, my, myself, name,
        namely, nd, near, nearly, necessary, need, needs, neither, never, nevertheless, new, next, nine, no, nobody,
        non, none, noone, nor, normally, not, nothing, novel, now, nowhere, obviously, of, off, often, oh, ok, okay,
        old, on, once, one, ones, only, onto, or, other, others, otherwise, ought, our, ours, ourselves, out, outside,
        over, overall, own, particular, particularly, per, perhaps, placed, please, plus, possible, presumably,
        probably, provides, que, quite, qv, rather, rd, re, really, reasonably, regarding, regardless, regards,
        relatively, respectively, right, said, same, saw, say, saying, says, second, secondly, see, seeing, seem,
        seemed, seeming, seems, seen, self, selves, sensible, sent, serious, seriously, seven, several, shall, she,
        should, shouldn’t, since, six, so, some, somebody, somehow, someone, something, sometime, sometimes, somewhat,
        somewhere, soon, sorry, specified, specify, specifying, still, sub, such, sup, sure, t’s, take, taken, tell,
        tends, th, than, thank, thanks, thanx, that, that’s, thats, the, their, theirs, them, themselves, then, thence,
        there, there’s, thereafter, thereby, therefore, therein, theres, thereupon, these, they, they’d, they’ll,
        they’re, they’ve, think, third, this, thorough, thoroughly, those, though, three, through, throughout, thru,
        thus, to, together, too, took, toward, towards, tried, tries, truly, try, trying, twice, two, un, under,
        unfortunately, unless, unlikely, until, unto, up, upon, us, use, used, useful, uses, using, usually, value,
        various, very, via, viz, vs, want, wants, was, wasn’t, way, we, we’d, we’ll, we’re, we’ve, welcome, well, went,
        were, weren’t, what, what’s, whatever, when, whence, whenever, where, where’s, whereafter, whereas, whereby,
        wherein, whereupon, wherever, whether, which, while, whither, who, who’s, whoever, whole, whom, whose, why,
        will, willing, wish, with, within, without, won’t, wonder, would, would, wouldn’t, yes, yet, you, you’d, you’ll,
        you’re, you’ve, your, yours, yourself, yourselves, zero
        '''
        self.stop_words = filter(
            lambda w: len(w)>1,
            re.split('[, \n\xe2\x80\x99s]' , stop_text))
        print self.stop_words
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
            lambda w: 20 > len(w) > 1 and self.isAscii(w) and not w in self.stop_words, re.split(
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