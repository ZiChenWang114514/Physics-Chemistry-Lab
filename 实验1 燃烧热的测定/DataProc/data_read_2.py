import pandas as pd

name = '20230921154902combustiondata_adjusted_2.csv'

def adjust(name):
    df = pd.read_csv(name)
    df2 = df.iloc[6:, :].copy()

    begin_time = float(df2.iloc[0, 0])
    begin_temp = float(df2.iloc[0, 1])

    df3 = df2.iloc[1:, :].copy()
    df3.index = range(df3.shape[0])

    for i in range(df3.shape[0]):
        #保留三位小数
        df3.iloc[i, 0] = str(f"{float(df3.iloc[i, 0]) - begin_time:.3f}")
        df3.iloc[i, 1] = str(f"{float(df3.iloc[i, 1]) - begin_temp:.3f}")

    df4 = pd.concat([df.iloc[:6, :], df3], axis=0)
    df4.to_csv(name[:-4] + '_adjusted.csv', index = False)

adjust(name)
print('adjust(name) done')


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
    aver_len = data_len // 5
    remainder = data_len % 5
    lens = [aver_len] * 5
    for i in range(remainder):
        lens[i] += 1 if i < remainder else 0
    
    df3 = df2.iloc[1:, :].copy()
    data_1 = df3.iloc[:lens[0], :].copy()
    data_2 = df3.iloc[lens[0]:lens[0]+lens[1], :].copy()
    data_3 = df3.iloc[lens[0]+lens[1]:lens[0]+lens[1]+lens[2], :].copy()
    data_4 = df3.iloc[lens[0]+lens[1]+lens[2]:lens[0]+lens[1]+lens[2]+lens[3], :].copy()
    data_5 = df3.iloc[lens[0]+lens[1]+lens[2]+lens[3]:, :].copy()

    
    #修改data_1, data_2, data_3的index
    data_1.index = range(lens[0])
    data_2.index = range(lens[1])
    data_3.index = range(lens[2])
    data_4.index = range(lens[3])
    data_5.index = range(lens[4])

    df4 = pd.concat([data_1, data_2, data_3, data_4, data_5], axis=1)

    data_latex = df4.to_latex(header = [time, temperature]*5, index = False)
    
    with open(name[:-4] + '.txt', 'w') as f:
        f.write(data_latex)


transfer(name[:-4] + '_adjusted.csv')
print('transfer(name_3[:-4] + _adjusted.csv) done')
