import nltk
nltk.download("punkt")

import nltk.corpus
nltk.download("stopwords")

import string


with open("prestuplenie-i-nakazanie.txt", mode="r") as file:
    txt = file.read()

txt = txt.replace("\n", " ")

txt = txt.replace("-", " ")

for i in range(999, -1, -1):
    txt = txt.replace(str(i), " ")


sents = nltk.sent_tokenize(txt, language="russian")

wrds = []


for num, sent in enumerate(sents):
    sents[num] = sent.translate(str.maketrans('', '', string.punctuation))
    sents[num] = sents[num].lower()
    sents[num] = nltk.word_tokenize(sents[num], language="russian")


wrds_mn = 1000
wrds_mx = 0

for num, sent in enumerate(sents):
    if len(sent) > wrds_mx:
        wrds_mx = len(sent)

for num, sent in enumerate(sents):
    if len(sent) < wrds_mn:
        wrds_mn = len(sent)

print("Мин", wrds_mn)

for num, sent in enumerate(sents):
    if len(sent) == wrds_mn:
        print(sent)

print("Макс", wrds_mx)

for num, sent in enumerate(sents):
    if len(sent) == wrds_mx:
        print(sent)


for num, sent in enumerate(sents):
    for num_0, wrd in enumerate(sent):
        wrds.append(wrd)

wrds_n_sw = [word for word in wrds if word not in nltk.corpus.stopwords.words('russian')]

print(nltk.FreqDist(wrds).most_common(10))
print(nltk.FreqDist(wrds_n_sw).most_common(20))
