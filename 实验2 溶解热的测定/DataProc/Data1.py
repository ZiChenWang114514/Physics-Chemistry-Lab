import numpy as np
import pandas as pd
import re

# Latex code

LatexCode = r"""
\\begin{align*}
\\text{Loop2-1-Line1} & : Er_{slope} = 0.120 \\times 10^{-5}, Er_{intercept} = 0.829 \\times 10^{-4} \\
\\text{Loop2-1-Line2} & : Er_{slope} = 0.021 \\times 10^{-4}, Er_{intercept} = 0.0006 \\
\\text{Loop2-1-Line3} & : Er_{slope} = 0.016 \\times 10^{-4}, Er_{intercept} = 0.0014 \\
\\text{Loop2-2-Line1} & : Er_{slope} = 0.009 \\times 10^{-4}, Er_{intercept} = 0.069 \\times 10^{-3} \\
\\text{Loop2-2-Line2} & : Er_{slope} = 0.027 \\times 10^{-4}, Er_{intercept} = 0.0009 \\
\\text{Loop2-2-Line3} & : Er_{slope} = 0.015 \\times 10^{-4}, Er_{intercept} = 0.0014 \\
\\text{Loop2-3-Line1} & : Er_{slope} = 0.009 \\times 10^{-4}, Er_{intercept} = 0.788 \\times 10^{-4} \\
\\text{Loop2-3-Line2} & : Er_{slope} = 0.010 \\times 10^{-4}, Er_{intercept} = 0.0004 \\
\\text{Loop2-3-Line3} & : Er_{slope} = 0.021 \\times 10^{-4}, Er_{intercept} = 0.0020 \\
\\text{Loop2-4-Line1} & : Er_{slope} = 0.011 \\times 10^{-4}, Er_{intercept} = 0.075 \\times 10^{-3} \\
\\text{Loop2-4-Line2} & : Er_{slope} = 0.009 \\times 10^{-4}, Er_{intercept} = 0.0003 \\
\\text{Loop2-4-Line3} & : Er_{slope} = 0.015 \\times 10^{-4}, Er_{intercept} = 0.0014 \\
\\text{Loop2-5-Line1} & : Er_{slope} = 0.010 \\times 10^{-4}, Er_{intercept} = 0.819 \\times 10^{-4} \\
\\text{Loop2-5-Line2} & : Er_{slope} = 0.009 \\times 10^{-4}, Er_{intercept} = 0.0003 \\
\\text{Loop2-5-Line3} & : Er_{slope} = 0.016 \\times 10^{-4}, Er_{intercept} = 0.0015 \\
\\text{Loop2-6-Line1} & : Er_{slope} = 0.008 \\times 10^{-4}, Er_{intercept} = 0.076 \\times 10^{-3} \\
\\text{Loop2-6-Line2} & : Er_{slope} = 0.007 \\times 10^{-4}, Er_{intercept} = 0.0003 \\
\\text{Loop2-6-Line3} & : Er_{slope} = 0.009 \\times 10^{-4}, Er_{intercept} = 0.0010 \\
\\end{align*}
"""

CSVCode = r"""
Loop2-1,143.91,522.99
Loop2-2,158.98,526.41
Loop2-3,170.16,654.39
Loop2-4,149.29,546.43
Loop2-5,174.17,600.47
Loop2-6,181.37,587.16
"""

# Data Processing
# 将以上数据转换为DataFrame格式，方便后续处理，提取出每组的Er_{slope}与Er_{intercept}

matches2 = re.findall(r'(Loop\d+-\d+),([\d.]+),([\d.]+)', CSVCode)


# 你现在可以使用data_list中的每一个对象了

class LinerFittingData:
    def __init__(self, name=None, slope=None, intercept=None):
        self.name = name
        self.slope = slope
        self.intercept = intercept
        
    @property
    def init_name(self):
        return self.name[:-6]
    
    def __repr__(self):
        return f"{self.init_name}, {self.name}, {self.slope}, {self.intercept}"

data_list = [
    LinerFittingData("Loop2-1-Line1", 0.120e-5, 0.829e-4),
    LinerFittingData("Loop2-1-Line2", 0.021e-4, 0.0006),
    LinerFittingData("Loop2-1-Line3", 0.016e-4, 0.0014),
    LinerFittingData("Loop2-2-Line1", 0.009e-4, 0.069e-3),
    LinerFittingData("Loop2-2-Line2", 0.027e-4, 0.0009),
    LinerFittingData("Loop2-2-Line3", 0.015e-4, 0.0014),
    LinerFittingData("Loop2-3-Line1", 0.009e-4, 0.788e-4),
    LinerFittingData("Loop2-3-Line2", 0.010e-4, 0.0004),
    LinerFittingData("Loop2-3-Line3", 0.021e-4, 0.0020),
    LinerFittingData("Loop2-4-Line1", 0.011e-4, 0.075e-3),
    LinerFittingData("Loop2-4-Line2", 0.009e-4, 0.0003),
    LinerFittingData("Loop2-4-Line3", 0.015e-4, 0.0014),
    LinerFittingData("Loop2-5-Line1", 0.010e-4, 0.819e-4),
    LinerFittingData("Loop2-5-Line2", 0.009e-4, 0.0003),
    LinerFittingData("Loop2-5-Line3", 0.016e-4, 0.0015),
    LinerFittingData("Loop2-6-Line1", 0.008e-4, 0.076e-3),
    LinerFittingData("Loop2-6-Line2", 0.007e-4, 0.0003),
    LinerFittingData("Loop2-6-Line3", 0.009e-4, 0.0010)
]

