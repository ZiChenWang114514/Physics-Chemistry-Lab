import pandas as pd
import sys

sys.path.append('C:\\Users\\11234\\Desktop\\PCL\\实验1 燃烧热的测定')
name_1 = '20230921121310combustiondata_adjusted.csv'
name_2 = '20230921142539dissolutiondata_adjusted.csv'
name_3 = '20230921154902combustiondata_adjusted_2_adjusted.csv'


def transfer(name):
    df = pd.read_csv(name)
    num_rows = df.shape[0]

    # 从第七行开始记录数据（行数从1开始）
    df2 = df.iloc[5:, :].copy()

    # 取出df2第一行第一列与第二列的数据，存为(time, temperature)
    time = df2.iloc[0, 0]
    temperature = df2.iloc[0, 1]

    #将df[6:]均匀的分为三个部分

    data_len = num_rows - 6
    aver_len = data_len // 7
    remainder = data_len % 7
    lens = [aver_len] * 7
    for i in range(remainder):
        lens[i] += 1 if i < remainder else 0
    
    df3 = df2.iloc[1:, :].copy()
    data_1 = df3.iloc[:lens[0], :].copy()
    data_2 = df3.iloc[lens[0]:lens[0]+lens[1], :].copy()
    data_3 = df3.iloc[lens[0]+lens[1]:lens[0]+lens[1]+lens[2], :].copy()
    data_4 = df3.iloc[lens[0]+lens[1]+lens[2]:lens[0]+lens[1]+lens[2]+lens[3], :].copy()
    data_5 = df3.iloc[lens[0]+lens[1]+lens[2]+lens[3]:lens[0]+lens[1]+lens[2]+lens[3]+lens[4], :].copy()
    data_6 = df3.iloc[lens[0]+lens[1]+lens[2]+lens[3]+lens[4]:lens[0]+lens[1]+lens[2]+lens[3]+lens[4]+lens[5], :].copy()
    data_7 = df3.iloc[lens[0]+lens[1]+lens[2]+lens[3]+lens[4]+lens[5]:, :].copy()

    
    #修改data_1, data_2, data_3的index
    data_1.index = range(lens[0])
    data_2.index = range(lens[1])
    data_3.index = range(lens[2])
    data_4.index = range(lens[3])
    data_5.index = range(lens[4])
    data_6.index = range(lens[5])

    df4 = pd.concat([data_1, data_2, data_3, data_4, data_5, data_6, data_7], axis=1)

    data_latex = df4.to_latex(header = [time, temperature]*7, index = False)
    
    with open(name[:-4] + '.txt', 'w') as f:
        f.write(data_latex)

transfer(name_1)
print('transfer(name_1) done')
transfer(name_2)
print('transfer(name_2) done')
transfer(name_3)
print('transfer(name_3) done')
