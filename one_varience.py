from scipy.stats import chi2
from checker_chi_f import checker_chi_f

def one_varience():
    n = int(input("Enter Sample Size: "))
    test_tail = int(input("Enter 1 for right tail test \nEnter 2 for left tail test \nEnter 3 for two sided test\n"))
    lvl = float(input("Enter the critical level"))
    sig = float(input("Enter sigma = Null hypo: "))
    chi_theory = 0.0
    if test_tail == 3:
        chi_theory = chi2.isf(1 - (lvl / 2),df=n-1)
        chi_t_theory = chi2.isf(lvl/2,df=n-1)
    elif test_tail == 2:
        chi_t_theory = chi2.isf(1-lvl, df=n-1)
    else:
        chi_t_theory = chi2.isf(lvl, df=n-1)
    print(chi_t_theory)
    Var = float(input("Enter the Varience for the given Data"))
    chi_t_observe = (n - 1) * Var / sig
    print("****************************************")
    checker_chi_f(chi_t_observe, chi_t_theory,chi_theory,test_tail)
    print("****************************************")
