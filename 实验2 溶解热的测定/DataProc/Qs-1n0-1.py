import pandas as pd

# 定义数据
data = {
    'n0': [310.7, 153.2, 100.8, 74.58, 58.87, 58.43],
    'Er_n0': [0.31, 0.15, 0.1, 0.075, 0.059, 0.048],
    'Qs': [45900, 45100, 44400, 43400, 42500, 41500],
    'Er_Qs': [430, 300, 240, 200, 170, 160]
}

# 创建DataFrame
df = pd.DataFrame(data)

# 转换n0, Qs为倒数
df['n0_inv'] = 1 / df['n0']
df['Qs_inv'] = 1 / df['Qs']

# 使用误差的传递公式来计算倒数的误差
df['Er_n0_inv'] = df['Er_n0'] / (df['n0']**2)
df['Er_Qs_inv'] = df['Er_Qs'] / (df['Qs']**2)

# 打印结果
print(df[['n0_inv', 'Er_n0_inv', 'Qs_inv', 'Er_Qs_inv']])


# 将index相同的数据转化为列表，并转化为科学计数法
data_list = df[['n0_inv', 'Er_n0_inv', 'Qs_inv', 'Er_Qs_inv']].values.tolist()
for i in range(len(data_list)):
    for j in range(len(data_list[i])):
        if j%2 == 0:
            data_list[i][j] = '%.3e' % data_list[i][j]
        else:
            data_list[i][j] = '%.1e' % data_list[i][j]


# 将n0_inv与Er_n0_inv结合，中间以\\pm分隔，使得两者数量级相同，例如 (100\pm10)e-3
def conbineer(x, er_x):
    str_x = str(x).split('e')
    str_er_x = str(er_x).split('e')
    er_x_num = round(float(str_er_x[0])*10**(int(str_er_x[1])-int(str_x[1])),10)
    return '$( ' + str_x[0] + ' \\pm ' + str(er_x_num) + ' ) \\times 10^{' + str_x[1][0] + str_x[1][-1] + '} $'

# 将数据转化为LaTeX表格行
for i in range(len(data_list)):
    latex_row = ''
    for j in [0, 2]:
        latex_row += conbineer(data_list[i][j], data_list[i][j+1])
        latex_row += ' & '
    latex_row = latex_row[:-2] + '\\\\'
    print(latex_row)
    
# 将dataframe格式的datalist转化为csv文件
df.to_csv('Qs-1n0-1.csv', index=False)








