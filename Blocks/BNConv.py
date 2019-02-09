import torch
import torch.nn as nn

class BNConv(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size,
                 padding, stride):
        '''
        The constructor for the BNConv Class
        
        Arguments:
        - in_channels : The number of input channels to the first conv layer
        - out_channels : # of output channels for the first conv layer
        - kernel_size : the kernel size
        - padding : the padding height and width
        - stride : the stride length
        '''
        
        super().__init__()
        
        self.conv = nn.Conv2d(in_channels=self.in_channels,
                              out_channels=self.out_channels,
                              kernel_size=self.kernel_size,
                              padding=self.padding,
                              stride=self.stride)
        
        self.bnorm = nn.BatchNorm2d(self.out_channels)
        
    def forward(self, x):
        '''
        The method which defines the forward pass of BNConv module
        
        Arguments:
        - x : the input to the network
        
        Returns:
        - the output of the network
        '''
        
        x = self.conv(x)
        x = self.bnorm(x)
        
        return x
