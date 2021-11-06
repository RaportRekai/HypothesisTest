from scipy.stats import norm, poisson, chi2
from prettytable import PrettyTable


def Goodness():
    x = PrettyTable()
    mean = float(input("Enter the mean to be compared with: "))
    temp_dat = input("Enter data : ")
    a_list = temp_dat.split()
    map_object = map(float, a_list)
    dat = list(map_object)
    temp_freq = input("Enter the corresponding frequencies : ")
    a_list = temp_freq.split()
    map_object = map(float, a_list)
    freq = list(map_object)
    s = 0
    poi = []
    exp = []
    choice = int(input("Enter 1 to compare with poisson \nEnter 2 to compare with normal distribution\n"))
    lvl = float(input("Enter significance level: "))
    if choice == 1:
        for i in range(0, len(dat)):
            poi.append(round(poisson.pmf(dat[i], mean), 4))
            exp.append(round(poi[i] * sum(freq), 4))
    if choice == 2:
        var = input(float("Enter the Varience of the data: "))
        for i in range(0, len(dat)):
            poi.append(round(norm.pdf(dat[i], loc=mean, scale=var ** 0.5), 4))
            exp.append(round(poi[i] * sum(freq), 4))

    fre = [x for x in freq]
    ex = [x for x in exp]
    s1 = 0
    s2 = 0
    for i in range(0, len(freq)):
        if s1 == 0 and freq[i] < 5:
            index = i
        if s1 < 5:
            s1 = s1 + freq[i]
            s2 = s2 + exp[i]
            exp[i] = 0
            freq[i] = 0
        if s1 >= 5:
            exp[i] = s2
            freq[i] = s1
            s1 = 0
            s2 = 0
        if i == len(freq) - 1 and s1 < 5:
            s1 = s1 + freq[index - 1]
            s2 = s2 + exp[index - 1]
            exp[index - 1] = s2
            freq[index - 1] = s1
    x.add_column("Data", dat)
    x.add_column("Frequency obs", fre)
    x.add_column("modified Frequency obs", freq)
    x.add_column("Poisson/Normal", poi)
    x.add_column("Expected", ex)
    x.add_column("Expected modified", exp)
    print(x)
    chi = 0.0
    count = 0
    for i in range(0, len(freq)):
        if not freq[i] == 0:
            chi = chi + (freq[i] - exp[i]) ** 2 / exp[i]
            count = count + 1
    print(f"Chi2 theory is: {chi2.isf(lvl, df=count - 1)}")
    print(f"Chi2 observed is: {chi}")
    if chi2.isf(lvl, df=count - 1) < chi:
        print("The samples are dependent")
    else:
        print("The samples are independent")
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13
# 3 15 47 76 68 74 46 39 15 9 5 2 0 1
