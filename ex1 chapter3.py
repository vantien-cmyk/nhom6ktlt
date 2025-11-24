print("Exercise 1")
H=float(input("Enter Hours: "))
R=float(input("Enter Rate: "))
if H>40:
    pay=40*R+(H-40)*R*1.5
else:
    pay=H*R
print("Enter Hours:", H)
print("Enter Rate:", R)
print("Pay:", pay)