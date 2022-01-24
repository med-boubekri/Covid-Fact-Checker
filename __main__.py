from src.clean import CleanData
from termcolor import cprint
if __name__ == "__main__" :
    import timeit
    start = timeit.default_timer()  
    data_set_cleaned = CleanData("Dataset/TestDataset.xlsx" , debug=True)
    stop = timeit.default_timer()
    cprint('Time: '+ str(stop - start)  , 'green')  