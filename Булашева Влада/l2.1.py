a = int(input("Введите номер вашего места:"))
if a%2==0 and a<=36:
    print("Ваше место верхнее")
elif a%2!=0 and a<=36:
    print("Ваше место нижнее")
elif a%2 == 0 and a > 36 and a <= 54:
    print("Ваше место боковое сверху")
else:
    print("Ваше место боковое снизу")