# 打开csv文档 读取数据
import pandas as pd
import numpy as np

names = [
    [
        "20230928110411dissolutiondata.csv",
        "20230928113253dissolutiondata.csv",
        "20230928115117dissolutiondata.csv",
        "20230928121156dissolutiondata-2.csv"
    ],
    [
        "20230928140130dissolutiondata.csv",
        "20230928141837dissolutiondata.csv",
        "20230928143546dissolutiondata.csv",
        "20230928145327dissolutiondata.csv",
        "20230928151030dissolutiondata.csv",
        "20230928153009dissolutiondata.csv"
    ]
]

foldernames = [
    "Loop1", "Loop2"
]

R = 11.3

I = [
    [
        0.97, 1.16, 1.46, 1.46
    ],
    [
        1.26, 1.26, 1.26, 1.26, 1.26, 1.26
    ]
]
path = "C:\\Users\\11234\\Desktop\\PCL\\实验2 溶解热的测定"

datas = []
# 读取csv文件
for foldername in foldernames:
    for name in names[foldernames.index(foldername)]:
        data_dir = {"name": str, "start_time": float, "end_time": float, "time": float, "R": float, "electricity": float, "Q'": float}
        with open(path + "\\" + foldername + "\\" + name, "r") as f:
            data = pd.read_csv(f)
            # 读取第五行第二列、第六行第二列数据
            start_time = float(data.iloc[5, 1])
            end_time = float(data.iloc[6, 1])
            t = end_time - start_time
            electricity = I[foldernames.index(foldername)][names[foldernames.index(foldername)].index(name)]
            # 计算Q'
            Q = electricity**2 * t * R
            name = "Loop" + str(foldernames.index(foldername) + 1) + "-" + str(names[foldernames.index(foldername)].index(name) + 1)
            # 转化为形如的形式data_dir = {"start_time": float, "end_time": float, "time": float, "R": float, "electricity": float, "Q'": float}
            data_dir["name"] = name
            data_dir["start_time"] = start_time
            data_dir["end_time"] = end_time
            #保留三位小数
            data_dir["time"] = round(t, 3)
            data_dir["R"] = R
            data_dir["electricity"] = electricity
            #将Q转化为科学计数法，并保留两位小数
            q = "$" + "{:.2f}".format(Q/1000) + "\\times 10^{3}$"
            data_dir["Q'"] = q
            
            datas.append(data_dir)

# 将datas转化为Latex格式

# 生成表头
table_head = "实验序号 & $t_1/\mathrm{s}$ & $t_2/\mathrm{s}$ & $\Delta t/\mathrm{s}$ & $R/\mathrm{\Omega}$ & $I\/mathrm{A}$ & $Q^\prime/\mathrm{J}$"

# 生成表格内容
table_content = ""
for data in datas:
    table_content += str(data["name"]) + " & " + \
                        str(data["start_time"]) + " & " + \
                        str(data["end_time"]) + " & " + \
                        str(data["time"]) + " & " + \
                        str(data["R"]) + " & " + \
                        str(data["electricity"]) + " & " +\
                        str(data["Q'"]) + "\\\\\n"
            
# 生成表格

table = "\\begin{table}[!htp]\n\\centering\n\\caption{Q'的测定}\n\\begin{tabular}{ccccccc}\n\\toprule\n" + table_head + "\\\\\n\\midrule\n" + table_content + "\\bottomrule\n\\end{tabular}\n\\end{table}"         

print(table)