class ReynoldsTime:
    def __init__(self):
        self.name = None
        self.t_a = None
        self.t_b = None

    def __eq__(self, other: LinerFittingData):
        return self.name == other.init_name
    
    def __repr__(self):
        return f"{self.name}, {self.t_a}, {self.t_b}"


RT_list = []



for match in matches2:
    RT = ReynoldsTime()
    RT.name = match[0]
    RT.t_a = float(match[1])
    RT.t_b = float(match[2])
    RT_list.append(RT)

for LFD in data_list:
    print(LFD)

for RT in RT_list:
    print(RT)


# 定义一个新的类来存储计算结果
class CalculationResult:
    def __init__(self):
        self.name = None
        self.T1 = None
        self.T2 = None
        self.T2p = None
        self.T1p = None
    
    def __repr__(self):
        return f"{self.name} & {self.T1} & {self.T2} & {self.T2p} & {self.T1p} \\\\"
    __str__ = __repr__

    #如何print一个对象，就是__repr__的作用，例如

class CalculationMinus:
    def __init__(self):
        self.name = None
        self.dT1 = None
        self.dT2 = None

    def __repr__(self):
        return f"{self.name} & {self.dT1} & {self.dT2} \\\\"

results_list = []
results_list_d = []

def errorcalculation(slope, intercept, t):
    return ((t * slope) ** 2 + intercept ** 2) ** 0.5

def errorcalculation2(err1, err2):
    return (err1 ** 2 + err2 ** 2) ** 0.5

def errorcalculation3(err1):
    e = 0.00005
    return (err1 ** 2 + e ** 2) ** 0.5

def ERR_CAL(slope1, inter1, x1,
            slope2, inter2, x2):
    a = errorcalculation(slope1, inter1, x1)
    b = errorcalculation(slope2, inter2, x2)
    a = errorcalculation3(a)
    b = errorcalculation3(b)
    dab = errorcalculation2(a, b)
    return float_to_latex(a), float_to_latex(b), float_to_latex(dab)



def float_to_latex(num, precision=2):
    s = "{:.{precision}e}".format(num, precision=precision)
    
    base, exponent = s.split("e")
    
    return r"${} \times 10^{{{}}}$".format(base, int(exponent))

# 对于RT_list中的每一个Loop2-n
for RT in RT_list:
    # 查找与其相对应的LinerFittingData条目
    corresponding_LFDs = list(filter(lambda x: x == RT, data_list))
    
    # 确保我们找到了对应的条目
    if len(corresponding_LFDs) == 3:
        calculation = CalculationResult()
        calculation_d = CalculationMinus()

        calculation.name = RT.name
        calculation_d.name = RT.name
        
        # 对于T_a与line1、line2的计算
        calculation.T1, calculation.T2, calculation_d.dT1 \
            = ERR_CAL(corresponding_LFDs[0].slope, corresponding_LFDs[0].intercept, RT.t_a,
                    corresponding_LFDs[1].slope, corresponding_LFDs[1].intercept, RT.t_a)

        # 对于T_b与line2、line3的计算
        calculation.T2p, calculation.T1p, calculation_d.dT2 \
            = ERR_CAL(corresponding_LFDs[1].slope, corresponding_LFDs[1].intercept, RT.t_b,
                    corresponding_LFDs[2].slope, corresponding_LFDs[2].intercept, RT.t_b)

        results_list.append(calculation)
        results_list_d.append(calculation_d)


for result in results_list_d:
    print(repr(result))

orig_T_a = [1.449, 1.433, 1.416, 1.401, 1.387, 1.373]
orig_T_b = [1.440, 1.352, 1.297, 1.305, 1.542, 1.333]

def Latex_to_float(s):
    s = s.replace("\\times", "")
    s = s.replace("$", "")
    s = s.replace("{", "")
    s = s.replace("}", "")
    s = s.replace(" ", "")
    s = s.replace("\\", "")
    s = s.replace("10", "")
    s = s.replace("^", "e")
    return float(s)

orig_error_list = []
# 将result中的CalculationMinus的两个数据分别于orig_T_a与orig_T_b结合，形如4062.0 +- 37.0，即dT1 +- orig_T_a, dT2 +- orig_T_b
for result, T_a, T_b in zip(results_list_d, orig_T_a, orig_T_b):
    orig_error = CalculationMinus() 
    orig_error.name = result.name
    orig_error.dT1 = f"{T_a} +- {Latex_to_float(result.dT1)}"
    orig_error.dT2 = f"{T_b} +- {Latex_to_float(result.dT2)}"
    orig_error_list.append(orig_error)

print()
for orig_error in orig_error_list:
    print(repr(orig_error))









