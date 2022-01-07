![멋사 캐치프라이즈](https://user-images.githubusercontent.com/66891085/148351155-642ec56e-4843-4e85-8f37-a5c973e55eb8.png)
--------------------------------------------------------------------------
## ✨프로젝트 한줄 소개✨

ZERO_DCE 모델을 이용한 쏘카 input 저조도차량파손사진 개선모델

## 🎁목차🎁


- 🤽‍♀️팀 소개
- 🍕프로젝트 소개
- 🎋느낀점

--------------------------------------------------------------------------
## 🤽‍♂️팀 소개

|Name|최주형|김두진|심영현|이태성|이창근|
|:---|:---:|---:|---:|---:|---:|
|Profile||-|-|![KakaoTalk_20220106_172658148 (1)](https://user-images.githubusercontent.com/66891085/148471052-1291b84f-eca6-4bd6-a8d6-c15772050d3d.jpg)|-|
|Position|1|2|3|4|5|
|Git|1|2|3|@2taesung|5|

--------------------------------------------------------------------------
## 🍕프로젝트 소개

1. **문제 제기**


    쏘카는 일평균 7-8만장, 최대 11만장의 차량 외관 이미지가 업로드된다고 합니다. 

    쏘카에서 진행한 [*'딥러닝모델을 이용한 차량 파손 탐지 딥러닝 모델'*](https://tech.socarcorp.kr/data/2020/02/13/car-damage-segmentation-   model.html) 은 그 중 육안으로 파손 여부를 확실히 판별할수 있는 이미지 2000장을 모델에 이용했다고 합니다.

    2000장의 이미지 중 어두운 곳에서 촬영된 차량 이미지에 모델의 정확도가 떨어지는 문제가 발생했다고 합니다.

    7만장 중에 밤에 찍은 사진이거나, 어두운 곳에서 찍은 사진이 의미 있게 쓰일수는 없을까??? 라는 생각이 들었습니다.

    딥러닝 모델을 이용하여 노이즈가 있거나 저조도의 차량파손 사진을 개선하는 것이 목표입니다.
    
  
  
2. **데이터 준비**


    쏘카에서 제공한 1.3만개의 차량 파손 데이터 중 다음과 같은 기준으로 400개의 이미지를 준비하였습니다.
    
        1. 초점이 잘 맞는 사진

        2. 파손 부위가 잘 보이는 사진
        
        3. 화질이 너무 낮지 않은 사진
    

  
    다양한 밝기에 노출된 이미지를 위해 400개의 이미지에 각각 10번의 transform을 적용하여 총 4000장의 이미지를 이용하였습니다.



3. **모델 선택**


    다음과 같은 구조를 가지는 DCE-net 모델을 사용하였습니다.
  
    <img src = "https://user-images.githubusercontent.com/42459518/148529377-607d4845-8399-4b54-8c89-a3fefb741170.png" width = "50%" height = "50%">
  
    (모델 관련 논문 링크: https://openaccess.thecvf.com/content_CVPR_2020/papers/Guo_Zero-Reference_Deep_Curve_Estimation_for_Low-Light_Image_Enhancement_CVPR_2020_paper.pdf)

4. **모델 선택 이유**
    
    
        1. paired and unpaired 상관없는 training data 사용가능.

        2. 학습시간과 이미지처리 시간이 적게 걸림. (대략 장당 0.001~0.003초)
    


5. **학습**

    <img src = "https://user-images.githubusercontent.com/42459518/148532204-2d9d4eda-9ece-4c5a-9ca6-6c6d4a7ad890.png" width = "40%" height = "40%">
    
    전체 파라미터에서 약 20% 차지하는 마지막 층을 제외한 나머지 층을 freeze시킨후 마지막 층만 학습을 시키는 fine-tuning을 진행하였습니다.
    
    저조도 사진이 모델에 의해 조도 개선이 된 후에는 사진의 미세한 영역들이 뭉게지거나 디테일이 훼손되는 경우가 있는데, 차량이미지 조도 개선 시 파손영역의 디테일이 훼손된다면 문제가 된다고 판단하여
    
    기존 모델에서 채택한 32크기의 feature map이 아닌 다양한 크기의 feature map으로 변경하여 학습을 진행하였고, 최종적으로 64크기의 feature map을 선택하여 학습을 진행하였습니다.
    
    이외에도 학습을 진행할 층 변경, batch size 변경, dataset 구성 변경등 다양한 환경 변화를 주며 hyperparameter tuning을 진행하였습니다.
    
    |Input|기존 model|7층 layer 학습|6,7층 layer 학습|
    |:---|:---:|---:|---:|
    |![20190220_323201550590495119](https://user-images.githubusercontent.com/42459518/148565083-10d8d67e-10cc-41bb-be5b-f8c76d49d206.jpeg)|![20190220_323201550590495119](https://user-images.githubusercontent.com/42459518/148565118-da48808c-5af6-4b16-8cbb-7f4886cd1e70.jpeg)|![20190220_323201550590495119](https://user-images.githubusercontent.com/42459518/148566627-b47f7d6f-f5d5-4afc-a4b2-073ee389e535.jpeg)|![20190220_323201550590495119](https://user-images.githubusercontent.com/42459518/148565177-e34d8927-00ba-49f5-a2c5-995833d591ce.jpeg)
    |1000 image + 8batch + 32feature map|2000 image + 8batch + 32feature map|2000 image + 16batch + 32featuremap|4000 image + 16batch + 64feature map|
    |![20190220_323201550590495119](https://user-images.githubusercontent.com/42459518/148566082-e52004da-3ee3-42b7-acbb-94a6de2336b6.jpeg)|![20190220_323201550590495119](https://user-images.githubusercontent.com/42459518/148566116-e1ecc922-4535-4ebe-b2df-a291318940ad.jpeg)|![20190220_323201550590495119](https://user-images.githubusercontent.com/42459518/148566148-e53bf6c6-df24-4c2b-87d7-427b5721f877.jpeg)|![20190220_323201550590495119](https://user-images.githubusercontent.com/42459518/148566167-210fadf1-bd00-42ba-98d4-bedeb433fd01.jpeg)|

    

    
    최종적으로, 학습시간 및 이미지처리 시간이 적게 걸리는 장점을 유지하며 조도 개선 후에도 사진의 디테일 훼손이 적은 최적의 모델의 파라미터를 설정하였습니다.
    
        최종 학습 환경 : (4000장의 다양한 노출 이미지, batch size : 16, feature map: 64, epoch : 100) 
    
    

5. **결과**

6. **문제점, 개선점**
--------------------------------------------------------------------------
## 🎋느낀점

- 최주형
- 김두진
- 심영현
- 이태성
- 이창근
