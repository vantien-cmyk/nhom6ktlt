print("Exercise 2")
try: #thử thực hiện đoạn code bên dưới
    H=float(input("Enter Hours: "))
    R=float(input("Enter Rate: "))
    if H>40:
        pay=40*R+(H-40)*R*1.5
    else:
        pay=H*R
    print("Enter Hours:", H)
    print("Enter Rate:", R)
except ValueError:
    print("Erorr, please enter numeric input.")