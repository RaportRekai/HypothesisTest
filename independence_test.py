from scipy.stats import chi2
from tabulate import tabulate


def independence_test():
    r = int(input("Enter the number of rows: "))
    c = int(input("Enter the number of columns: "))
    lvl = float(input("significance value: "))
    m = []
    for i in range(0, r):
        m.append([])
        for j in range(0, c):
            m[i].append(0)
    for i in range(0, r):
        temp_dat_2 = input(f"Enter row {i}: ")
        a_list = temp_dat_2.split()
        map_object = map(float, a_list)
        m[i] = list(map_object)
        m[i].append(sum(m[i]))
    m.append([])
    for i in range(0, c + 1):
        s = 0
        for j in range(0, r):
            s = s + m[j][i]
        m[r].append(s)
    print(tabulate(m))
    exp = []
    for i in range(0, r):
        exp.append([])
        for j in range(0, c):
            exp[i].append(m[i][c] * m[r][j] / m[r][c])
    print(tabulate(exp))
    chi = []
    s = 0
    for i in range(0, r):
        chi.append([])
        for j in range(0, c):
            ch = ((m[i][j] - exp[i][j]) ** 2) / exp[i][j]
            chi[i].append(ch)
            s = s + ch
    print(tabulate(chi))
    print(f"Chi2 theory = {chi2.isf(lvl, df=(r - 1) * (c - 1))}")
    print(f"Chi2 observed{s}")
    if chi2.isf(lvl, df=(r - 1) * (c - 1)) < s:
        print("The samples are dependent")
    else:
        print("The samples are independent")
