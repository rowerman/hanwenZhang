# GAN使用说明:

本文件与代码历次更新时间:

* 2023/5/10/18:18 by ZYN
    需更新内容:缺少训练过程结果图形化展示功能

## 初始化:

1. 按照`requirement.txt`安装所需要的库
    方法:
    > pip install -r requirements.txt

2. 请安装`pytorch_gpu`文件夹里面的三个包(如果仅仅做测试请跳过)
    方法:
    1. > cd pytorch_gpu
    2. > pip install .\torch-1.13.1+cu117-cp310-cp310-win_amd64.whl
    3. > pip install .\torchaudio-0.13.1+cu117-cp310-cp310-win_amd64.whl
    4. > pip install .\torchvision-0.14.1+cu117-cp310-cp310-win_amd64.whl
   
3. 请运行`initialize.py`
    方法:
    > python initialize.py 

## 运行&训练

4. 如果想要测试请使用经过训练的示例网络
    方法:
    > python api.py

5. 如果想要更改测试网络的手写数字输出请打开api.py并修改`epoch`和`iters`两个参数,依次分别为model文件名的两个参数,其中`model_-1_-1`为默认示例网络
    
6. 如果想要从头训练网络请运行`train.py`
    方法:
    > python train.py

## 文件作用说明:
    * 每250个iters会输出一张结果演示图在`pictue_output`文件夹里
    * 每次得到更优网络会保存在`model`文件夹里
    * 模型类文件在`model.py`里面
    * 数据载入文件在`makeData.py`里面


本文件及本套代码作者:张奕宁 Zhang.Y.N@sjtu.edu.cn

