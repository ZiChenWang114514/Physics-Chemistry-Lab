def Q_S(n_0):
    a = 46853.16731
    b = -257711.43377
    return a + b / n_0

def Q_DD(n_0):
    return 257711 * (n_0 ** -2)

def Q_DS(n_0):
    return 46853 + (-515422 * (n_0 ** -1))

n_0_list = [200, 150, 100, 80, 50]
Q_list = []

class Q:
    def __init__(self):
        self.n_0 = 0.
        self.Qs = 0.
        self.Qdd = 0.
        self.Qds = 0.
        self.Qd = 0.

    def to_latex(self):
        self.Qs = to_latex_num(self.Qs)
        self.Qdd = to_latex_num(self.Qdd)
        self.Qds = to_latex_num(self.Qds)
        self.Qd = to_latex_num(self.Qd)

    def print_latex(self):
        q.to_latex()
        print(f"{self.n_0} & {self.Qs} & {self.Qdd} & {self.Qds} & {self.Qd} \\\\")

for n_0 in n_0_list:
    q = Q()
    q.n_0 = n_0
    q.Qs = Q_S(n_0)
    q.Qdd = Q_DD(n_0)
    q.Qds = Q_DS(n_0)
    index = n_0_list.index(n_0)
    if index:
        q.Qd = q.Qs - Q_list[index - 1].Qs
    Q_list.append(q)

def to_latex_num(num):
    # 转化为latex的科学计数法)
    if abs(num) < 100:
        if num < 10 :
            num = f"{float(num):.2f}"
        else:
            num = f"{float(num):.1f}"
    else:
        num = f"{num:.2e}"
        num = num.split('e')
        num = f"${float(num[0]):.2f} \\times 10^{{{int(num[1])}}}$"
    return num



    


for q in Q_list:
    q.print_latex()
