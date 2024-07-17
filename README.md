# PALCON 프로젝트

PALCON프로젝트는 객체탐지 로봇팔 프로젝트인 PAL 팀의 객체탐지 모듈입니다. YOLOv7 segmentation을 사용하여 객체를 탐지하고, 대상 타겟의 중심점을 계산합니다. 이 중심점의 이미지 분석을 통해 로봇팔이 어디를 쥐어야 하는지를 인식하고, 로봇팔은 해당 좌표로 이동하여 객체를 집게 됩니다.

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
- `res/fork-and-cup02.png`

## 요구사항

- Python 3.x
- 필요한 패키지는 `requirements.txt` 파일을 참고하여 설치하십시오.
  ```bash
  pip install -r requirements.txt
  ```

## 기여 방법

1. 이 저장소를 포크합니다.
2. 새로운 브랜치를 생성합니다.
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. 변경 사항을 커밋합니다.
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. 브랜치에 푸시합니다.
   ```bash
   git push origin feature/AmazingFeature
   ```
5. 풀 리퀘스트를 생성합니다.

## 라이센스

이 프로젝트는 MIT 라이센스를 따릅니다. 자세한 내용은 `LICENSE` 파일을 참고하십시오.
