### 比赛说明
- 参赛者需要通过已经打标的图片和对应的csv文件建立模型，识别图片中的各种大小汽车，然后将模型应用于测试集，以预测图片中车辆数目以及坐标
- [比赛地址](http://www.dcjingsai.com/common/cmpt/%E4%BA%A4%E9%80%9A%E5%8D%A1%E5%8F%A3%E8%BD%A6%E8%BE%86%E4%BF%A1%E6%81%AF%E7%B2%BE%E5%87%86%E8%AF%86%E5%88%AB_%E8%B5%9B%E4%BD%93%E4%B8%8E%E6%95%B0%E6%8D%AE.html)

### 数据处理
- 增加KITTI数据
- [同态滤波（针对黑夜情况）](https://blog.csdn.net/cjsh_123456/article/details/79351654)
- [cutout增强](https://arxiv.org/abs/1708.04552)

### 模型
- [faster-rcnn pytorch(在其基础上加了resnext和densenet backbone)](https://github.com/jwyang/faster-rcnn.pytorch)
- [retinanet keras](https://github.com/fizyr/keras-retinanet)
- [deformable conv network](https://github.com/msracver/Deformable-ConvNets)
- [detectron](https://github.com/facebookresearch/Detectron), detectron相关编译安装见detectron_docker文件夹中，我用的是docker安装

### 技巧
- nms, softnms
- cutout
- 模型融合

### 成绩
- 线上0.88, 30名

### 工程文件链接
- [faster-rcnn](https://pan.baidu.com/s/17cIPyji0NbCKrzCGyAhtJQ)
- [dcn](https://pan.baidu.com/s/1CBl1uybcQxeTwBPkyN0eqQ)
- [retinanet](https://pan.baidu.com/s/13rgBikry51jTVxb-cTOReg)
- [DataSets](https://pan.baidu.com/s/1LsehnN-h6ZSIkTK3wnW0Yg)

