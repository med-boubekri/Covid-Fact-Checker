from termcolor import cprint
import pandas as pd
import os
from pathlib import Path
from gui.main_window import main
HOME = str(Path.home())

from gui.src.model import Train
from gui.src.clean import CleanData


if __name__ == "__main__" :
    main()
    # import timeit
    # start = timeit.default_timer()
    # inFile = "Dataset/TrainSet.xlsx"
    # outFile = "results/Cleaned_DS_test.csv"
    # # Train set 
    # train_set_data = CleanData( inFile , debug=False  , test = False)
    # # DataSet = train_set_data.Dataset
    # # targets = train_set_data.targets
    # # print(targets)
    # # Test set
    # inFile= "Dataset/TestSet.xlsx"
    # test_set_data = CleanData( inFile , debug=False , test=True)
    # tester = Train(train_set_data.Dataset ,train_set_data.targets , train_set_data.Dataset , train_set_data.targets , debug=True)
    # file= HOME + "\\hehe.txt"
    # with open(file , 'r' ,errors="ignore") as fd : 
    #     lines = fd.readlines()
    #     for line in lines :  
    #         line = line.strip()
    #         tweet_cleaned = CleanData.clean(line)
    #         real = tester.predict(tweet_cleaned)
    #         print(line)
    #         cprint('is ' +( "real" if real else "fake")   , 'green')
        
    # #DataSet.drop(['label'], axis='columns', inplace=True)
    # #print(DataSet)
    # # cprint("[!] original data : " , 'blue')
    # # print(train_set_data.Dataset)
    # stop = timeit.default_timer()
    # cprint('Time: '+ str(stop - start) , 'green')