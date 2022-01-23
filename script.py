import pandas as pd
import re
from gensim.utils import tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
    

def del_urls(dataset)  :
    # Delete urls from Dataset 
    match = r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'
    i = 0
    for row in dataset["tweet"] : 
        row = str(row)
        row = re.sub(match, '', row)
        dataset.loc[i,"tweet"] = row
        i = i+1
    return dataset

def del_characters(dataset):

    # delete useless characters
    # delete hashtags:
    match_hash = r'#([^\s]+)'
    # delete mentions
    match_mention = r'@([^\s]+)'
    # match characters
    match_char = r"[^0-9A-Za-z\s'-]*"
    
    i = 0
    for row in dataset["tweet"] : 
        row = str(row)
        row = re.sub(match_hash, '', row)
        row = re.sub(match_mention, '', row)
        row = re.sub(match_char, '', row)
        dataset.loc[i,"tweet"] = row
        i = i+1
    return dataset
    
def harmonize(dataset):
    i = 0
    for row in dataset["tweet"] : 
        row = row.lower()
        dataset[i,"tweet"] = row
        i = i+1
    return dataset
    
def tokenized(dataset) : 
    # Tokenization : 
    # Cleaning 
    Words = []
    for row in dataset["tweet"] : 
        Words.append(list(tokenize(row)))
    return Words

def clean_words(words) : 
    stopw_english = stopwords.words('english')
    new = []
    newwords = []
    for line in words :
        new  = [] 
        for i in range(len(line)) :
            if line[i] not in stopw_english :  
                new.append(line[i])
        newwords.append(new)
    return newwords
    
def lemmatize(words) : 
    lemme = WordNetLemmatizer()
    newords = []
    for line in words : 
        new = []
        for word in line : 
            new.append(lemme.lemmatize(word))
        newords.append(new)
    return newords
def stem(words) : 
    ps = PorterStemmer()
    newords = []
    for line in words : 
        new = []
        for word in line : 
            new.append(ps.stem(word))
        newords.append(new)
    #print(newords)
    return newords

def frequency_filtering(dataset):
    frequency = {}
    # flatten 2d list to 1d list
    dictionary = sum(dataset, [])
    # unique elements of all documents
    dictionary = list(set(dictionary))
    # for all elements in the dictionary
    for n in dictionary:
        #if element figures in a list of the 2d list
        for list_ in dataset:
            if(n in list_):
               if(n in frequency):
                  frequency[n] += 1
               else:
                  frequency[n] = 1
    """
    # sort items in dictionary by value
    import operator
    frequency = sorted(frequency.items(), key=lambda kv: kv[1])
    print(frequency)
    """
    newwords = []
    for list_ in dataset:
        new = []
        for item in list_:
            if(frequency[item] > 2):
                 new.append(item)
            newwords.append(new)
    return newwords
        

if __name__ == "__main__" :
    dat_set = pd.read_excel('TestDataset.xlsx')
    data_set_no_url = del_urls(dat_set)
    data_set_cleaned = del_characters(data_set_no_url)
    data_set_harmonized = harmonize(data_set_cleaned)
    data_set_words = tokenized(data_set_harmonized)
    data_set_words_cleaned = clean_words(data_set_words)
    data_set_words_lemme = lemmatize(data_set_words_cleaned)
    data_set_words_stem = stem(data_set_words_lemme)
    data_set_words_freq_filtered = frequency_filtering(data_set_words_stem)
    
    
    
    dictionary = sum(data_set_words_freq_filtered, [])
    dictionary = list(set(dictionary))
    #print(dictionary)
    _list = ['document']
    _list.extend(dictionary)
    Dataset = pd.DataFrame(0, index= dat_set.id, columns=_list)
    print(Dataset)
    
    
    Dataset.document = dat_set.id
    
    frequency = {}
    for _list in data_set_words_freq_filtered:
        i = 1
        for item in _list:
            Dataset.loc[i, item] += 1
        
        
    """
    dictionary.sort()
    i= 0
    for n in dictionary:
        print(i,": ",n)
        i = i+1
    """















