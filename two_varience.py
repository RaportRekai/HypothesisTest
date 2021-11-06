from scipy.stats import f
from checker_chi_f import checker_chi_f


def two_varience():
    n1 = int(input("Enter Sample Size 1: "))
    n2 = int(input("Enter Sample Size 2: "))
    test_tail = int(input("Enter 1 for right tail test \nEnter 2 for two sided test\n"))
    s1_var = float(input("Enter the varience of the first sample: "))
    s2_var = float(input("Enter the varience of the second sample: "))
    lvl = float(input("Enter the critical level: "))
    if test_tail == 2:
        f_theory = f.isf(lvl / 2, dfn=n1 - 1, dfd=n2 - 1)
    else:
        f_theory = f.isf(lvl, dfn=n1 - 1, dfd=n2 - 1)
    f_observed = max(s1_var, s2_var) / min(s1_var, s2_var)
    print("****************************************")
    print(f"observed f {f_observed}")
    print(f"theory f {f_theory}")
    if f_observed > f_theory:
        print("Reject Null Hypothesis")
    else:
        print("Accept Null Hypothesis")
    print("****************************************")
