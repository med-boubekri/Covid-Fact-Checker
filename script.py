import pandas as pd
import re

def del_urls(dataset)  :
    # Delete urls from Data set 
    match = r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'
    i = 0;
    for row in dataset["tweet"] : 
        row = str(row)
        row = re.sub(match, '', row)
        dataset["tweet"][i] = row
        i = i+1
    return dataset

def del_characters(dataset):

    # delete useless characters
    # delete hashtags:
    match_hash = r'#([^\s]+)'
    # delete mentions
    match_mention = r'@([^\s]+)'
    # match characters
    match_char = r'[^0-9A-Za-z\s-]*'
    
    i = 0;
    for row in dataset["tweet"] : 
        row = str(row)
        row = re.sub(match_hash, '', row)
        row = re.sub(match_mention, '', row)
        row = re.sub(match_char, '', row)
        dataset["tweet"][i] = row
        i = i+1
        print(row)
    return dataset
    
def harmonize(dataset):
    i = 0;
    for row in dataset["tweet"] : 
        row = row.lower()
        dataset["tweet"][i] = row
        i = i+1
        print(row)
    return dataset
    

if __name__ == "__main__" :
    dat_set = pd.read_excel('TestDataset.xlsx')
    data_set_no_url = del_urls(dat_set)
    
    data_set_cleaned = del_characters(data_set_no_url)
    
    data_set_harmonized = harmonize(data_set_cleaned)
