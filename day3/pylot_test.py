import numpy as np
from matplotlib import pyplot as plt
import matplotlib
#绘制线性函数 点线图
def drawLinear():
# fname 为 你下载的字体库路径，注意 SimHei.ttf 字体的路径

    x = np.arange(1, 11,0.1)
    y =2*x+5
    plt.title("菜鸟教程 - 测试")

    # fontproperties 设置中文显示，fontsize 设置字体大小
    plt.xlabel("x 轴")
    plt.ylabel("y 轴")
    plt.plot(x, y,"m")
    plt.show()

#绘制1张图中多个子图
def drawSubplot():
    # 计算正弦和余弦曲线上的点的 x 和 y 坐标
    x = np.arange(0, 3 * np.pi, 0.1)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    # 建立 subplot 网格，高为 2，宽为 1
    # 激活第一个 subplot
    plt.subplot(2, 1, 1)
    # 绘制第一个图像
    plt.plot(x, y_sin)
    plt.title('Sine')
    # 将第二个 subplot 激活，并绘制第二个图像
    plt.subplot(2, 1, 2)
    plt.plot(x, y_cos)
    plt.title('Cosine')
    # 展示图像
    plt.show()

#绘制直方图
def drawBar():
    x=[6,9,12]
    y=[10,2,6]
    plt.bar(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

#频率分布图
def drawHistogram():
    x=np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
    plt.hist(x,bins=[0,20,40,60,80,100])
    plt.show()
plt.rcParams['font.sans-serif']=['FangSong']
drawHistogram()