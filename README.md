
# Avg26 (23-1 HUFS Capstone)

# personal Color Performance
### Personal Color Performance recognizes a person's picture and shows the submission background as a web.

<b>2023.06.21 한국외국어대학교 캡스톤설계 프로젝트 최우수상 수상 </b>
(<a href="https://con2.kr/%E3%88%9C%EB%A7%88%EB%A3%A8%ED%8A%B8%EB%A0%88%EC%9D%B4%EB%8D%94-%ED%95%9C%EA%B5%AD%EC%99%B8%EB%8C%80%EC%99%80-%EC%82%B0%ED%95%99-%ED%98%91%EB%A0%A5%EC%9C%BC%EB%A1%9C-%EC%98%88%EC%88%A0%EA%B8%B0/"> 캡스톤 수상 관련 기사 </a>)
<br>

| **Name** | **Role**                                                     | **Contact**           |
| -------- | ------------------------ | --------------------- |
| 김채현   | 팀장,인공지능 개발 | spec327@naver.com |
| 조성민   | 백엔드 개발 및 서버 구축 | another0306@naver.com |
| 이건중   |  프론트엔드 개발 | namuju_hi@naver.com   |

# Key Words

* 감정
* 배경
* Yolo
* Stable Diffusion
* 색상


# Motivation
코로나로 인해 제한되었던 사회 활동이 점차 정상화되어 가며, 정체되어 있던 문화/공연 사업도 다시금 활기를 찾았습니다.

 기존, 단순히 공연자가 공연을 통해 관객을 만나는 공연 문화에서, 관람객들이 공연에 참여하는 참여형 공연으로 공연 기획의 트렌드가 많이 변하는 모습을 볼 수 있습니다. 일반적으로, 무대 배경에 많이 사용되는 이미지는 사전에 준비한 단조로운 배경이나 뮤직 비디오, 가사가 있는 경우 가사를 표시해주는 배경입니다.

 공연을 관람하는 관객들의 표정을 이용해 감정을 추정하고, 추정한 감정을 사전에 지정된 색상을 이용해 의도된 무대 배경을 생성하고 활용하는 것이 본 프로젝트의 개발 목적입니다.

관객의 감정이 표현된 무대 배경을 활용해, 참여형 공연을 기획할 수 있으며, 공연자도 관객의 감정/반응 상태를 실시간으로 파악해 공연에 도움을 줍니다.


# development goal
- 호스팅 웹/프로그램 형태로 제작하며, 일정 시간의 버퍼 타임 (15초~30초) 간격으로 관객의 감정을 추정하고, 이에 상응하는 배경 이미지를 생성 및 출력

- 객체 탐지 Pretrain-Model인 Yolo를 파인 튜닝하여, 관객의 표정을 통해 감정을 추정할 수 있는 모델 개발

- 사전에 정의된 프롬포트를 이용해, 감정이 포함된 무대 배경을 생성하는 생성 모델(Stable-Diffusion) 개발

# final result

<img width="610" alt="스크린샷 2023-08-03 오후 11 21 26" src="https://github.com/nuyhc/Avg26_Personal_Color_Performance/assets/101984130/5ba1a97f-c464-4ff3-8103-8e4c0e976629">
관객들로부터 추정된 감정과 공연의 의도 감정을 상기 표의 색상을 이용해 무대 배경 생성에 활용합니다.

 관객 이미지 -> 감정 추정 -> 색상 맵핑 -> 무대 배경 생성의 파이프라인으로 구성
결과 2. (예시) 관객 이미지와 추정된 감정됩니다.<img width="511" alt="스크린샷 2023-08-03 오후 11 31 30" src="https://github.com/nuyhc/Avg26_Personal_Color_Performance/assets/101984130/11226834-03b2-4a79-a596-5bd73e55958e">
<img width="524" alt="스크린샷 2023-08-03 오후 11 31 48" src="https://github.com/nuyhc/Avg26_Personal_Color_Performance/assets/101984130/850c0f29-27de-4977-8c75-a3cc2cf0a669"><br>

 추정된 감정 중, 가장 많이 추정된 감정을 이용해, 해당 감정의 정확도(confidence)를 색상의 조도로 이용해 무대 배경을 생성하게 됩니다.

 생성 모델에 의해 무대 배경이 생성되므로, 동일한 입력값이 입력되어도 동일한 배경이 생성될 가능성은 매우 희박합니다.

 <img width="475" alt="스크린샷 2023-08-03 오후 11 31 59" src="https://github.com/nuyhc/Avg26_Personal_Color_Performance/assets/101984130/15d082a9-634d-484b-894c-52e2e02e3180">
 <img width="525" alt="스크린샷 2023-08-03 오후 11 32 16" src="https://github.com/nuyhc/Avg26_Personal_Color_Performance/assets/101984130/bbf7f830-5fb0-46ec-9113-d811cceded9c">

