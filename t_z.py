#some slight modifications are required
import statistics
from scipy.stats import norm, t
from checker import checker
def t_z_calculate():
    n = int(input("Enter Sample Size: "))
    test_tail = int(input("Enter 1 for right tail test \nEnter 2 for left tail test \nEnter 3 for two sided test\n"))
    lvl = float(input("Enter the critical level"))
    mean_choice = input("Do you want to mention the data elements (directs to T Test) Y/N: ")
    Mean_theory = float(input("Enter u = Null hypo: "))
    if test_tail == 3:
        lvl = lvl/2
    if mean_choice == "N":
        Z_t_theory = norm.isf(lvl,loc=0,scale =1)
        Var = float(input("Enter the Varience for the given Data"))
        Mean_observe = float(input("Enter the mean for the data"))
        Z_t_observe = (Mean_observe - Mean_theory) / ((Var / n) ** 0.5)
        print("****************************************")
        checker(Z_t_observe, Z_t_theory, test_tail)
        print("****************************************")
    else:
        Z_t_theory = t.isf(lvl, n-1)
        temp_dat_1 = input("Enter sample data enter with decimal point : ")
        a_list = temp_dat_1.split()
        map_object = map(float, a_list)
        s1_data = list(map_object)
        print(s1_data)
        Mean_observe = statistics.mean(s1_data)
        Var = statistics.variance(s1_data)
        print("****************************************")
        print(f"The varience of the data is {Var}")
        Z_t_observe = (Mean_observe - Mean_theory) / ((Var / n) ** 0.5)
        checker(Z_t_observe, Z_t_theory, test_tail)
        print("****************************************")
