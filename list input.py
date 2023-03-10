n = input("Enter a text of number to do addition : ")
list = n.split()
sum = 0

for num in list:
     sum = sum + int (num)
print(sum)

n = input("Enter a text of number to do multiplication : ")
list = n.split()
Multiply = 1

for num in list:
     Multiply = Multiply * int (num)
print(Multiply)