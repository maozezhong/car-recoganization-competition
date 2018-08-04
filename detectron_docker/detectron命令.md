### 注意，permisision问题得加sudo
1. docker安装：https://blog.csdn.net/yyh272/article/details/77389064
2. nvidia-docker安装：https://github.com/NVIDIA/nvidia-docker

### 通过docker images编译caffe
docker pull caffe2ai/caffe2
nvidia-docker run -it caffe2ai/caffe2:latest python -m caffe2.python.operator_test.relu_op_test
nvidia-docker run -it caffe2ai/caffe2:latest /bin/bash

//### clone cocoapi


### clone detectron
git clone https://github.com/facebookresearch/detectron $DETECTRON
pip install -r $DETECTRON/requirements.txt

### 通过docker images编译detectron
cd $DETECTRON/docker
docker build -t detectron:c2-cuda9-cudnn7 .
sudo nvidia-docker run --rm -it detectron:c2-cuda9-cudnn7 python2 detectron/tests/test_batch_permutation_op.py

### inference
sudo nvidia-docker run --rm -it detectron:c2-cuda9-cudnn7 python2 tools/infer_simple.py \
    --cfg configs/12_2017_baselines/e2e_mask_rcnn_R-101-FPN_2x.yaml \
    --output-dir /tmp/detectron-visualizations \
    --image-ext jpg \
    --wts https://s3-us-west-2.amazonaws.com/detectron/35861858/12_2017_baselines/e2e_mask_rcnn_R-101-FPN_2x.yaml.02_32_51.SgT4y1cO/output/train/coco_2014_train:coco_2014_valminusminival/generalized_rcnn/model_final.pkl \
    demo

### 进入docker
- 进入bash同时将文件夹挂载到mnt文件夹下:  sudo nvidia-docker run -it -v /home/maozezhong/Desktop/docker_detectron:/mnt detectron:c2-cuda9-cudnn7 /bin/bash

- 可视化方式进入bash: sudo nvidia-docker run -it -v /tmp/.X11-unix:/tmp/.X11-unix -v /home/maozezhong/Desktop/docker_detectron:/mnt -e DISPLAY=unix$DISPLAY -e GDK_SCALE -e GDK_DPI_SCALE detectron:c2-cuda9-cudnn7 /bin/bash

### 先运行这两个命令
ln -s /mnt/coco /detectron/detectron/datasets/data/coco
cp /mnt/dummy_datasets.py /detectron/detectron/datasets/dummy_datasets.py
cp /mnt/config.py /detectron/detectron/core/config.py
pip install pandas

### 训练
- fpn resnext101_64: 
python2 tools/train_net.py \
    --cfg /mnt/configs/12_2017_baselines\ /e2e_faster_rcnn_X-101-64x4d-FPN_1x.yaml \
    OUTPUT_DIR /mnt/output

- fpn resnext101_32: 
python2 tools/train_net.py \
    --cfg /mnt/configs/12_2017_baselines\ /e2e_faster_rcnn_X-101-32x8d-FPN_1x.yaml \
    OUTPUT_DIR /mnt/output

- fpn resnet101: 
python2 tools/train_net.py \
    --cfg /mnt/configs/12_2017_baselines\ /e2e_faster_rcnn_R-101-FPN_1x.yaml \
    OUTPUT_DIR /mnt/output

- fpn resnet50: 
python2 tools/train_net.py \
    --cfg /mnt/configs/12_2017_baselines\ /e2e_faster_rcnn_R-50-FPN_1x.yaml \
    OUTPUT_DIR /mnt/output

### test
- python2 predict.py --cfg /mnt/configs/12_2017_baselines\ /e2e_faster_rcnn_X-101-64x4d-FPN_1x.yaml --wts /mnt/output/train/coco_2014_train/generalized_rcnn/model_iter33999.pkl /mnt/coco/test
