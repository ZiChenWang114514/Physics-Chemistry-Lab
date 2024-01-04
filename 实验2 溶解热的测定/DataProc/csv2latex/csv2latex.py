import pandas as pd
pd.set_option('display.max_rows', None)

N = 10

names_1 = [
    '20230928110411dissolutiondata.csv', 
    '20230928113253dissolutiondata.csv',
    '20230928115117dissolutiondata.csv',
    '20230928121156dissolutiondata-2.csv'
]

names_2 = [
    '20230928140130dissolutiondata.csv',
    '20230928141837dissolutiondata.csv',
    '20230928143546dissolutiondata.csv',
    '20230928145327dissolutiondata.csv',
    '20230928151030dissolutiondata.csv',
    '20230928153009dissolutiondata.csv'
]

paths = [
    'C:\\Users\\11234\\Desktop\\PCL\\实验2 溶解热的测定\\Loop1\\',
    'C:\\Users\\11234\\Desktop\\PCL\\实验2 溶解热的测定\\Loop2\\'
]

names = [
    names_1, names_2
]

def transfer(name):
    df = pd.read_csv(name)

    # 从第七行开始记录数据（行数从1开始）
    df2 = df.iloc[9:, :].copy()

    #将df[6:]均匀的分为三个部分

    data_len = df2.shape[0] -1
    aver_len = data_len // N
    remainder = data_len % N
    lens = [aver_len] * N
    for i in range(remainder):
        lens[i] += 1 if i < remainder else 0
    
    break_points = []
    for i in range(N):
        break_points.append(sum(lens[:i+1]))
    
    df3 = df2.iloc[1:, :].copy()
    
    data_list = []
    for i in range(N):
        data = df3.iloc[break_points[i]-lens[i]:break_points[i], :].copy()
        #change index
        data.index = range(data.shape[0])
        # print(data.shape[0], lens[i])
        data_list.append(data)
    
    #修改data_1, data_2, data_3的index

    df4 = pd.concat(data_list, axis=1)

    head = ['t/\\mathrm{s}', '\\Delta T/\\mathrm{K}']*N
    data_latex = df4.to_latex(header=head, index=False, escape=False)
    
    # print(df4.iloc[1, :])
    # print(data_latex[:200])

    with open(name[:-4] + '.txt', 'w') as f:
        f.write(data_latex)



for i in range(len(names_1)):
    transfer(paths[0] + names_1[i])
    print('transfer ' + names_1[i] + ' done')

for i in range(len(names_2)):
    transfer(paths[1] + names_2[i])
    print('transfer ' + names_2[i] + ' done')
