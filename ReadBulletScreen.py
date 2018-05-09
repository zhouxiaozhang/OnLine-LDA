# -*- coding: utf-8 -*-
import re
import jieba
import jieba.posseg as pseg
import uniout
import copy

try:
    import cPickle as pickle
except ImportError:
    import pickle
class BulletScreen(object):
    def __init__(self):
        self.stop_words= set([
                    " ","the","of","is","and","to","in","that","we","for",\
                    "an","are","by","be","as","on","with","can","if","from","which","you",
                    "it","this","then","at","have","all","not","one","has","or","that","什么","姐姐","一个"
                    ])


    def load_stop_words(self,file="data/metadata/stopWords.txt"):
        f = open(file)
        content = f.read().decode('utf-8')
        words = content.split('\n')
        for w in words:
            self.stop_words.add(w.strip())


    def read(self):

        f = open("data/1993410.txt", "r")
        #max time
        timelength = 5640
        #f = open("data/2152134.txt", "r")
        # self.timelength = 12306

        tempLine=[]
        jieba.load_userdict("data/metadata/user_dict.txt")
        for lineNo,line in enumerate(f.readlines()):
            pattern=re.compile("^<d p=\"(.+)\">(.+)</d>")
            m=pattern.match(line)
            if m:
                temp={"time":int(float(m.group(1).split(',')[0])), \
                                   "text":[word  for word,flag in pseg.cut(m.group(2))  \
                                           if word not in self.stop_words and flag not in \
                                           ["m","w","g","c","o","p","z","q","un","e","r","x","d","t","h","k","y","u","s","uj","ul","r","eng"] ],
                                   "lineno":lineNo+1}

                if len(temp["text"])>3:
                    tempLine.append(temp)

        lines=sorted(tempLine, key= lambda e:(e.__getitem__('time')))
        print  "video comment size: %d " % len(lines)
        return lines,timelength



    def run(self):
        self.load_stop_words()
        return self.read()

if __name__=="__main__":

    print BulletScreen().run()




