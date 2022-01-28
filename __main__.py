from gui.src.clean import CleanData
from termcolor import cprint
from gui.src.model import Train
import pandas as pd
from sys import exit



if __name__ == "__main__" :

    import timeit
    start = timeit.default_timer()
    inFile = "Dataset/TrainSet.xlsx"
    outFile = "results/Cleaned_DS_test.csv"
    # Train set 
    train_set_data = CleanData( inFile , debug=False  , test = False)
    # DataSet = train_set_data.Dataset
    # targets = train_set_data.targets
    # print(targets)
    # Test set
    inFile= "Dataset/TestSet.xlsx"
    test_set_data = CleanData( inFile , debug=True)
    Train(train_set_data.Dataset ,train_set_data.targets , train_set_data.Dataset , train_set_data.targets)
    #DataSet.drop(['label'], axis='columns', inplace=True)
    #print(DataSet)
    # cprint("[!] original data : " , 'blue')
    # print(train_set_data.Dataset)
    stop = timeit.default_timer()
    cprint('Time: '+ str(stop - start) , 'green')

