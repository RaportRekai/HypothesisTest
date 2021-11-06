from scipy.stats import chi2
from checker_chi_f import checker_chi_f
from tabulate import tabulate
def Multiple_propotions():
    temp_dat_3 = input(print("Enter the total no.of samples for each item: "))
    a_list_3 = temp_dat_3.split()
    map_object_3 = map(int, a_list_3)
    s3_data = list(map_object_3)
    s3_data.append(sum(s3_data))
    temp_dat_1 = input(print("Enter no.of success data for the distribution: "))
    a_list_1 = temp_dat_1.split()
    map_object = map(int, a_list_1)
    s1_data = list(map_object)
    s1_data.append(sum(s1_data))
    s2_data = []
    lvl = float(input("Enter significance level: "))
    test_tail = int(input("Enter 1 for right tail test \nEnter 2 for left tail test \nEnter 3 for two sided test\n"))
    chi_theory = 0.0
    if test_tail == 3:
        chi_theory = chi2.isf(1 - (lvl / 2),df=len(s3_data)-2)
        chi_t_theory = chi2.isf(lvl/2,df=len(s3_data)-2)
    elif test_tail == 2:
        chi_t_theory = chi2.isf(1-lvl, df=len(s3_data)-2)
    else:
        chi_t_theory = chi2.isf(lvl, df=len(s3_data)-2)
    for j in range(0,len(s3_data)):
        s2_data.append(s3_data[j] - s1_data[j])
    print(tabulate([s1_data,s2_data,s3_data]))
    exp = [[],[]]
    chi = 0.0
    for i in range(0,2):
        for j in range(0,len(s3_data)-1):
            if i ==0:
                exp[i].append(s1_data[3]*s3_data[j]/s3_data[3])
            else:
                exp[i].append(s2_data[3] * s3_data[j] / s3_data[3])
    print(exp)
    for i in range(0,2):
        if i == 0:
            for j in range(0,len(s3_data)-1):
                chi = chi + ((s1_data[j] - exp[i][j])**2)/exp[i][j]
        else:
            for j in range(0,len(s3_data)-1):
                chi = chi + ((s2_data[j] - exp[i][j])**2)/exp[i][j]
    print(f"Chi square calculated = {chi_t_theory}")
    checker_chi_f(chi, chi_t_theory, chi_theory,test_tail)
