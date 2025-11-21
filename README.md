# TSM (Temporal Shift Module) Training Project

이 프로젝트는 **Something-Something V2** 데이터셋을 사용하여 **TSM (ResNet50 Backbone)** 모델을 학습시키기 위한 코드 및 수정 사항을 포함하고 있습니다.

## 🚀 실행 방법 (Usage)

학습을 시작하려면 아래 명령어를 실행하세요.

```bash
python temporal-shift-module/main.py somethingv2 RGB \
    --arch resnet50 --num_segments 8 --gd 20 --lr 0.001 --lr_steps 20 40 \
    --epochs 2 --batch-size 4 -j 4 --dropout 0.5 --consensus_type=avg \
    --eval-freq=1 --shift --shift_div=8 --shift_place=blockres --npb
```

### 원본에서 수정한 항목

- [ops/dataset_config.py](ops/dataset_config.py): 루트 경로만 수정
- [ops/utils.py](ops/utils.py#L39): 39번째 줄 간단한 오류 수정
- [ssd/](ssd/): 하위 폴더 전체 컨텐츠 생성
- [tools/vid2img_sthv2.py](tools/vid2img_sthv2.py): 전체적으로 오류 수정

## [로그 데이터](log.csv)

```
Epoch: [0][0/5], lr: 0.00100	Time 21.956 (21.956)	Data 5.845 (5.845)	Loss 5.1544 (5.1544)	Prec@1 0.000 (0.000)	Prec@5 0.000 (0.000)
Test: [0/3]	Time 6.137 (6.137)	Loss 0.8891 (0.8891)	Prec@1 75.000 (75.000)	Prec@5 100.000 (100.000)
Testing Results: Prec@1 33.333 Prec@5 100.000 Loss 1.29828
Best Prec@1: 33.333

Epoch: [1][0/5], lr: 0.00100	Time 6.376 (6.376)	Data 5.808 (5.808)	Loss 0.9133 (0.9133)	Prec@1 50.000 (50.000)	Prec@5 100.000 (100.000)
Test: [0/3]	Time 6.174 (6.174)	Loss 2.2050 (2.2050)	Prec@1 0.000 (0.000)	Prec@5 100.000 (100.000)
Testing Results: Prec@1 33.333 Prec@5 100.000 Loss 1.51781
Best Prec@1: 33.333
```