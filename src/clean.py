import pandas as pd
import re
from math import log
from gensim.utils import tokenize as tk
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from termcolor import cprint
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import sys
import os

class CleanData : 
    def __init__(self , file , debug=False, index_col=id) :
        self.debug = debug
        self.Dataset =pd.DataFrame()
        try : 
            self.dataset = pd.read_excel(file)
            if debug : 
                cprint("[+] " , 'green' , end="")
                cprint("Dataset loaded")
        except FileNotFoundError :
            if debug :  
                cprint("[!] ", 'red' , end="")
                cprint("File not found . exiting ...")
            exit(0)
        try : 
            self.lines = len(self.dataset)
            self.target()
            self.clean_urls()
            self.clean_bad_characters()
            self.harmonize()
            self.ponderation()
            if debug : 
                cprint("[+] " , 'green' , end="")
                cprint("Data cleaned")
        except Exception as e : 
            if debug : 
                cprint("[!] "  , 'red' ,end="")
                print("Error : ")
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print(e)
            cprint("[!]"  , 'red' ,end="")
            print("Error occured , exiting ... ")
    def clean_urls(self) : 
        """"Clean urls from datasets"""
        match = r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'
        i = 0
        self.dataset_cleaned = self.dataset.copy()
        for row in self.dataset_cleaned["tweet"] : 
            row = str(row)
            row = re.sub(match, '', row)
            self.dataset_cleaned.loc[i,"tweet"] = row
            i = i+1
    def clean_bad_characters(self) : 
        """"Delete hashtags, mentions and any characters other than ' and -"""
        match_hashtag = r'#([^\s]+)'
        match_mention = r'@([^\s]+)'
        match_char = r"[^0-9A-Za-z\s'-]*"
        i = 0
        for row in self.dataset_cleaned["tweet"] : 
            row = str(row)
            row = re.sub(match_hashtag, '', row)
            row = re.sub(match_mention, '', row)
            row = re.sub(match_char, '', row)
            self.dataset_cleaned.loc[i,"tweet"] = row
            i = i+1
    def harmonize(self):
        """"lowercase all tweets of the cleaned dataset """
        i = 0
        for row in self.dataset_cleaned["tweet"] : 
            row = row.lower()
            self.dataset_cleaned.loc[i,"tweet"] = row
            i = i+1

    def extract_tokens(self, text) :
        """Tokenization , return a list of words of each tweet"""
        Words = []     
        i = 0 
        for row in self.dataset_cleaned["tweet"] : 
            Words.append(list(tk(row)))
            i+=1
        return Words

    def clean_words(self, words) : 
        """Clean words from the stop words list:  unwanted words from english grammer"""
        stopw_english = stopwords.words('english')
        new_line = []
        new_words = []

        for line in words :
            new_line  = [] 
            for i in range(len(line)) :
                if line[i] not in stopw_english :  
                    new_line.append(line[i])
            new_words.append(new_line)
        return new_words
        
    def lemmatize(self, words) : 
        """lemmatization using nltk library"""
        lemme = WordNetLemmatizer()
        new_words = []
        for line in words : 
            new = []
            for word in line : 
                new.append(lemme.lemmatize(word))
            new_words.append(new)
        return new_words
    def stem(self, words): 
        """Stemming using nltk"""
        porter_stem = PorterStemmer()
        new_words = []
        for line in words : 
            new = []
            for word in line : 
                new.append(porter_stem.stem(word))
            new_words.append(new)
        return new_words
        
    def frequency_filtering(self, words):
        """Bag of words indexation : return all the words with frequency > 2"""
        frequency = {}
        dictionary = sum(words, [])
        dictionary = list(set(dictionary))
        for n in dictionary:
            for list_ in words:
                if(n in list_):
                    if(n in frequency):
                        frequency[n] += 1
                    else:
                        frequency[n] = 1
        new_words = []
        for list_ in words:
            new_line = []
            for item in list_:
                if(frequency[item] > 2):
                    new_line.append(item)
            new_words.append(new_line)
        return new_words
        
    def tokenize(self, text):
        tokens = self.extract_tokens(text)
        tokens = self.clean_words(tokens)
        tokens = self.lemmatize(tokens)
        tokens = self.stem(tokens)
        tokens = self.frequency_filtering(tokens)
        return tokens
    
    
    def ponderation(self):
        tweets = self.dataset_cleaned['tweet']
        tweets = np.array(tweets)
        tweets_tokenized = self.tokenize(self.dataset_cleaned['tweet'])
        tweets_tokenized_txt = [" ".join(x) for x in tweets_tokenized]
        vectorizer = TfidfVectorizer()
        tfidf_encodings = vectorizer.fit_transform(tweets_tokenized_txt)
        tfidf_encodings_array = list(tfidf_encodings.toarray())
        self.Dataset = pd.DataFrame(0, index = self.dataset.index, columns=["tweet"])
        self.Dataset.tweet = tfidf_encodings_array
        

    def target(self) : 
        """store targets (labels) on a list"""
        self.targets = []
        for i in range(0 , self.lines ) :
            if self.dataset.loc[i , 'label'] == 'real' :
                self.targets.append(1)
            elif self.dataset.loc[i , 'label'] == 'fake' : 
                self.targets.append(0)
            else : 
                cprint("[!] " , 'red' , end="")
                print("Error target not in ('real' , 'fake') , crashing ..")
                exit(0)
        