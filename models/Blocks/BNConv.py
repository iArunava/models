import torch
import torch.nn as nn

class BNConv(nn.Module):

    def __init__(self, in_channels, out_channels, kernel_size, stride,
                 padding, eps, momentum):
        '''
        '''

        super(BNConv, self).__init__()
        
        self.main = nn.Sequential(
                    nn.Conv2d(in_channels=in_channels,
                                          out_channels=out_channels,
                                          stride=stride,
                                          padding=padding,
                                          bias=bias),
                    
                    nn.BatchNorm2d(out_channels, eps=eps, momentum=momentum)
                )


    def forward(self, x):
        '''
        Method that defines the forward pass through the BNConv network.

        Arguments:
        - x : The input to the network

        Returns:
        - The output of the network BNConv
        '''

        x = self.main(x)

        return x
