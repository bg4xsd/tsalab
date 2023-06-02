# 时间序列分析实验室 tsalab


# DA310  Env：

pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/

pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

pip config set global.index-url https://mirrors.cloud.tencent.com/pypi/simple

## 基础安装

pip install scipy numpy matplotlib pandas  ipython scikit-learn statsmodels patsy seaborn beautifulsoup4 simplejson bokeh psutil  pylint flake8 yapf autopep8 black requests lxml astropy scikit-learn-intelex ipykernel plotly pyecharts

## 音频相关安装

pip install librosa==0.8.1 pip install soundfile # 因为最新版有很多变化，只能用老的配合课件

pip install PyWavelets  # for the wavelet tool

安装 pyaudio会麻烦些
(1) Linux
sudo apt-get install ffmpeg

sudo apt-get install libsndfile1

sudo apt-get install gstreamer1.0-plugins-base gstreamer1.0-plugins-ugly

sudo apt-get install  libportaudio2 portaudio19-dev

pip install pyaudio

(2) Winodws
python -m pip install pygobject

## 时间序列

 pip install nolds pynamical PyRQA pyts hundun
 
 pip install  AutoTS Sktime tsfresh

 按照要求，先装torch， 再装fastai, 最后 tsai

 pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

 pip install fastai

 pip install tsai

 pip install -U Prophet -i https://pypi.org/simple

 ### add 2023.06.01 概率时间
 conda install -c conda-forge pymc # for windows

 conda install -c conda-forge gluonts # for windows, need mxnet with vs c++ compiler

 For Linux, it works well.
 
 pip install pytensor pymc mxnet -i https://mirrors.cloud.tencent.com/pypi/simple

## FASTAI 相关资料需要安装 (建议fastai的相关学习到GPU服务器上)

pip install fastbook

   2022年最后更新， 支持python3.8，

  会造成 jupyterlab-widgets， widgetsnbextension， ipywidgets  降级， 如果有需要，注意单独安装其环境

pip install -U duckduckgo_search

   一直在更新，支持python3.11

 ## 可怜存储太少

pip cache purge

conda clean --all


![Image](./images/bfcat.png)

![Image](./images/bfcat.png?raw=true)

![Image](./images/bfcat.png)