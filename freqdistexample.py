import nltk
import sys

saying = ['After','all','is','said','and','done','more','is','said','than','done']
tokens = set(saying)
tokens = sorted(tokens)
print(tokens[-2:])

sampleFilePath = 'sample.txt'
textfile = open(sampleFilePath,'r',encoding='utf-8')

raw = textfile.read()
tokens = nltk.word_tokenize(raw)
print(raw)
print(tokens)
print(len(tokens))

fd = nltk.FreqDist(tokens)
fd.plot(50)