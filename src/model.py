import torch
import torch.nn
import pandas as pd 
from sklearn.model_selection import train_test_split
from termcolor import cprint
from torch.utils.data import Dataset
from torch.utils.data import DataLoader 
import torch.nn.functional as Functional

class Model(Dataset)  :
    def __init__(self , dataset , targets):
        self.data = dataset
        self.targets = targets
    
    def __len__(self):
        return len(self.targets)

    def __getitem__(self, idx):
        return  self.data[idx], self.targets[idx]

class MyNeural(torch.nn.Module):
    def __init__(self , columns):
        super(MyNeural, self).__init__()
        # input/hidden/output layers
        # Nous devons préciser le nombre de Hidden layers que nous allons utiliser
        self.f1 = torch.nn.Linear(columns, 32)
        self.f2 = torch.nn.Linear(32, 16)
        self.f3 = torch.nn.Linear(16, 1)

    # x = le tensor, 
    def forward(self, x):
        x = self.f1(x)
        x = Functional.relu(x)
        x = self.f2(x)
        x = Functional.relu(x)
        x = self.f3(x)
        return x


class Train() :
    def __init__(self , data , targets):
        self.data = torch.tensor(data.values)
        self.targets = torch.tensor(targets) 
        cprint("[+] Starting spliting and normalizing" , 'green')
        self.split()
        self.normalize()
        cprint("[+] Starting modeling and loading " , 'green')
        self.model()
        self.load()
        cprint("[+] Starting Training" , 'green')
        self.training()
    def split(self) :
        self.train_set, self.test_set, self.train_targets, self.test_targets = train_test_split(self.data, self.targets, test_size=0.2, random_state=42)
        self.train_set, self.validation_set, self.train_targets, self.validation_targets = train_test_split(self.train_set, self.train_targets, test_size=0.2)
    def normalize(self) : 
        self.train_set = (self.train_set - torch.mean(self.train_set)) /  torch.std(self.train_set)
        self.validation_set = (self.validation_set - torch.mean(self.validation_set)) /  torch.std(self.validation_set)
        self.train_set = (self.test_set - torch.mean(self.test_set)) /  torch.std(self.test_set)
    def model(self) : 
        self.train = Model(self.train_set , self.train_targets)
        self.test = Model(self.test_set , self.test_targets)
        self.validation = Model(self.validation_set , self.validation_targets)
    def load(self) : 
        self.batch = 32
        self.train_DL = DataLoader(self.train, batch_size=self.batch)
        self.test_DL = DataLoader(self.test, batch_size=self.batch)
        self.validation_DL = DataLoader(self.validation, batch_size=self.batch)
    def training(self) :
        self.net = MyNeural(self.data.shape[1])
        self.entropyloss = torch.nn.CrossEntropyLoss()
        self.optim = torch.optim.Adam(self.net.parameters(), lr=0.001)
        self.epochs=5
        for i in range(self.epochs): 
            self.net.train(mode=True)
            train_loss = 0.0
            i = 0
            for  data, targets in self.train_DL:
                cprint(f"iteration : {i}" , 'blue')
                pred_targets = self.net(data)
                loss += self.entropyloss(pred_targets, targets)
                self.optim.zero_grad()
                loss.backward()
                self.optim.step()
                train_loss += loss.item()
                i+=1
            train_loss /= len(self.train_DL)
            valid_loss = 0.0
            correct = 0
            self.net.eval()
            with torch.no_grad():
                for data, targets in self.validation_DL:
                    pred_targets = self.net(data)
                    loss = self.cout(pred_targets, targets)
                    valid_loss += loss.item()
                    correct += torch.sum(torch.argmax(pred_targets, dim=1) == targets).item()
                valid_loss /= len(self.validation_DL)
                correct /= len(self.validation_DL.dataset)
                print(f"epoch: {i}, train_loss: {train_loss:.4f},test_loss: {valid_loss} valid_loss: {valid_loss:.4f}, correct predictions: {correct*100:.2f}%") 
            

def main(data  , targets) :
    """Split data and create model"""
    # data = torch.tensor(data)
    # targets = torch.tensor(targets)
    # train_set, test_set, train_targets, test_targets = train_test_split(data, targets, test_size=0.2, random_state=42)
    # train_set, validation_set, train_targets, validation_targets = train_test_split(train_set, train_targets, test_size=0.2)
    # train_set = (train_set - torch.mean(train_set)) /  torch.std(train_set)

