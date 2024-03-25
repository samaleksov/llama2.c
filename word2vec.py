import os
from gensim.models import Word2Vec

sentences = []

for a, b, fileList in os.walk('text'):
    for file in fileList:
       with open('text/' + file, encoding='utf8') as f:
           txt = str.split(f.read().replace('\n', ''), '.')
           for s in txt:
               words = []
               for w in s.split():
                  if (len(w.strip()) > 0):
                      words.append(w.strip().lower())
               sentences.append(words)

train_sentences = list(sentences)

model = Word2Vec(sentences=train_sentences, 
                 vector_size=100,
                 window=100,
                 workers=4)

print(len(model.wv))
print(model.wv.index_to_key[:100])

embedding = model.wv['марко']

print(model.wv.most_similar(positive=[embedding], topn=10)) 
