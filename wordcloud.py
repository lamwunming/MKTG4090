
# coding: utf-8

# In[ ]:


import pandas as pd 

df2013 = pd.read_csv('/Users/Lwmformula/Desktop/2013_.csv')
comment2013 = df2013['comment']

df2014 = pd.read_csv('/Users/Lwmformula/Desktop/2014_.csv')
comment2014 = df2014['comment']

df2015 = pd.read_csv('/Users/Lwmformula/Desktop/2015_.csv')
comment2015 = df2015['comment']

df2016 = pd.read_csv('/Users/Lwmformula/Desktop/2016_.csv')
comment2016 = df2016['comment']

df2017 = pd.read_csv('/Users/Lwmformula/Desktop/2017_.csv')
comment2017 = df2017['comment']


# In[ ]:


import re
import operator 
import json
from collections import Counter
from nltk.corpus import stopwords
import string
from string import digits
import nltk
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return ''

punctuation = list(string.punctuation)
numstring = ['one','two','three','four','five','six','seven','eight','nine','ten']
stop = stopwords.words('english') + punctuation + ['rt', 'via','@VictoriasSecret','secret',"victoria's",'i',
                                                   'vs','victoria',"i'm","#victoriassecret"] + numstring
#stop = stopwords.words('english') + punctuation + ['rt', 'via','@Aerie','secret',"aerie's",'i',
#                                                   'aerie',"i'm",'#aeriereal','#aerie'] + numstring
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>',
    r'(?:@[\w_]+)',
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',
    r'(?:(?:\d+,?)+(?:\.?\d+)?)',
    r"(?:[a-z][a-z'\-_]+[a-z])",
    r'(?:[\w_]+)',
    r'(?:\S)'
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
lemmatizer = WordNetLemmatizer()
 
def tokenizefunc(s):
    return tokens_re.findall(s)

def lemma(word):
    return lemmatizer.lemmatize(word, get_wordnet_pos(nltk.pos_tag([word])[0][1]))
 
def preprocess(s, lowercase=False):
    _tokens_ = []
    tokens = s.translate(None, digits)
    tokens = tokenizefunc(tokens)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    tokens_ = [term.lower() for term in tokens if term.lower() not in stop and not term.startswith(('@'))] 
    for i in tokens_:
        try:
            _tokens_.append(lemma(i))
        except:
            _tokens_.append(i)
    return _tokens_
    #return tokens_
tokenize2013 = map(lambda x: preprocess(x),comment2013)
tokenize2014 = map(lambda x: preprocess(x),comment2014)
tokenize2015 = map(lambda x: preprocess(x),comment2015)
tokenize2016 = map(lambda x: preprocess(x),comment2016)
tokenize2017 = map(lambda x: preprocess(x),comment2017)


# In[ ]:


count_all2013 = Counter()
for i in tokenize2013:
    count_all2013.update(i)
print '2013:'
print(count_all2013.most_common(100))
print ''

count_all2014 = Counter()
for i in tokenize2014:
    count_all2014.update(i)
print '2014:'
print(count_all2014.most_common(100))
print ''

count_all2015 = Counter()
for i in tokenize2015:
    count_all2015.update(i)
print '2015:'
print(count_all2015.most_common(100))
print ''

count_all2016 = Counter()
for i in tokenize2016:
    count_all2016.update(i)
print '2016:'
print(count_all2016.most_common(100))
print ''

count_all2017 = Counter()
for i in tokenize2017:
    count_all2017.update(i)
print '2017:'
print(count_all2017.most_common(100))
print ''


# In[ ]:


from collections import defaultdict
 
com2013 = defaultdict(lambda : defaultdict(int))
for ii in tokenize2013:
    for i in range(len(ii)-1):            
        for j in range(i+1, len(ii)):
            w1, w2 = sorted([ii[i], ii[j]])                
            if w1 != w2:
                com2013[w1][w2] += 1          
com_max2013 = []
for t1 in com2013:
    t1_max_terms = sorted(com2013[t1].items(), key=operator.itemgetter(1), reverse=True)[:5]
    for t2, t2_count in t1_max_terms:
        com_max2013.append(((t1, t2), t2_count))
# Get the most frequent co-occurrences
terms_max2013 = sorted(com_max2013, key=operator.itemgetter(1), reverse=True)
print '2013:'
print(terms_max2013[:50])
print ''

