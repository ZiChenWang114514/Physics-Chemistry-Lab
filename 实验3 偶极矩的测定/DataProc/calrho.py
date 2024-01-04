import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

C_D = 1.537

def x_cal(m_1, m_2):
    result = (m_1/74.12)/(m_1/74.12+m_2/84.16)
    # 保留三位小数
    return round(result, 3)

m_1_list = [0.552, 0.866, 1.114, 1.273, 1.644]

m_2_list = [11.229, 10.840, 10.565, 10.380, 10.205]

x_list = [x_cal(m_1, m_2) for m_1, m_2 in zip(m_1_list, m_2_list)]
x_list = [0.000] + x_list + [1.000]

rho_list = [
    [0.77835, 0.77418, 0.77463, 0.77510, 0.77534, 0.77596, 0.80571],
    [0.77836, 0.77418, 0.77462, 0.77512, 0.77533, 0.77594, 0.80572],
    [0.77835, 0.77418, 0.77462, 0.77512, 0.77533, 0.77595, 0.80572],
]

bar_rho = [round(sum(i)/len(i),5) for i in zip(*rho_list)]

datas1 = {
    'x': x_list,
    'rho_1': rho_list[0],
    'rho_2': rho_list[1],
    'rho_3': rho_list[2],
    'bar_rho': bar_rho
}

df = pd.DataFrame(datas1)
df.to_latex('datas.tex', index=False)

datas2 = {
    'x': x_list[1:-1],
    'rho': bar_rho[1:-1]
}

df2 = pd.DataFrame(datas2)
df2.to_csv('datas.csv', index=False)

# 线性拟合
x = np.array(x_list[1:-1])
y = np.array(bar_rho[1:-1])
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
print(p)
plt.plot(x, y, 'o', label='original data')
plt.plot(x, p(x), 'r--', label='fitting data')
plt.xlabel('x')
plt.ylabel('rho')
plt.legend()
plt.savefig('fitting.png')
plt.show()




