import numpy as np
import re



data = r'''4087 +- 38
4061 +- 38
4033 +- 37
3922 +- 36
3853 +- 35
3733 +- 34'''

# 将data的每行分别提取出来，第一个数记为Q, 第二个数记为EQ

data_list = []
for line in data.split('\n'):
    Q, EQ = re.findall(r'(\d+) \+- (\d+)', line)[0]
    data_list.append((int(Q), int(EQ)))

# 将data_list的每个元素的第一个数累计相加，第二个数取累计的根号平方和

data_new_list = []
Q_sum = 0
EQ2_sum = 0
for line in data_list:
    Q_sum += line[0]
    EQ2_sum += line[1] ** 2
    data_new_list.append((Q_sum, np.sqrt(EQ2_sum)))

# 将data_new_list每个line转化回最初的格式

data_new = ''
for line in data_new_list:
    data_new += f'{line[0]} $\\pm$ {line[1]:.0f} & \n'

print(data_new)