com2014 = defaultdict(lambda : defaultdict(int))
for ii in tokenize2014:
    for i in range(len(ii)-1):            
        for j in range(i+1, len(ii)):
            w1, w2 = sorted([ii[i], ii[j]])                
            if w1 != w2:
                com2014[w1][w2] += 1          
com_max2014 = []
for t1 in com2014:
    t1_max_terms = sorted(com2014[t1].items(), key=operator.itemgetter(1), reverse=True)[:5]
    for t2, t2_count in t1_max_terms:
        com_max2014.append(((t1, t2), t2_count))
# Get the most frequent co-occurrences
terms_max2014 = sorted(com_max2014, key=operator.itemgetter(1), reverse=True)
print '2014:'
print(terms_max2014[:50])
print ''

com2015 = defaultdict(lambda : defaultdict(int))
for ii in tokenize2015:
    for i in range(len(ii)-1):            
        for j in range(i+1, len(ii)):
            w1, w2 = sorted([ii[i], ii[j]])                
            if w1 != w2:
                com2015[w1][w2] += 1          
com_max2015 = []
for t1 in com2015:
    t1_max_terms = sorted(com2015[t1].items(), key=operator.itemgetter(1), reverse=True)[:5]
    for t2, t2_count in t1_max_terms:
        com_max2015.append(((t1, t2), t2_count))
# Get the most frequent co-occurrences
terms_max2015 = sorted(com_max2015, key=operator.itemgetter(1), reverse=True)
print '2015:'
print(terms_max2015[:50])
print ''

com2016 = defaultdict(lambda : defaultdict(int))
for ii in tokenize2016:
    for i in range(len(ii)-1):            
        for j in range(i+1, len(ii)):
            w1, w2 = sorted([ii[i], ii[j]])                
            if w1 != w2:
                com2016[w1][w2] += 1          
com_max2016 = []
for t1 in com2016:
    t1_max_terms = sorted(com2016[t1].items(), key=operator.itemgetter(1), reverse=True)[:5]
    for t2, t2_count in t1_max_terms:
        com_max2016.append(((t1, t2), t2_count))
# Get the most frequent co-occurrences
terms_max2016 = sorted(com_max2016, key=operator.itemgetter(1), reverse=True)
print '2016:'
print(terms_max2016[:50])
print ''

com2017 = defaultdict(lambda : defaultdict(int))
for ii in tokenize2017:
    for i in range(len(ii)-1):            
        for j in range(i+1, len(ii)):
            w1, w2 = sorted([ii[i], ii[j]])                
            if w1 != w2:
                com2017[w1][w2] += 1          
com_max2017 = []
for t1 in com2017:
    t1_max_terms = sorted(com2017[t1].items(), key=operator.itemgetter(1), reverse=True)[:5]
    for t2, t2_count in t1_max_terms:
        com_max2017.append(((t1, t2), t2_count))
# Get the most frequent co-occurrences
terms_max2017 = sorted(com_max2017, key=operator.itemgetter(1), reverse=True)
print '2017:'
print(terms_max2017[:50])
print ''   


# In[ ]:


cons2013 = [(i[0][0] + ' ' + i[0][1],i[1]) for i in terms_max2013]
cons2014 = [(i[0][0] + ' ' + i[0][1],i[1]) for i in terms_max2014]
cons2015 = [(i[0][0] + ' ' + i[0][1],i[1]) for i in terms_max2015]
cons2016 = [(i[0][0] + ' ' + i[0][1],i[1]) for i in terms_max2016]
cons2017 = [(i[0][0] + ' ' + i[0][1],i[1]) for i in terms_max2017]

cloud2013 = dict(count_all2013.most_common(1000) + cons2013)
cloud2014 = dict(count_all2014.most_common(1000) + cons2014)
cloud2015 = dict(count_all2015.most_common(1000) + cons2015)
cloud2016 = dict(count_all2016.most_common(1000) + cons2016)
cloud2017 = dict(count_all2017.most_common(1000) + cons2017)

print cloud2013


# In[ ]:


from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

alice_mask = np.array(Image.open("/Users/Lwmformula/Desktop/template.png"))

wordcloud = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
                      width=1500,height=1000).generate_from_frequencies(cloud2017)

# store to file
wordcloud.to_file("/Users/Lwmformula/Desktop/cloud2017.png")

