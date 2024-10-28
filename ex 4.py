summa=0
max=min=int(input("Vvedit chislo: "))
while True:
    num=int(input("Vvedit chislo: "))
    if num==7:
        print("Good bye")
        break
    summa+=num
    if num>max:
        max=num
    if num<min:
        min=num
print("Suma",summa)
print("maximum",max)
print("Minimum",min)
