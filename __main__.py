from src.clean import CleanData
from termcolor import cprint
from src.model import Train
from sys import exit


if __name__ == "__main__" :

    import timeit
    start = timeit.default_timer()
    file = "Dataset/DS_800.xlsx"
    train_set_data = CleanData( file , debug=True)
    print("============ Data Frame Nan main", train_set_data.Dataset.isnull().values.any())
    #train_set_data.Dataset.to_csv("results/res2.csv")
