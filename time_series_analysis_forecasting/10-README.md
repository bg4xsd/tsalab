11- chaotic attractor reconstruction is cited from
     https://node99.org/tutorials/ar/
     https://blog.csdn.net/weixin_45278115/article/details/120200065 
     https://physics.emory.edu/faculty/weeks/research/tseries4.html
     
                            https://resteche.github.io/REsteche_blog/chaos%20theory/butterfly%20effect/python%20animation/2021/10/20/Lorenz_animation.html    
     
     
     
比较好用的Python库（混沌，时间序列分析相关的）

## nolds 0.5.2， pip install nolds

Nolds is a small numpy-based library that provides an implementation and a learning resource for nonlinear measures for dynamical systems based on one-dimensional time series. Currently the following measures are implemented:

sample entropy (sampen)
Measures the complexity of a time-series, based on approximate entropy

correlation dimension (corr_dim)
A measure of the fractal dimension of a time series which is also related to complexity.

Lyapunov exponent (lyap_r, lyap_e)
Positive Lyapunov exponents indicate chaos and unpredictability. Nolds provides the algorithm of Rosenstein et al. (lyap_r) to estimate the largest Lyapunov exponent and the algorithm of Eckmann et al. (lyap_e) to estimate the whole spectrum of Lyapunov exponents.

Hurst exponent (hurst_rs)
The hurst exponent is a measure of the “long-term memory” of a time series. It can be used to determine whether the time series is more, less, or equally likely to increase if it has increased in previous steps. This property makes the Hurst exponent especially interesting for the analysis of stock data.

detrended fluctuation analysis (DFA) (dfa)
DFA measures the Hurst parameter H, which is very similar to the Hurst exponent. The main difference is that DFA can be used for non-stationary processes (whose mean and/or variance change over time).


## pynamical 0.3.2  pip install pynamical==0.3.2

pynamical is a Python package for modeling, simulating, visualizing, and animating discrete nonlinear dynamical systems and chaos. pynamical uses pandas, numpy, and numba for fast simulation, and matplotlib for beautiful visualizations and animations to explore system behavior. Compatible with Python 2 and 3. See the examples and demos on GitHub.
目前看这个函数库主要是对Map类型的混沌系统进行处理

## pyunicorn 0.6.1 pip install pyunicorn
                   conda install -c conda-forge python-unicorn
Advanced statistical analysis and modeling of general and spatially embedded complex networks with applications to multivariate nonlinear time series analysis。
pyunicorn (Unified Complex Network and RecurreNce analysis toolbox) is a fully object-oriented Python package for the advanced analysis and modeling of complex networks. Above the standard measures of complex network theory such as degree, betweenness and clustering coefficient it provides some uncommon but interesting statistics like Newman’s random walk betweenness. pyunicorn features novel node-weighted (node splitting invariant) network statistics as well as measures designed for analyzing networks of interacting/interdependent networks.

Moreover, pyunicorn allows to easily construct networks from uni- and multivariate time series and event data (functional (climate) networks and recurrence networks). This involves linear and nonlinear measures of time series analysis for constructing functional networks from multivariate data (e.g. Pearson correlation, mutual information, event synchronization and event coincidence analysis). pyunicorn also features modern techniques of nonlinear analysis of single and pairs of time series such as recurrence quantification analysis (RQA), recurrence network analysis and visibility graphs.

## PyRQA 8.0.0 pip install PyRQA

Highlights
Perform recurrence analysis on long time series in a time efficient manner using the OpenCL framework.

Conduct recurrence quantification analysis (RQA) and cross recurrence quantification analysis (CRQA).

Compute recurrence plots (RP) and cross recurrence plots (CRP).

Compute unthresholded recurrence plots (URP) and unthresholded cross recurrence plots (UCRP).

Conduct joint recurrence quantification analysis (JRQA) and compute joint recurrence plots (JRP).

Employ the euclidean, maximum or taxicab metric for determining state similarity.

Choose the fixed radius or radius corridor neighbourhood condition.

Use univariate time series or pre-embedded time series as input data.

Select either the half, single or double floating point precision for conducting the analytical computations.

Leverage machine learning techniques that automatically choose the fastest from a set of implementations.

Apply the computing capabilities of GPUs, CPUs and other platforms that support OpenCL.

Use multiple computing devices of the same or different type in parallel.

## pyts: pip install pyts
a Python package for time series classification
pyts is a Python package for time series classification. It aims to make time series classification easily accessible by providing preprocessing and utility tools, and implementations of state-of-the-art algorithms. Most of these algorithms transform time series, thus pyts provides several tools to perform these transformations.

