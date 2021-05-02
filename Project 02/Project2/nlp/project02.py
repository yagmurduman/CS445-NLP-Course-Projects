import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import nltk
#nltk.download('stopwords')
#nltk.download('punkt')
import nltk.lm
from nltk.util import ngrams
from nltk.util import everygrams
from nltk.corpus import stopwords as stop_words
from nltk.lm import MLE
from nltk.lm import KneserNeyInterpolated
from nltk.tokenize import sent_tokenize, word_tokenize
import matplotlib
import matplotlib.pyplot as plt
from scipy import special
import numpy as np
import random
import seaborn as sns
from scipy.stats import zipf
from gensim.test.utils import common_texts
from gensim.utils import simple_preprocess
from gensim.models import Word2Vec
import math



def create_WordCloud (Docs, size, outputfile , mode, stopwords):

    if stopwords:
        stopwordlist = stop_words.words('turkish')
        stopwordlist.append("nin")
        stopwordlist.append("nın")
        stopwordlist.append("in")
        stopwordlist.append("ın")
        stopwordlist.append("ne")
        stopwordlist.append("na")
        stopwordlist.append("da")
        stopwordlist.append("bir")
    else:
        stopwordlist = None
    

    if mode =="TFIDF":
       vectorizer = TfidfVectorizer(stop_words=(stopwordlist))
       X = vectorizer.fit_transform(Docs)
       feature_names= vectorizer.get_feature_names()
       df = pd.DataFrame(X.toarray(), columns = feature_names)
       df=df.sum(axis = 0, skipna = False)
       wordfreqs= dict(df)
       wordcloud = WordCloud(width=(size*100),height=(size*100), background_color="white").generate_from_frequencies(wordfreqs)
       plt.imshow(wordcloud, interpolation='bilinear')
       plt.axis("off")  
       plt.savefig(outputfile)
       plt.show()
       


def create_ZiphsPlot(Docs,zips_outputfile):
  
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(Docs)
    feature_names= vectorizer.get_feature_names()
    df = pd.DataFrame(X.toarray(), columns = feature_names)
    df=df.sum(axis = 0, skipna = False)
    wordfreqs= dict(df)

    sorted_freqs = dict(sorted(wordfreqs.items(), key=lambda item: item[1])) 

    rank = []
    i= 1
    for i in range (1, len(sorted_freqs)+1):
        rank.append(i)
        i+= 1
    rank.reverse()

    freqslist = list(sorted_freqs.values())

    plt.loglog(rank, freqslist)
    plt.xlabel('frequency(f)', fontsize=16, fontweight='bold')
    plt.ylabel('rank(r)', fontsize=16, fontweight='bold')
    plt.grid(True)
    plt.savefig(zips_outputfile)
    plt.show()
    
    

def create_HeapsPlot(Docs,heaps_outputfile):
    
    alltext =""
    for text in Docs:
        for words in text:
            alltext += words
    
    tokens=nltk.wordpunct_tokenize(alltext)

    uniq = set()

    wordlist = []
    uniquelist = []
    for i, token in enumerate(tokens):
        uniq.add(token)
        wordlist.append(i)
        uniquelist.append(len(uniq))


    plt.plot(wordlist, uniquelist)   
    plt.xlabel('Word Count', fontsize=16, fontweight='bold')
    plt.ylabel('Unique Word Count', fontsize=16, fontweight='bold')
    plt.grid(True)
    plt.savefig(heaps_outputfile)
    plt.show() 


def create_LanguageModel(Docs,model_type,ngram):

    alltext =""
    for text in Docs:
        for words in text:
            alltext += words
    
    
    sent_tokens = nltk.sent_tokenize(alltext)
    tokenizedtext = []
    for token in sent_tokens:
        token = nltk.word_tokenize(token)
        tokenizedtext.append(token)
    
    if(model_type == 'MLE'):
        model = MLE(ngram)
        traintext, padded = nltk.lm.preprocessing.padded_everygram_pipeline(ngram, tokenizedtext)
        model.fit(traintext, padded)
        return model
    
    if(model_type == 'KneserNeyInterpolated'):
        model = KneserNeyInterpolated(ngram)
        traintext, padded = nltk.lm.preprocessing.padded_everygram_pipeline(ngram, tokenizedtext)
        model.fit(traintext, padded)
        return model
    

def generate_sentence(model,text):

    endlist =[]
    perplist =[]
    for i in range (0,5):
        i
        generated_word = [text]
        new_word =  model.generate(num_words=1, text_seed=generated_word)
        while(new_word != '</s>'):
            generated_word.append(new_word)
            new_word = model.generate(num_words=1, text_seed=generated_word)
        
        maxlen = model.order    

        everygram = list(everygrams(generated_word, max_len= maxlen))

        perp = model.perplexity(everygram)

        sentence = ""
        for word in generated_word:
            sentence += word
            sentence += " "

        endlist.append(sentence)
        perplist.append(perp)

        ind = perplist.index(min(perplist))

    
    return endlist[ind],perplist[ind]

def create_WordVectors(Docs,dimvec,model_type,winsize):
    
    tokenizedtext = []
    for doc in Docs:
        sent_tokens = sent_tokenize(doc)
        for token in sent_tokens:
            i = simple_preprocess(token)
            tokenizedtext.append(i)


    if (model_type == "cbow"):
        model = Word2Vec(sentences=tokenizedtext, size= dimvec, window= winsize, sg = 0)
        return model

    if (model_type == "Skipgram"):    
        model = Word2Vec(sentences=tokenizedtext, size= dimvec, window= winsize, sg = 1)
        model.save("word2vec.model")
        return model

def use_WordRelationship(model,tuple_list,tuple_test):
    
    count = 0
    distlist = []
    for element in tuple_list:
        if (element[0] in model.wv.vocab) and (element[1] in model.wv.vocab):
            dist = model.wv[element[0]] - model.wv[element[1]]
            count+= 1
            distlist.append(dist)

    if count == 0:
        print("Sorry, this operation cannot be performed!")
    
    
    fdist = np.sum(distlist, axis = 0)
    
    averagedist = fdist/count

    print(tuple_test[1])
    word = ""
    if(tuple_test[0] != '' ):
        word = tuple_test[0]
        if (tuple_test[0] in model.wv.vocab):
            finaldist = model.wv[tuple_test[0]] - averagedist

    if(tuple_test[1] != ''):
        word = tuple_test[1]
        if (tuple_test[1] in model.wv.vocab):
            finaldist = model.wv[tuple_test[1]] + averagedist
    
    liste = model.similar_by_vector(finaldist, topn =5)
    for el in liste:
        if word != el[0]:
            print(el)


