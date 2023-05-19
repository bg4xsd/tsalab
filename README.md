# tsalab

这个版本使用的是 GITEE 仓库

关于时间序列分析相关的研究

开发环境参照 DA310， 这里实际使用的是 python=3.9

## 基础环境：

pip install scipy numpy matplotlib pandas  ipython scikit-learn statsmodels patsy seaborn beautifulsoup4 simplejson bokeh psutil  pylint flake8 yapf autopep8 black requests lxml astropy scikit-learn-intelex ipykernel plotly -i https://mirrors.cloud.tencent.com/pypi/simple


## pip 默认源  -i https://pypi.org/simple


## 时间序列包
 pip install nolds pynamical PyRQA pyts hundun
 pip install  AutoTS Sktime tsfresh 
 
 pip install tsai # 会顺带安装 torch， fastai
 
 pip install Prophet # 这个包跟 tensorflow， tsai打架， 有需要单独安装一个环境
 pip install -U Prophet -i https://pypi.org/simple

 ## 神经网络， DA310里面按照需要选装
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 cpuonly -c pytorch
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.7 -c pytorch -c nvidia
pip install tensorflow 


## 可怜存储太少, 可以根据需要少装些
pip cache purge
