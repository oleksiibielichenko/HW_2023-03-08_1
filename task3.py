
def operator(choose):
    if choose == '1':
        return 'KS'
    elif choose == '2':
        return 'VF'
    elif choose == '3':
        return 'LC'
    else:
        return print('Incorrect operator')


operator_1 = input("""
Choose your operator:
1) KS
2) VF
3) LC
""")
oper_1 = operator(operator_1)

operator_2 = input("""
Choose abonent's operator:
1) KS
2) VF
3) LC
""")
oper_2 = operator(operator_2)

prise = int(input("Enter prise: "))
time = int(input("Enter call time: "))
cost = prise*time
print("Call from ", oper_1, " to ", oper_2, "costs: ", cost)
