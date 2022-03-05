from gui.src.clean import CleanData
from termcolor import cprint
from gui.src.model import Train
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt


if __name__ == "__main__" :

    import timeit
    start = timeit.default_timer()
    inFile = "Dataset/DataSet.xlsx"
    outFile = "results/Cleaned_DS_test.csv"
    train_set_data = CleanData( inFile , debug=True  , test = False)
    #Clean Test set
    inFile= "Dataset/TestSet.xlsx"
    test_set_data = CleanData( inFile , debug=True , test = True )
    
    #Change to actual value
    layers = 3
    
    for lr in [0.0001, 0.00002, 0.00003, 0.00005, 0.00001]:
        #changer les ecpochs et les couches manuellement
        train = Train(train_set_data.Dataset ,train_set_data.targets , test_set_data.Dataset , test_set_data.targets , True, lr)
        
        """ Data visualization """
        x = list(train.validation_loss.keys())
        y1 = list(train.validation_loss.values())
        y2 = list(train.training_loss.values())
        y3 = list(train.accuracy.values())
        
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.plot(x, y1,  label='Validation loss')
        ax.plot(x, y2, label='Training loss')
        ax.plot(x, y3, label='Accuracy')
        ax.set_xlabel('Epochs')
        ax.set_ylabel('Loss/Acc')
        ax.text(0,0.95, f"Learning rate: {lr} / Couches:{layers}", fontsize=10)
        plt.ylim([0, 1])
        plt.axhline(y=train.test_correct, color='y', linestyle='-', label="Test accuracy")
        plt.axhline(y=train.test_loss, color='r', linestyle='-', label="Test loss")
        plt.legend(loc = 'upper right')
        fig1 = plt.gcf()
        plt.show()
        plt.draw()
        fig1.savefig(f'viz/Lay_{layers}_LR_{lr}.png')
    
    
    stop = timeit.default_timer()
    cprint('Time: '+ str(stop - start) , 'green')


















