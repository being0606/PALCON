# PALCON 프로젝트

PALCON프로젝트는 객체탐지 로봇팔 프로젝트인 PAL 팀의 객체탐지 모듈입니다. YOLOv8n segmentation을 사용하여 객체를 탐지하고, 대상 타겟의 중심점을 계산합니다. 이 중심점의 이미지 분석을 통해 로봇팔이 어디를 쥐어야 하는지를 인식하고, 로봇팔은 해당 좌표로 이동하여 객체를 집게 됩니다.

<video width="600" controls>
  <source src="res/24LC110_PAL%204.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## 프로젝트 구조

- `src/main.py` : 메인 실행 파일입니다.
- `src/yolo7Seg-test.ipynb` : YOLOv7seg를 사용하여 데모를 실행하는 Jupyter Notebook 파일입니다.
- `src/segmaㅌntation.ipynb` : YOLOv7seg를 웹캠에 적용시켜 대상 이미지를 실시간으로 탐지하는 Jupyter Notebook 파일입니다.
- `src/segTracing.ipynb` : YOLOv7seg를 웹캠에 적용하여 특정 라벨(이 프로젝트에서는 포크와 접시 등 식기)만을 탐지하도록 수정한 Jupyter Notebook 파일입니다.

## 사용된 모델

이 프로젝트에서는 COCO 데이터셋을 사전 학습한 YOLOv7 모델을 사용합니다.

## 실행 방법

### 메인 파일 실행

1. `src/main.py` 파일을 실행하여 프로젝트를 시작합니다.
   ```bash
   python src/main.py
   ```

### Jupyter Notebook 사용

1. YOLOv7seg 데모 실행:
   - `src/yolo7Seg-test.ipynb` 파일을 Jupyter Notebook에서 열고 순서대로 셀을 실행합니다.
2. 실시간 대상 이미지 탐지:
   - `src/segmantation.ipynb` 파일을 Jupyter Notebook에서 열고 순서대로 셀을 실행하여 웹캠을 통해 실시간으로 이미지를 탐지합니다.
3. 특정 라벨 탐지:
   - `src/segTracing.ipynb` 파일을 Jupyter Notebook에서 열고 순서대로 셀을 실행하여 특정 라벨(포크와 접시 등 식기)만을 탐지합니다.

## 결과 이미지

깃허브 저장소에는 실행 결과 이미지가 포함되어 있습니다. 각 노트북 파일을 실행한 후 생성되는 결과 이미지를 참고하십시오.

- `res/fork-and-cup01.png`
  ![Image](/res/fork-and-cup01.png)
- `res/fork-and-cup02.png`
  ![Image](/res/fork-and-cup02.png)

## 결과 및 함의

이 프로젝트에서는 기존 바운딩 박스의 중심을 추적하는 Object Dectection모델에서 발생하는 문제를 해결했습니다. 이전에는 박스의 중심과 대상 객체의 중심이 서로 다른 경우가 있었는데, 우리는 이를 개선하여 대상체의 정확한 중심을 추적하였습니다. 이는 객체 탐지 및 로봇팔 제어에 있어서 더욱 정확하고 효과적인 결과를 도출할 수 있게 해줍니다.

## 라이센스

이 프로젝트는 MIT 라이센스를 따릅니다. 자세한 내용은 `LICENSE` 파일을 참고하십시오.
