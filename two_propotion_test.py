from scipy.stats import norm
from checker import checker


def two_propotion_test():
    n1 = int(input("Enter number of samples in sample1: "))
    n2 = int(input("Enter number of samples in sample2: "))
    succ1 = int(input("Enter the no. of success for sample1: "))
    succ2 = int(input("Enter the no. of success for sample2: "))
    lvl = float(input("Enter significance level: "))
    test_tail = float(input("Enter 1 for right tail test \nEnter 2 for left tail test \nEnter 3 for two sided test\n"))
    p1 = float(succ1 / n1)
    p2 = float(succ2 / n2)
    p = (succ2 + succ1) / (n1 + n2)
    z_observe = (p1 - p2) / ((p * (1 - p) * (1 / n1 + 1 / n2)) ** 0.5)
    z_theory = norm.isf(lvl)
    print(f"Z_theory = {z_theory}")
    checker(z_observe, z_theory, test_tail)
