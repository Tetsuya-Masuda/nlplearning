def lexical_divesity(text):
    return len(text) / len(set(text))

def percentage(count,tatal):
    return 100 * count / total

sent1 = ['Call','me','Ishmael','.']
print(sent1)

print(lexical_divesity(sent1))

sent = ['word1','word2','word3','word4','word5','word6','word7','word8','word9','word10']
print(sent[0])
print(sent[9])

print(sent[5:8])
print(sent[5])

sent[0] = 'First'
sent[9] = 'Last'
print(len(sent))

sent[1:9] = ['Second', 'Third']
print(sent)
print(sent[9])


# 文字列数が15文字以上などを抽出する
# 文字列数ごとにdictを作り、各要素の頻出度合いを見る
