import torch
import torch.nn as nn


class StartingNetwork(torch.nn.Module):
    """
    Basic logistic regression example. You may need to double check the dimensions :)
    """

    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(110, 100) # What could that number mean!?!?!? Ask an officer to find out :)
        self.fc2 = nn.Linear(100, 2)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        '''
        x (tensor): the input to the model
        '''
        x = self.fc1(x)
        x = self.sigmoid(x)
        x = self.fc2(x)
        return x


