from src.clean import CleanData
from termcolor import cprint
from src.model import Train
import pandas as pd
from sys import exit
import os



if __name__ == "__main__" :

    import timeit
    start = timeit.default_timer()
    inFile = "Dataset/DS_800.xlsx"
    outFile = "results/Cleaned_DS.csv"
    
    if (not(os.path.exists(outFile)) or os.stat(outFile).st_size == 0):
        train_set_data = CleanData( inFile , debug=True)
        train_set_data.Dataset.to_csv(outFile, index=False)
    else:
        print("File not empty")
    # print("Dataset is null : ", train_set_data.Dataset.isnull().values.any())
    
    DataSet = pd.read_csv(outFile)
    targets = DataSet.label.values.tolist()
    print(targets)
    DataSet.drop(['label'], axis='columns', inplace=True)
    print(DataSet)
    # cprint("[!] original data : " , 'blue')
    # print(train_set_data.Dataset)
    Train(DataSet , targets)
    stop = timeit.default_timer()
    cprint('Time: '+ str(stop - start) , 'green')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    