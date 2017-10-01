import nltk
from nltk.corpus import gutenberg

gutenberg.fileids()
emma = gutenberg.words('austen-emma.txt')


def gutenberg_file_info():
    for fileid in gutenberg.fileids():
        num_chars = len(gutenberg.raw(fileid))
        num_words = len(gutenberg.words(fileid))
        num_sents = len(gutenberg.sents(fileid))
        num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
        print (int(num_chars/num_words), int(num_words / num_sents), int(num_words/num_vocab), fileid)

def gutenberg_macbeth_examle():
    macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
    print(macbeth_sentences)
    print(macbeth_sentences[1037])
    longest_len = max([len(s) for s in macbeth_sentences])
    print([s for s in macbeth_sentences if len(s) == longest_len])

def webtext_example():
    from nltk.corpus import webtext
    for fileid in webtext.fileids():
        print(fileid,webtext.raw(fileid)[:65],'...')

from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
print(chatroom[123])
