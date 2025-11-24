try:
    s = float(input("Enter Score: "))
except ValueError:
    #thử nhập value mình là 1 số nếu là chữ thì nó sẽ cho là s=2 ngoại phạm vì thì sẽ thực hiện lệnh if n
    s = 2.0
print("Score:", s)
if not (0.0 <= s <= 1.0):
    print("Bad score")
elif s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
else:
    print("F")