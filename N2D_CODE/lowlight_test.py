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
import numpy as np
from torchvision import transforms
from PIL import Image
import glob
import time

 
def lowlight(image_path):
	os.environ['CUDA_VISIBLE_DEVICES']='0'
	data_lowlight = Image.open(image_path)

	data_lowlight = (np.asarray(data_lowlight)/255.0)

	data_lowlight = torch.from_numpy(data_lowlight).float()
	data_lowlight = data_lowlight.permute(2,0,1)
	data_lowlight = data_lowlight.cuda().unsqueeze(0)

	DCE_net = model.enhance_net_nopool().cuda()
	
	# DCE_net.load_state_dict(torch.load('snapshots/Epoch99.pth'))
	
	DCE_net.load_state_dict(torch.load('N2D_CODE/snapshots/NewEpoch99.pth'))
	start = time.time()
	_,enhanced_image,_ = DCE_net(data_lowlight)

	end_time = (time.time() - start)
	print(end_time)

	image_path = image_path.replace('test_data','result')
	result_path = image_path
	
	temp_path = result_path.replace("\\",'/')
	temp_path = temp_path.split("/")[-2]
	
	# print(temp_path)
	# print(image_path.replace('/'+image_path.split("/")[-1],'')+ "/" + temp_path)

	if not os.path.exists(image_path.replace('/'+image_path.split("/")[-1],'')+ "/" + temp_path):
		os.makedirs(image_path.replace('/'+image_path.split("/")[-1],'')+ "/" + temp_path)

	# result_path = result_path.replace("\\",'/')
	# print('변환 결과: ' + result_path)

	torchvision.utils.save_image(enhanced_image, result_path)

if __name__ == '__main__':
# test_images
	with torch.no_grad():
		filePath = 'data/test_data/'
		
		file_list = os.listdir(filePath)

		for file_name in file_list:
			test_list = glob.glob(filePath + file_name + "/*") 
			for image in test_list:
				# image = image
				print(image)
				lowlight(image)

		

