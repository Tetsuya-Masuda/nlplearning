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

def nps_chat_example():
    from nltk.corpus import nps_chat
    chatroom = nps_chat.posts('10-19-20s_706posts.xml')
    print(chatroom[123])

def brown_corpus_example():
    '''ブラウン大学で作成され,100万語の英語からなる初の電子コーパス'''
    from nltk.corpus import brown
    print(brown.categories())
    print(brown.words(categories='news'))
    print(brown.words(fileids=['cg22']))
    print(brown.sents(categories=['news','editorial','reviews']))
    #法定助詞の使われ方が、各ジャンルにより違う
    news_text = brown.words(categories='news')
    fdist = nltk.FreqDist([w.lower() for w in news_text])
    modals = ['can','could','may','might','must','will']
    for m in modals:
        print (m + ':' , fdist[m],)

    cfd = nltk.ConditionalFreqDist(
        (genre,word)
        for genre in brown.categories()
        for word in brown.words(categories=genre))
    genres = ['news','religion','hobbies','science_fiction','romance','humor']
    modals = ['can','could','may','might','must','will']
    cfd.tabulate(conditions=genres,samples=modals)
brown_corpus_example()