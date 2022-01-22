import pandas as pd
import re

def del_urls(dataset)  :
    # Delete urls from Data set 
    match = r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"
    for row in dataset["tweet"] : 
        m = re.findall(match , row)
        if m != [] : 
            print(m)
    return 

if __name__ == "__main__" :
    dat_set = pd.read_excel('TestDataset.xlsx')
    del_urls(dat_set)
