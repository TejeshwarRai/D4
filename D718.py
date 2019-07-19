from __future__ import print_function, division
import os
import torch
import pandas as pd
from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils

"""
print(torch.__version__)
x = torch.empty(5, 3)
print(x)
print(type(x))
x = torch.rand(3, 3)
print(x)

num = [10, 20, 30, 40]
torchTensor = torch.empty(num)
print(torchTensor)

ndarr = torchTensor.numpy()
print(ndarr)

data = np.array([1, 3, 5, 7, 9])
print(data)

torchData = torch.from_numpy(data)
print(torchData)
"""

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")

plt.ion()
landmarks_frame = pd.read_csv('C:/Users/dell/Desktop/Auribises/D4/faces/face_landmarks.csv')

n = 65
img_name = landmarks_frame.iloc[n, 0]
landmarks = landmarks_frame.iloc[n, 1:].as_matrix()
landmarks = landmarks.astype('float').reshape(-1, 2)

print('Image name: {}'.format(img_name))
print('Landmarks shape: {}'.format(landmarks.shape))
print('First 4 Landmarks: {}'.format(landmarks[:4]))

def show_landmarks(image, landmarks):
    """Show image with landmarks"""
    plt.imshow(image)
    plt.scatter(landmarks[:, 0], landmarks[:, 1], s=10, marker='.', c='r')
    plt.pause(0.001)  # pause a bit so that plots are updated


plt.figure()
show_landmarks(io.imread(os.path.join('C:/Users/dell/Desktop/Auribises/D4/faces', img_name)),
               landmarks)
plt.show()
input()
