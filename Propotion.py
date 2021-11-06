from scipy.stats import norm
from checker import checker
def Propotion():
    n = int(input("Enter Sample Size: "))
    test_tail = int(input("Enter 1 for right tail test \nEnter 2 for left tail test \nEnter 3 for two sided test\n"))
    lvl = float(input("Enter the critical level"))
    p = float(input("Enter probability of success: "))
    Mean_theory = n*p
    if test_tail == 3:
        lvl = lvl / 2
    Z_t_theory = norm.isf(lvl, loc=0, scale=1)
    Var = ((n*p*(1-p))**0.5)
    Mean_observe = float(input("Enter the observed number of success for the data"))
    Z_t_observe = (Mean_observe - Mean_theory) /Var
    print("****************************************")
    checker(Z_t_observe, Z_t_theory, test_tail)
    print("****************************************")