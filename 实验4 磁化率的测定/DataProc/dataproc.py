import pandas as pd
import numpy as np

 # 读取时以空格分割
data = pd.read_csv('data.csv', sep=' ')

# 提取出奇数行的数据
data2 = data.iloc[1::2, :].copy().reset_index(drop=True)

# 将data2中的数据从第二列开始减去第一列的数据，并保留四位小数
data2.iloc[:, 1:] = data2.iloc[:, 1:] - data2.iloc[:, 0].values.reshape(-1, 1)


# 将data2中的数据保留四位小数
data2 = data2.round(4)

chi_0 = 4.056 * 10 ** (-7)

# 0.01900 -0.0200 -0.0180 -0.0110
class Sample():
    def __init__(self, name, m, m3, m4, m31, m41):
        self.name = name
        self.m = m
        self.m3 = m3
        self.m4 = m4
        self.m31 = m31
        self.m41 = m41

# 将

# 将data2逐行转化为latex，保留四位小数，并保存

# 清除data2.tex中的内容
with open('data2.tex', 'w') as f:
    f.write('')
    f.write('\n')

for i in range(data2.shape[0]):
    # 不要使用tolatex
    latex = data2.iloc[i, :].to_string(header=False, index=False, float_format=lambda x: '%.4f' % x)
    # 转化为latex格式
    latex = latex.replace('\n', ' & ') + ' \\\\'
    with open('data2.tex', 'a') as f:
        f.write(latex)
        f.write('\n')
        
print(latex)

