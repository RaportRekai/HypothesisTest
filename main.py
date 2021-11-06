
from independence_test import independence_test
from two_propotion_test import two_propotion_test
from t_z import t_z_calculate
from two_independent_small import two_independent_small
from one_varience import one_varience
from two_varience import two_varience
from Propotion import Propotion
from Multiple_propotions import Multiple_propotions
from Goodness import Goodness

choice = int(input("Enter your choice \n 1.Z and T test on one mean \n 2. Z and T test on 2 means \n 3. Test on one "
                   "varience \n 4. Test on two varience \n 5. Z test for single propotion \n 6. Multiple proportiom "
                   "\n 7. 2 propotion comparison, \n 8. Independence test \n 9. Goodness test\n "))
if choice == 1:
    t_z_calculate()
if choice == 2:
    two_independent_small()
if choice == 3:
    one_varience()
if choice == 4:
    two_varience()
if choice == 5:
    Propotion()
if choice == 6:
    Multiple_propotions()
if choice == 7:
    two_propotion_test()
if choice == 8:
    independence_test()
if choice == 9:
    Goodness()

