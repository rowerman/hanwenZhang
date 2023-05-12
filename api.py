import torch
import numpy as np
from torch.autograd import Variable
import matplotlib.pyplot as plt
import torchvision.utils as vutils
from model import Generator
import os






# 神经网络选择：请依次输入想要选择的神经网络的两个序号，全为-1为示例网络

epoch=-1
iters=-1
Labels=[1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,0,0,0,0,0,0,1,2,3,4]














Labels=torch.tensor(Labels)
generator=Generator()
generator.load_state_dict(torch.load("model/model_"+str(epoch)+"_"+str(iters)+".pt",map_location='cpu'))
labels_onehot = np.zeros((64, 10))
labels_onehot[np.arange(64), Labels.numpy()] = 1

for l in range(20):
    
    z = Variable(torch.randn(64, 100))
    z = np.concatenate((z.numpy(), labels_onehot), axis=1) # 噪音和one-hot 向量加在一起
    z = Variable(torch.from_numpy(z).float())
    output=generator(z)
    i = vutils.make_grid(output[:64], padding=2, normalize=True)
    fig = plt.figure(figsize=(5, 5))
    plt.imshow(np.transpose(i.to('cpu'), (1, 2, 0)))
    plt.axis('off')  # 关闭坐标轴
    plt.savefig("test_picture_output/test_pic_%d.png" % (l))
    plt.close(fig)