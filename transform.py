import glob
import os
import torch
import torchvision
import numpy as np
from PIL import Image
from pathlib import Path
from torchvision import transforms as T

# 변경할 사진을 data/socar_data에 넣기
# 변경된 사진은 data/transformed 항목에 생성됨

filePath = 'data/socar_data/'
file_list = glob.glob(filePath + "/*")
jitter = T.ColorJitter(brightness=[0.2,1.2], contrast = [0.2,1.2])

savepath = filePath.replace('socar_data','transformed')

if not os.path.exists(savepath):
	os.makedirs(savepath)

disp_cnt = 0

for image in file_list:

  origin_img = Image.open(image)
  jitted_imgs = [jitter(origin_img) for _ in range(5)]
  temp = image.split('/')[-1].split('.')[0]
  temp_path = temp.split('\\')[-1]
  disp_cnt += 1

  if(disp_cnt % 10 ==0):
      print(f"변경완료 : {disp_cnt}/{len(file_list)}")

  for i in range(5):
    img = jitted_imgs[i]
    img.save(os.path.join(savepath, temp_path + str(i) + '.jpg'))
    