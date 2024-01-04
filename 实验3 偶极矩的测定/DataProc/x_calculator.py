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


#转化为dataframe

C_0 = [
    [4.25, 4.25, 4.25, 4.25, 4.26, 4.25],
    [4.25, 4.25, 4.25, 4.25, 4.25, 4.26]
]
C_1 = [
    [7.02, 7.29, 7.46, 7.64, 7.78, 8.07],
    [7.02, 7.29, 7.46, 7.64, 7.79, 8.07]
]

bar_C_0 = [sum(i)/len(i) for i in zip(*C_0)]
bar_C_1 = [sum(i)/len(i) for i in zip(*C_1)]

def cal_epsilon(C_air, C_sample):
    result = (C_sample - C_D)/(C_air - C_D)
    return round(result, 2)

epsilon_0 = [cal_epsilon(C_air, C_sample) for C_air, C_sample in zip(bar_C_0, bar_C_1)]

# 将x_list, C_0, bar_C_0, C_1, bar_C_1, epsilon_0转化为dataframe
data = {
    '$x$': [0.00] + x_list,
    '$C_{\\text{air},1}/\\mathrm{pF}$': C_0[0],
    '$C_{\\text{sample},1}/\\mathrm{pF}$': C_1[0],
    '$C_{\\text{air},2}/\\mathrm{pF}$': C_0[1],
    '$C_{\\text{sample},2}/\\mathrm{pF}$': C_1[1],
    '$\\bar{C}_{\\text{air}}/\\mathrm{pF}$': bar_C_0,
    '$\\bar{C}_{\\text{sample}}/\\mathrm{pF}$': bar_C_1,
    '$\\varepsilon$': epsilon_0
}

df = pd.DataFrame(data)
print(df)
df.to_latex('datas2.tex', index=False)

data2 = {
    'x':  x_list,
    'epsilon': epsilon_0[1:]
}

df2 = pd.DataFrame(data2)
df2.to_csv('datas2.csv', index=False)

x = df2['x']
y = df2['epsilon']

m, c = np.polyfit(x, y, 1)

print(m, c)

plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, m*x + c, 'r', label='Fitted line')
plt.legend()
plt.savefig('epsilon.png')
plt.show()



    