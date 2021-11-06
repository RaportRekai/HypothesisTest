import statistics
from scipy.stats import norm,t
from checker import checker
def two_independent_small():
    n1 = int(input("Enter no.of Samples in sample1: "))
    n2 = int(input("Enter no.of Samples in sample2: "))
    test_tail = int(input("Enter 1 for right tail test \nEnter 2 for left tail test \nEnter 3 for two sided test\n"))
    critical_value = float(input("Enter the critical Value: "))
    diff_theory = float(input("theoretical value of sample differences: "))
    prompt = (input("Do you want to enter data Y/N (directs to T test): "))
    if test_tail == 3:
        critical_value = critical_value/2
    if prompt == "N":
        Z_theory = norm.isf(critical_value, loc = 0, scale = 1)
        s1_var = float(input("Enter varience of sample1: "))
        s2_var = float(input("Enter varience of sample2: "))
        s1_mean_observe = float(input("observed mean of smaple1: "))
        s2_mean_observe = float(input("observed mean of smaple2: "))
        Z_observed = ((s1_mean_observe-s2_mean_observe) - diff_theory)/((s1_var/n1 + s2_var/n2)**0.5)
        print("****************************************")
        checker(Z_observed, Z_theory, test_tail)
        print("****************************************")
    else:
        T_theory = t.isf(critical_value,(n1+n2-2))
        temp_dat_1 = input("Enter sample 1: ")
        a_list = temp_dat_1.split()
        map_object = map(float, a_list)
        s1_data = list(map_object)
        s1_var = statistics.variance(s1_data)
        s1_mean_observe = statistics.mean(s1_data)
        temp_dat_2 = input("Enter sample 2: ")
        a_list = temp_dat_2.split()
        map_object = map(float, a_list)
        s2_data = list(map_object)
        s2_var = statistics.variance(s2_data)
        s2_mean_observe = statistics.mean(s2_data)
        sigma = ((n1-1)*s1_var + (n2-1)*s2_var)/(n1+n2-2)
        t_observed = ((s1_mean_observe - s2_mean_observe) - diff_theory) / ((sigma*(1/n1+1/n2)) ** 0.5)
        print("****************************************")
        checker(t_observed, T_theory, test_tail)
        print("****************************************")

        # 707.0
        # 632.0
        # 604.0
        # 652.0
        # 669.0
        # 674.0
        #
        # 552.0
        # 554.0
        # 484.0
        # 630.0
        # 648.0
        # 610.0