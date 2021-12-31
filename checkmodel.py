import torch
import torch.nn as nn
import torchvision
import torch.backends.cudnn as cudnn
import torch.optim
import os
import sys
import argparse
import time
import dataloader
import model
import Myloss
import numpy as np
from PIL import Image
from torchvision import transforms
from torchsummary import summary


# os.environ['CUDA_VISIBLE_DEVICES']='0'

# DCE_net = model.enhance_net_nopool().cuda()

# DCE_net.load_state_dict(torch.load('snapshots\Epoch99.pth'))

print('모델출력')
# print(DCE_net)

# 사진 데이터 크기 확인
# data_lowlight = Image.open('data/test_data/DICM/15.jpg')
# data_lowlight = (np.asarray(data_lowlight)/255.0)
# data_lowlight = torch.from_numpy(data_lowlight).float()
# data_lowlight = data_lowlight.permute(2,0,1)
# data_lowlight = data_lowlight.cuda().unsqueeze(0)
# print(data_lowlight.shape)

#모델 층별 파라미터 확인
# summary(DCE_net, (3, 640, 480))


# 모델 층별 프리즈
# ct = 0
# for child in DCE_net.children():
#   ct += 1
#   # 7번째 conv층의 parameter를 고정
#   if ct == 8:
#     for param in child.parameters():
#         param.requires_grad = False

# 파이토치 버전 확인
# import torch
# print(torch.__version__)