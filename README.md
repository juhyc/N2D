![멋사 캐치프라이즈](https://user-images.githubusercontent.com/66891085/148351155-642ec56e-4843-4e85-8f37-a5c973e55eb8.png)
--------------------------------------------------------------------------
## ✨프로젝트 한줄 소개✨

ZERO_DCE 모델을 이용한  저조도차량파손사진 개선모델

## 🎁목차🎁


- 🤽‍♀️팀 소개
- 🍕프로젝트 소개
- 🎋느낀점

--------------------------------------------------------------------------
## 🤽‍♂️팀 소개

|Name|최주형|김두진|심영현|이태성|
|:---:|:---:|:---:|:---:|:---:|
|Profile|![주형님](https://user-images.githubusercontent.com/66891085/148636745-b78824b7-8f35-4223-a134-6cefb71086f5.jpg)|![두진님 (1)](https://user-images.githubusercontent.com/66891085/148635331-a636e9ac-1f00-4998-a362-2108163b17a7.png)|![영현님](https://user-images.githubusercontent.com/66891085/148642104-cca9926c-1d50-4e9e-95a6-122aa167e158.jpg)|![KakaoTalk_20220106_172658148 (1)](https://user-images.githubusercontent.com/66891085/148471052-1291b84f-eca6-4bd6-a8d6-c15772050d3d.jpg)|
|Git|@juhyc|@d00jin|@ks00141|@2taesung|

--------------------------------------------------------------------------
## 🍕프로젝트 소개

1. **문제 제기**


    쏘카에는 일평균 7-8만장, 최대 11만장의 차량 외관 이미지가 업로드됩니다. 
    
    또한, 딥러닝을 이용해 이미지의 파손 부위를 탐지하는 모델을 개발하기도 했습니다.

     [*Semantic Segmentation을 활용한 차량 파손 탐지 딥러닝 모델 개발기*](https://tech.socarcorp.kr/data/2020/02/13/car-damage-segmentation-model.html) (👈 쏘카 기술 블로그 포스팅으로 가기)
    
    위의 프로젝트 과정에서 육안으로 파손 여부를 확실히 판별할수 있는 이미지가 2000장.

    그 중 어두운 곳에서 촬영된 차량 이미지 입력시 모델의 정확도가 떨어지는 문제가 발생했습니다.
    
    ![조도3](https://user-images.githubusercontent.com/66891085/148645333-22b89d3a-0076-4fc7-9470-0e5ec9dd1aae.jpg)
    (출처 : 쏘카 기술 블로그)
    
    
    그래서 우리팀은, 7만장 중에 밤에 찍은 사진이거나, 어두운 곳에서 찍은 사진이 의미있게 쓰일 수 있는 방법은 무엇일까? 에 집중해 보았습니다. 
    
    그 과정에서, 우리들이 배운 내용을 활용한다면 실제 쏘카 어플리케이션에 직접적인 도움이 될 수 있다고 생각했습니다.
    
    <br/>

    🎆결론적으로 
    
    
    
    **딥러닝 모델을 이용해 노이즈 또는 저조도의 차량파손 사진을 개선해,**
    
    **실제 쏘카에서 이미지 인식시 어려움을 겪는 저조도 이미지 문제 해결을 목표했습니다.**
    
<br/>   
  
2. **데이터 준비**

    DCE-net을 조사하고 다루어보며 결과를 비교해본 결과를 토대로,

    쏘카에서 제공한 1.3만개의 차량 파손 데이터 중 다음과 같은 기준으로 400개의 이미지를 준비하였습니다.
    
        1. 초점이 잘 맞는 사진

        2. 파손 부위가 잘 보이는 사진
        
        3. 화질이 너무 낮지 않은 사진
    
    
  
    다양한 밝기에 노출된 이미지를 위해 400개의 이미지에 각각 transform을 적용하여 모델 학습 이미지로 사용하였습니다.



3. **모델 선택**


    다음과 같은 구조를 가지는 DCE-net 모델을 사용하였습니다.
  
    <img src = "https://user-images.githubusercontent.com/42459518/148529377-607d4845-8399-4b54-8c89-a3fefb741170.png" width = "50%" height = "50%">
    
    위 모델은 Unsupervised Learning의 일종인 Non-Reference loss function을 이용합니다.
    
    image에 대한 color constancy loss, exposure control loss, spatial consistency loss, illumination smoothness loss를 loss function으로 사용합니다.
    
    위 loss function으로 image enhancement quality를 측정하고 network를 학습하는 구조입니다.
  
    (모델 관련 논문 링크: https://openaccess.thecvf.com/content_CVPR_2020/papers/Guo_Zero-Reference_Deep_Curve_Estimation_for_Low-Light_Image_Enhancement_CVPR_2020_paper.pdf)

4. **모델 선택 이유**
    
    
        1. paired and unpaired 상관없는 training data 사용가능.

        2. 학습시간과 이미지처리 시간이 적게 걸림. (대략 장당 0.001~0.003초)
    
    
    - 다른 모델들과 비교


        - DSLR(Deep stacked laplacian restorer for low-light image enhancement) : DCE-net 와 비교해 정보가 적고 코드들이 복잡. 해당 모델의 중요한 개념인 Laplacian Pyramid의 어려움.
        
        
        - KinD(Kindling the darkness) : tensorflow 기반, DCE-net 와 비교해 정확도 낮음.


        - TBEFN(A Two-Branch Exposure-Fusion Network) : 추가적인 데이터 튜닝 필요

5. **학습**

    <img src = "https://user-images.githubusercontent.com/42459518/148532204-2d9d4eda-9ece-4c5a-9ca6-6c6d4a7ad890.png" width = "40%" height = "40%">
    
    전체 파라미터에서 약 20% 차지하는 마지막 층을 제외한 나머지 층을 freeze시킨후 마지막 층만 학습을 시키는 fine-tuning을 진행하였습니다.
    
    저조도 사진이 모델에 의해 조도 개선이 된 후에는 사진의 미세한 영역들이 뭉게지거나 디테일이 훼손되는 경우가 있는데, 차량이미지 조도 개선 시 파손영역의 디테일이 훼손된다면 문제가 된다고 판단하여
    
    학습을 진행할 층 변경, batch size 변경, dataset 구성 변경, feature map size 변경등 다양한 환경 변화를 주며 hyperparameter tuning을 진행하였습니다.
    
    |Input|3000img + 8batch + 32f|3000img + 16batch + 32f|
    |:---|:---:|---:|
    |![20190220_323201550590495119](https://user-images.githubusercontent.com/42459518/148633348-106ba036-d475-4713-be96-cde112d9d8e9.jpeg)|![20190220_323201550590495119](https://user-images.githubusercontent.com/42459518/148633357-65777671-c569-47c6-846c-c2238bc63620.jpeg)|![20190220_323201550590495119](https://user-images.githubusercontent.com/42459518/148633369-89ec5535-8b72-4dba-84a2-8cac0e6fefca.jpeg)|
    |4000img + 16batch + 64f|2000img + 16batch + 32f|2000img + 8batch + 32f|
    |![20190220_323201550590495119](https://user-images.githubusercontent.com/42459518/148633448-968f0b51-504a-4dd0-a92b-7ff34ce5b403.jpeg)|![20190220_323201550590495119](https://user-images.githubusercontent.com/42459518/148633454-cc99664d-1992-4497-a2b8-c5e62fc14b29.jpeg)|![20190220_323201550590495119](https://user-images.githubusercontent.com/42459518/148633458-b65b2e80-5f65-4cfc-be8e-a148f630034e.jpeg)|

    batch size와 feature map size가 커질수록 저조도 부위는 많은 개선이 있었지만, 개선 과정에서 사진의 파손부위에 해당하는 디테일 훼손이 심하게 일어나는 경향이 있었습니다.
    
    최종적으로, 학습시간 및 이미지처리 시간이 적게 걸리는 장점을 유지하며 조도 개선 후에도 사진의 디테일 훼손이 적은 최적의 모델의 파라미터를 설정하였습니다.
    
        최종 학습 환경 : (2000장의 다양한 노출 이미지, batch size : 8, feature map: 32, epoch : 100) 
    
    

5. **결과**
    
    학습한 모델을 가지고 다음과 같이 test를 진행하였습니다.
    
    1. 의도적으로 밝기를 낮춘 image에 대해 조도개선
    
       ![image](https://user-images.githubusercontent.com/97295719/148641027-f7ac3508-0388-48eb-b4b5-5df6e4af26fd.png)
       
       PyTorch의 Transform 기능을 사용하여 밝기를 어둡게 조정한 이미지에 대해 조도 개선을 진행하였습니다. 
       
       어두워서 육안으로 파손부위 식별이 잘 되지 않던 이미지가, 파손부위 식별이 용이한 이미지가 되었습니다.
       
       
       ![image](https://user-images.githubusercontent.com/97295719/148641171-50546bc0-188b-43ac-958b-4f16a8fc52ee.png)
       
       개선 전/후 이미지에 대해 Segmentation을 진행한 결과입니다.
       
       개선 전에 비해 개선 후 이미지가 조금 더 넓은 부분을 인식하는 결과를 보여줍니다.
       
       또한, 개선 전 이미지의 경우 손잡이 부분을 파손 부위로 인식하는 오류를 보였으나, 개선 후 이미지에서는 이와 같은 오류가 개선되었습니다.
       
       
       
       다른 사진으로 test를 진행한 결과입니다.
       
       ![image](https://user-images.githubusercontent.com/97295719/148641358-66b8cd39-1ee4-4b02-9f10-c7c147c4cc84.png)
       
       위 이미지의 경우 개선 후에 이미지가 밝아지긴 했으나 육안으로 파손부위를 잡아내는것은 여전히 쉽지 않습니다.
       
       ![image](https://user-images.githubusercontent.com/97295719/148641363-4c06f78c-090a-435f-a513-6a6acabcbb15.png)
       
       개선 전/후 이미지에 대해 Segmentation을 진행한 결과입니다.
       
       개선 후 파손 범위 검출 능력이 매우 향상되는 것을 확인할 수 있습니다.
       
       ![image](https://user-images.githubusercontent.com/97295719/148641368-588fc8d7-0f13-4efe-bff1-506ffe06cf3e.png)
       
       제공된 Mask 이미지와 함께 확인하면 성능 향상을 더 체감할 수 있습니다.



       
    2. SOCAR 제공 image에 대해 조도개선
     
        <img src = "https://user-images.githubusercontent.com/42459518/148634035-7063c3fc-cc75-4439-8c9a-b7514ce8ec31.png" width = 70% height = 70%>
        
        기존 이미지의 파손 부위의 디테일을 약간 훼손하지만 조도 개선을 통해 어두운 부분의 파손 부위가 검출되었습니다.


    3. 실제 외부환경에서 찍은 image에 대해 조도개선
        
       <img src = "https://user-images.githubusercontent.com/42459518/148634593-987dc26d-d961-4e5f-bda4-5e182140d849.png" width = 70% height = 70%>
       
       조도 개선을 통해 이미지의 형태 파악에는 도움이 됐지만, 파손 부위 검출에는 도움이 되지않았습니다.
       
       
       차후 문제점을 파악하여 개선한다면 다양한 활용이 기대됩니다.

    

6. **문제점, 개선점**

    1. Input사진의 화질, 초점 문제
    
    |화질이 낮고, 초점이 맞지 않는 사진|보정 후|화질이 좋고, 초점이 잘 맞는 사진|보정 후|
    |:---:|:---:|:---:|:---:|
    |![초점X개선전사진](https://user-images.githubusercontent.com/42459518/148636248-68864681-5dc8-45d4-a1d2-932e6a383574.jpeg)|![초점X개선사진](https://user-images.githubusercontent.com/42459518/148636252-64e6b173-6f8a-4d5b-b791-ea9be48f2071.jpeg)|![초점O개선전사진](https://user-images.githubusercontent.com/42459518/148636285-09e59d12-4cfd-4359-b6cc-bdf65cac7f22.jpeg)|![초점O개선사진](https://user-images.githubusercontent.com/42459518/148636286-f3a0ef50-b3fc-4f65-b255-a430965289ed.jpeg)|
    
    모델을 통한 조도개선 결과 어느정도 화질저하 문제(노이즈 증가, 디테일 훼손)가 있습니다.
    
    Input Image가 초점이 잘 맞고, 높은 화질의 사진이면 보정결과물도 육안으로 확인가능한 선에서 화질저하가 있습니다.
    
    Input Image가 초점이 잘 맞지 않고, 낮은 화질의 사진이면 보정결과 디테일이 심하게 뭉개지거나, 노이즈 증가 문제가 있습니다.
    
    2. 형체 파악은 좋으나, detail 파악이 아쉬움
    
    |실제 찍은 풍경 사진|보정 후|실제 찍은 차량 사진|보정 후|
    |:---:|:---:|:---:|:---:|
    |![수정됨_KakaoTalk_20220105_191453479 (8)](https://user-images.githubusercontent.com/42459518/148639279-111c8704-0be7-4cef-b0ac-f1ef9198b5e3.jpg)|![수정됨_KakaoTalk_20220105_191453479 (8)](https://user-images.githubusercontent.com/42459518/148639305-8b31b468-9a82-4e29-95e7-620b92bbed33.jpg)|![수정됨_IMG_4567](https://user-images.githubusercontent.com/42459518/148639594-4203750d-7888-4c26-8d00-9a6ceee62e48.jpg)|![수정됨_IMG_4567](https://user-images.githubusercontent.com/42459518/148639408-ff21accd-4966-4dfc-9db1-1af3fa5340f1.jpg)|
    
    조도 개선을 통해 보이지 않았던 형체들이 검출되나, detail한 파악이 아쉬운 모습을 보였습니다.
    
    입력으로 주어진 이미지 안의 객체 위치와 객체의 종류를 파악하는 Obeject Detection에는 유용할것으로 보입니다.
    
    보정 전후 픽셀의 변화가 생기기 때문에 픽셀을 대상으로 한 Classification문제인 Segmentation문제에서는 아쉬운 결과를 보였습니다.
    
    
--------------------------------------------------------------------------
## 🎋느낀점

- 최주형 : 모델의 구조를 변경해보고, 다양한 하이퍼파라미터를 수정하면서 프로젝트 목적과 실제서비스 운영 사이에 적절한 타협점이 필요하다고 느꼈습니다. 배치사이즈를 키우거나, feature map 사이즈를 키우면 학습시간은 오래걸리지만, 좀 더 개선된 사진을 얻을 수 있었습니다. 하지만, 실제 운영서비스에서는 빠른 이미지 처리가 필요하고, 풍경사진이나 인물사진이 아닌 차량파손이미지 사진에 알맞는 결과물을 얻어야 하기 때문에 그에 맞춰서 하이퍼파라미터를 수정하는것이 중요하다고 느꼈습니다. 실제 야간 차량데이터를 찍어봤을때 스마트폰의 자체적인 보정효과가 있어 모델을 통한 개선결과보다 만족스러운 이미지를 반환했습니다. 대부분 스마트폰의 카메라 해상도가 좋아졌기 때문에 서비스 사용자가 카메라 포커스에 잘 맞춰 촬영을 한다면 보다 양질의 데이터셋을 얻을 수 있을것 같다는 생각을 했습니다.

- 김두진 : 멋사 부트캠프에서 머신러닝/딥러닝을 처음 공부하고 프로젝트 역시 처음 해보는 거라 여러면에서 긴장이 되었으나, 좋은 팀원분들 만나서 즐겁게 프로젝트 진행한 거 같습니다!
이번 해커톤을 통해 그동안 글로만 접했던 프로젝트 수행을 직접 경험해보아서 개인적으로는 굉장히 뜻 깊었습니다. 불편한 점을 개선하기 위한 아이디어를 제시하고, 그 아이디어를 구현하기 위해 많은 노력과 끊임없는 호기심, 시행착오에도 무너지지 않는 뚜렷한 목표의식이 필요하다는 것을 느꼈고, 앞으로 어떻게 공부해나가야 할지 어렴풋하게나마 감을 잡을 수 있는 유익한 경험이었습니다^^
 
- 심영현 : 모델 학습용 이미지를 선별하면서, 모델의 성능도 중요하겠지만 원본 데이터의 품질 또한 굉장히 중요 하다고 느꼈습니다.
저희 모델의 경우 저해상도이거나 포커스가 흐린 이미지 처럼 품질이 안좋은 이미지는 아무리 모델의 성능을 올려도 기대하는 만큼 결과가 좋지 못했습니다.
그렇다면 실제 서비스에서 어떻게 양질의 데이터를 많이 얻을수 있을까에 대해 생각하게 되었습니다.
쏘카를 예로들어 차량사진을 전송할때, 그만큼 사진의 각도라던지 포커스 해상도에 제약을 둔다면
양질의 데이터를 얻을수 있겠지만 반대로, 유저의 경우 해당 서비스에 대한 반감이 증가 할 것 같다고 생각 했습니다.
이러한 두 입장차를 머신러닝 엔지니어로써 어떻게 기술적으로 극복 할지에 대해 고민하는 계기가 되었습니다.

- 이태성 : 목표에 맞는 모델들을 찾으며 단순히 최신, 정확도만을 생각하고 선정하면 안되는 걸 알게 되었습니다. 내가 다룰 수 있는 프레임워크, 내가 이해할 수 있는 개념들 그리고 테스트 할 수 있는 환경들 등 고려할 부분들이 많이 있었습니다. 정확도에 영향을 끼치는 다양한 요소들에 대해 생각해보게 되었습니다. 이용자가 최적의 환경에서만 사진을 찍는게 아니라 어둡거나 좋지 않은 화질로 사진을 찍을 경우 해결해줄 수 있는 솔루션을 우리가 제시했습니다. 이를 통해 이용자 친화적인 서비스에 대해 다시 생각해보게 되었고 이를 해결하기 위해 AI 기술들이 큰 기여를 할 수 있을 것에 기대가 되고 흥분이 됩니다.
