
def operator(choose):
    if choose == '1':
        oper = 'KS'
    elif choose == '2':
        oper = 'VF'
    elif choose == '3':
        oper = 'LC'
    else:
        return print('Incorrect operator')

    return oper


operator_1 = input("""
Choosen your operator:
1) KS
2) VF
3) LC
""")
operator(operator_1)

operator_2 = input("""
Choosen abonent's operator:
1) KS
2) VF
3) LC
""")
operator(operator_2)

prise = int(input("Enter prise: "))
time = int(input("Enter call time: "))
cost = prise*time
print("Call from ", operator_1, " to ", operator_2, "costs: ", cost)
