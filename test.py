def are_all_conditions_true(conditions):
    if len(conditions) != 0:
        for i in conditions:
            if i == False:
                a = False
            else:
                a = False
    else:
        a = None
    return a

a1 = [True, True, False, True, False, False, True]
a2 = [True, True, True]
a3 = []
a4 = [False, True, None, None]

print(are_all_conditions_true(a4))