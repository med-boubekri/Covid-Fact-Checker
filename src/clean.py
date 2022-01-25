import pandas as pd
import re
from math import log
from gensim.utils import tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from termcolor import cprint

class CleanData : 
    def __init__(self , file , debug=False) :
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
        self.lines = len(self.dataset)
        self.target()
        try : 
            self.clean_urls()
            self.clean_bad_characters()
            self.harmonize()
            self.tokenized()
            self.clean_words()
            self.lemmatize()
            self.stem()
            self.frequency_filtering()
            self.indexing()
            self.ponder()
        except Exception as e : 
            if debug : 
                cprint("[!]"  , 'red' ,end="")
                print("Error : ")
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
        
    def tokenized(self) : 
        """Tokenization , return a list of words of each tweet"""
        self.Words = []
        for row in self.dataset_cleaned["tweet"] : 
            self.Words.append(list(tokenize(row)))

    def clean_words(self) : 
        """Clean words from the stop words list:  unwanted words from english grammer"""
        stopw_english = stopwords.words('english')
        new_line = []
        new_words = []
        for line in self.Words :
            new_line  = [] 
            for i in range(len(line)) :
                if line[i] not in stopw_english :  
                    new_line.append(line[i])
            new_words.append(new_line)
        self.Words = new_words
        
    def lemmatize(self) : 
        """lemmatization using nltk library"""
        lemme = WordNetLemmatizer()
        new_words = []
        for line in self.Words : 
            new = []
            for word in line : 
                new.append(lemme.lemmatize(word))
            new_words.append(new)
        self.Words =  new_words
    def stem(self) : 
        """Stemming using nltk"""
        porter_stem = PorterStemmer()
        new_words = []
        for line in self.Words : 
            new = []
            for word in line : 
                new.append(porter_stem.stem(word))
            new_words.append(new)
        self.Words = new_words
    def frequency_filtering(self):
        """Bag of words indexation : return all the words with frequency > 2"""
        frequency = {}
        dictionary = sum(self.Words, [])
        dictionary = list(set(dictionary))
        for n in dictionary:
            for list_ in self.Words:
                if(n in list_):
                    if(n in frequency):
                        frequency[n] += 1
                    else:
                        frequency[n] = 1
        new_words = []
        for list_ in self.Words:
            new_line = []
            for item in list_:
                if(frequency[item] > 2):
                    new_line.append(item)
            new_words.append(new_line)
        self.Words = new_words
    def indexing(self):
        """Indexing : using the frequency to create a dataset""" 
        self.dictionary = list(set(sum(self.Words, [])))
        columns = self.dictionary
        index_ = [e for e in range(len(self.dataset))]
        self.Dataset = pd.DataFrame(0, index = index_, columns=columns)
        self.Dataset.document = self.dataset.id.copy()
        i = 0
        for line in self.Words: 
            for item in line:
                self.Dataset.loc[i, item] += 1
            i+=1

    def ponder( self) : 
        """Pondering : rearange the frequency to the intarval [0,1]"""
        lignes = len(self.Words)
        for i in range(0,lignes) : 
            for item in self.dictionary : 
                tf = self.Dataset.loc[i , item]/len(self.Words[i])
                freq = 0 
                for line in self.Words :
                    if item in line : freq += 1
                idf = log(lignes/freq , 10)
                self.Dataset.loc[i , item] = tf * idf 
    def target(self) : 
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
