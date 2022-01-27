from src.clean import CleanData
from termcolor import cprint
from src.model import Train
from sys import exit


if __name__ == "__main__" :

    import timeit
    start = timeit.default_timer()
    file = "Dataset/DS_800.xlsx"
    train_set_data = CleanData( file , debug=True)
    train_set_data.Dataset.to_csv("results/res2.csv")
    Train(train_set_data.Dataset , train_set_data.targets)
    stop = timeit.default_timer()
    cprint('Time: '+ str(stop - start) , 'green')