## chaospy 4.3.12  pip install chaospy   # 不确定度量化的数值工具，没用！
Chaospy is a numerical toolbox for performing uncertainty quantification using polynomial chaos expansions, advanced Monte Carlo methods implemented in Python. It also include a full suite of tools for doing low-discrepancy sampling, quadrature creation, polynomial manipulations, and a lot more.

The philosophy behind chaospy is not to be a single tool that solves every uncertainty quantification problem, but instead be a specific tools to aid to let the user solve problems themselves. This includes both well established problems, but also to be a foundry for experimenting with new problems, that are not so well established. To do this, emphasis is put on the following:

## hundun 0.1.38  pip install hundun
https://github.com/llbxg/hundun/wiki
感觉这个包就够用了


# 其它时间序列分析相关的库
AutoTS
顾名思义，它是一个用于自动时间序列分析的 Python 库。 AutoTS 允许我们用一行代码训练多个时间序列模型，以便我们可以选择最适合的模型。该库是 autoML 的一部分，其目标是为初学者提供自动化库。autoML 可以去看看，里面还有个 H2O很不错。

Prophet
Prophet 是由 Facebook 的数据科学团队开发的用于解决时间序列相关问题的优秀库，可以使用在 R 和 Python 中。这对于处理具有强烈季节性影响的时间序列（如购买行为或销售预测）特别有用。 此外，它可以很好地处理杂乱的数据，无需任何手动操作。

Darts
Darts 是由 http://Unit8.co 开发的用于预测时间序列，并且对scikit-learn 友好 的Python 包。 它包含大量模型，从 ARIMA 到深度神经网络，用于处理与日期和时间相关的数据。该库的好处在于它还支持用于处理神经网络的多维类。它还允许用户结合来自多个模型和外部回归模型的预测，从而更容易地对模型进行回测。

Pyflux
Pyflux 是一个为 Python 构建的开源时间序列库。 Pyflux选择了更多的概率方法来解决时间序列问题。这种方法对于需要更完整的不确定性的预测这样的任务特别有利。用户可以建立一个概率模型，其中通过联合概率将数据和潜在变量视为随机变量。

Sktime
Sktime是一个Python库，它带有时间序列算法和工具，与scikit-learn兼容。它还具有分类模型、回归模型和时间序列预测模型。这个库的主要目标是制作可以与scikit-learn互操作。

tsfresh

atspy


kats





# R

CRAN packages: tseriesChaos, nonlinearTseries, fNonlinear, DChaos, highfrequency, nnet
https://www.pks.mpg.de/tisean//
https://www.pks.mpg.de/tisean//Tisean_3.0.1/index.html

tseriesChaos: Analysis of Nonlinear Time Series
Routines for the analysis of nonlinear time series. This work is largely inspired by the TISEAN project, by Rainer Hegger, Holger Kantz and Thomas Schreiber: <http://www.mpipks-dresden.mpg.de/~tisean/>.

fNonlinear: Rmetrics - Nonlinear and Chaotic Time Series Modelling
Provides a collection of functions for testing various aspects of univariate time series including independence and neglected nonlinearities. Further provides functions to investigate the chaotic behavior of time series processes and to simulate different types of chaotic time series maps.

nonlinearTseries: Nonlinear Time Series Analysis
https://cran.r-project.org/web/packages/nonlinearTseries/vignettes/nonlinearTseries_quickstart.html
Functions for nonlinear time series analysis. This package permits the computation of the most-used nonlinear statistics/algorithms including generalized correlation dimension, information dimension, largest Lyapunov exponent, sample entropy and Recurrence Quantification Analysis (RQA), among others. Basic routines for surrogate data testing are also included. Part of this work was based on the book "Nonlinear time series analysis" by Holger Kantz and Thomas Schreiber (ISBN: 9780521529020).

DChaos: Chaotic Time Series Analysis
Chaos theory has been hailed as a revolution of thoughts and attracting ever increasing attention of many scientists from diverse disciplines. Chaotic systems are nonlinear deterministic dynamic systems which can behave like an erratic and apparently random motion. A relevant field inside chaos theory and nonlinear time series analysis is the detection of a chaotic behaviour from empirical time series data. One of the main features of chaos is the well known initial value sensitivity property. Methods and techniques related to test the hypothesis of chaos try to quantify the initial value sensitive property estimating the Lyapunov exponents. The DChaos package provides different useful tools and efficient algorithms which test robustly the hypothesis of chaos based on the Lyapunov exponent in order to know if the data generating process behind time series behave chaotically or not.