# Content of the project


<img width="586" alt="스크린샷 2023-08-03 오후 11 39 43" src="https://github.com/nuyhc/Avg26_Personal_Color_Performance/assets/101984130/f92d7c6b-b975-4038-88c4-fcb48ffb31f1">
관객들로부터 감정을 추정하기 위해, 객체 탐지 모델인 Yolov5와 Yolov7을 파인튜닝했습니다. v5 모델과 v7 모델 모두, mAP50과 mAP95 모두 90%, 80% 이상의 성능을 보였고 실시간 영상 및 이미지로부터 표정을 통해 감정을 추정하는 것이 가능합니다.

 사용자가 사전에 정의한 감정(공연의 기획으로 의도된 감정)과 함께 추정된 감정이 무대 배경 생성에 사용되며, 객체 인식에 실패한 경우 기획 감정에 따라 무대 배경이 생성되게 됩니다.  배경 생성은 Hugging Face의 Stable-Diffusion 파이프라인을 사용했습니다.

 1.데이터셋 정제 및 파인튜닝

 KAIST에서 생성한, 한국인 감정 인식을 위한 복합 영상 데이터 (AI HUB)를 이용했으며, 7개의 레이블(분노, 당황, 기쁨, 중립, 슬픔, 상처, 불안)과 총 43만장의 이미지로 이뤄진 대규모 데이터 셋입니다.

 이미지의 메타 정보로, 사람의 얼굴이 위치한 좌표(Anchor Box)를 함께 제공하고 있으므로, 객체 탐지 모델을 학습 시키기 위한 앵커링 작업을 최소화 할 수 있는 장점이 있습니다.

 초기 7개의 레이블을 모두 사용한 경우와 유사한 감정 (불안/당황, 슬픔/상처)을 묶어 5개의 레이블만 사용한 경우를, CNN 기반 EfficentNetB0 모델을 통해 사전 분류를 진행하고, 최종적으로 감정의 종류 (5개 레이블)를 정의하고 사용했습니다

<img width="512" alt="스크린샷 2023-08-03 오후 11 43 07" src="https://github.com/nuyhc/Avg26_Personal_Color_Performance/assets/101984130/958befc0-4a3c-489a-8cec-ebb0a778567c">

<img width="548" alt="스크린샷 2023-08-03 오후 11 47 59" src="https://github.com/nuyhc/Avg26_Personal_Color_Performance/assets/101984130/96300269-831b-4d58-8e2c-92c82468e291">





2.관객 이미지 전달과 배경 이미지 출력

 React를 이용하여 사용자의 카메라 input 영상을 받고, 특정 Interval 마다 캡쳐하여 감정 추정 모델에 전달하는 Front End App을 개발했습니다.

 통신과 결과를 출력하는 Main 컴포넌트인 App.js와 Camera와 Capture를 담당하는 CamHanlder.js 컴포넌트로 구성되며, POST 방식으로 전송과 수신이 이뤄집니다.

 Back End는 Django를 이용해 구현하였으며, 감정 추정 및 배경 생성 모델의 동작을 수행하며 추정된 감정을 기록합니다.


 
3.관객 이미지 전달 처리 과정

  Front에서 관객 이미지 값이 오면 값을 저장하고 folder_path에 저장되는 경로를 넣는다. 이후에 os를 import 한 후 os.listdir()함수를 활용해서 안에 있는 값들을 가져오고 sorted 함수를 활용해서 생성 순서대로 값을 정렬 시킨 후 가장 첫 번째로 생성된 파일을 불러온다. 그 후 해당경로를 ai로 전송해서 이미지 경로를 보낸 후 이미지 값이 나오면 그 값을 다시 프론트로 보내서 사람의 감정인식 후 나오는 배경그림을 보여주게 한다.

 또한 보낼 때 값을 modelviewset을 통해서 값을 전달받고 그 값을 그대로 프론트로 retrun시킨다. 이때 값을 serializer를 통해서 값을 직렬화 하는 과정을 거친 후에 값을 보내는 식으로 해서 프론트에 값을 전달한다.

 # Benefit
 - 관객이 공연을 보며 느끼는 감정들이, 즉석으로 색을 이용해 무대 배경으로 표현되어, 공연의 기획이나 의도가 확실한 공연에 있어 프로그램에 가장 효과가 좋은 리스트를 수집 할 수 있음 (곡 구성 등)

- 관객의 감정을 파악하여 관객의 호응 유도 효과를 기대할 수 있음

- 관객의 호응과 공연 내용을 결합해 새로운 퍼포먼스를 기획, 제공할 수 있음

# 참고문헌
- Joseph Redmon, You Only Look Once: Unified, Real-Time Object Detection, 2016

- ultralytics, yolov5, 2020

- WongKinYiu, yolov7, 2022

- DJango document

- DjangoRestFramework with python


