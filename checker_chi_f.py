def checker_chi_f(Z_t_observe, Z_t_theory,Z_theory, test_tail):
    if test_tail == 1:
        if Z_t_observe > Z_t_theory:
            print(f"The observer value of Z is {Z_t_observe}\n")
            print("Alternative Hypothesis Is True")
        if Z_t_observe < Z_t_theory:
            print(f"The observer value of Z is {Z_t_observe}\n")
            print("Null Hypothesis Is True")

    if test_tail == 2:
        if Z_t_observe < -Z_t_theory:
            print(f"The observer value of Z is {Z_t_observe} \n")
            print("Alternative Hypothesis Is True")
        if Z_t_observe > -Z_t_theory:
            print(f"The observer value of Z is {Z_t_observe}\n")
            print("Null Hypothesis Is True")

    if test_tail == 3:
        if Z_t_observe > Z_t_theory or Z_t_observe < Z_theory:
            print(f"The observer value of Z is {Z_t_observe}\n")
            print("Alternative Hypothesis Is True")
        else:
            print(f"The observer value of Z is {Z_t_observe}\n")
            print("Null Hypothesis Is True")