# 📄 TSM (Temporal Shift Module) Pre-trained Model Test Report

본 보고서는 TSM 모델의 사전 학습된 가중치를 사용하여 Kinetics 데이터셋의 일부에 대한 테스트 및 검증 결과를 기록합니다.

---

## 1. ⚙️ Environment Setup

| 항목 | 상세 내용 |
| :--- | :--- |
| **개발 환경** | PyCharm 사용 |
| **저장소** | GitHub repository를 클론하여 사용 |
| **의존성** | 클론 후 가상 환경(Virtual Environment)에 `requirements` 파일의 의존성 설치 |
| **설정** | `ops/dataset_config.py` 파일에서 루트 디렉터리(root directory) 등의 환경 변수 수정 |

---

## 2. 🧠 Apply Pre-trained Model & Data Preprocessing

### 2.1. 모델 및 데이터 준비

* **Pre-trained Weights:** Kinetics (K400) 데이터셋으로 사전 학습된 가중치 사용.
    * `pretrained/TSM_kinetics_RGB_resnet50_avg_segment5_e50.pth`
* **Dataset Download:** Kinetics (K400) 데이터셋 다운로드.
    * 원본 저장소 링크: [https://github.com/cvdfoundation/kinetics-dataset](https://github.com/cvdfoundation/kinetics-dataset)

### 2.2. 데이터 전처리

* **프레임 이미지 변환:** `tools/vid2img_kinetics.py` 스크립트를 사용하여 동영상 파일 형태의 데이터를 **프레임 이미지 (Frame Image)** 형태로 전처리했습니다.
* **데이터 샘플링:** K400 데이터셋의 용량이 매우 크기 때문에, 전체 데이터 중 약 **1/6 수준의 샘플 데이터**만 사용하여 테스트를 진행했습니다.
* **Ground Truth 생성:** 모델의 클래스 예측(Validation)을 위해 사용된 샘플 데이터와 1:1 대응하는 **Ground Truth 파일**을 별도로 생성했습니다.

---

## 3. 🚀 Run Demo (Testing Script)

### 실행 스크립트

메모리 부족 문제로 인해 공식 제공 코드의 `batch_size`를 절반으로 줄여 테스트를 실행했습니다.

```bash
.venv) PS C:\Users\jdmdj\Desktop\temporal-shift-module> python .\test_models.py kinetics \
--weights=pretrained/TSM_kinetics_RGB_resnet50_avg_segment5_e50.pth \
--test_segments=8 --test_crops=1 --batch_size=32
