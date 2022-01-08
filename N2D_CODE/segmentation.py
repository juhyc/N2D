# 변환 전후를 판단하기 위한 segmentation 모델 결과값 비교

import os
import time
import random

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

import torch
from torch import nn
import torch.utils.data
from torch.utils.data import Dataset, DataLoader
from torch.utils.data import random_split

import torchvision
from torchvision import datasets, transforms
import torchvision.models as models
from torchvision.models import segmentation

def compare(image1, image2):
    os.environ['CUDA_VISIBLE_DEVICES']='0'

    seg_model = models.segmentation.deeplabv3_resnet101(pretrained=True)
    seg_model.classifier[4] = nn.Conv2d(256, 2, kernel_size=(1,1), stride=(1,1))

    model_path = 'N2D_CODE\model\SOCAR_SEG_1.pth'

    seg_model.load_state_dict(torch.load(model_path))
    seg_model.eval()

    infer_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
    ])

    input_image1 = infer_transform(image1)

    output1 = seg_model(input_image1.unsqueeze(dim=0))

    cls = torch.argmax(output1['out'][0], dim=0).numpy()
    out1 = np.zeros_like(cls)
    out1[cls==1] = 1
    

    input_image2 = infer_transform(image2)

    output2 = seg_model(input_image2.unsqueeze(dim=0))

    cls = torch.argmax(output2['out'][0], dim=0).numpy()
    out2 = np.zeros_like(cls)
    out2[cls==1] = 1

    print("이미지 출력")
    # 이미지 출력
    plot_img = [image1, out1, image2, out2]
    fig = plt.figure(figsize = (20,20))
    for i,pic in enumerate(plot_img):
        ax = fig.add_subplot(2,2,i+1)
        ax.imshow(pic)
    plt.show()

    print("이미지 출력 완료")

if __name__ == "__main__":
    before_image_path = 'data/test_data/SOCAR'
    after_image_path = 'data/result/SOCAR'

    image_path = '수정됨_IMG_4571.jpg'
    # '20190811_483391565449418702.jpeg'
    # 수정됨_IMG_4572.jpg
    # 20190107_293071546810917412.jpeg
    
    image1 = Image.open(before_image_path + "/" + image_path)
    image2 = Image.open(after_image_path + "/" + image_path)

    compare(image1, image2)




