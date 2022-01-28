from src.clean import CleanData
from termcolor import cprint
from src.model import Train
import pandas as pd
from sys import exit
import os



if __name__ == "__main__" :

    import timeit
    start = timeit.default_timer()
    inFile = "Dataset/DataSet.xlsx"
    outFile = "results/Cleaned_DS_test.csv"
    train_set_data = CleanData( inFile , debug=True)
    DataSet = train_set_data.Dataset
    targets = train_set_data.targets
    #DataSet.drop(['label'], axis='columns', inplace=True)
    #print(DataSet)
    # cprint("[!] original data : " , 'blue')
    # print(train_set_data.Dataset)
    Train(DataSet , targets)
    stop = timeit.default_timer()
    cprint('Time: '+ str(stop - start) , 'green')

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    