#Задача №2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N. 

number = int(input())
list=[]
def number_factors(ls, n):
    for i in range(1, n+1):
        if n%i == 0:
            ls.insert((i-1), i)         
    return(ls)
number_factors(list, number)

print("Простыми множителями числа", number, "являются:", " ".join(map(str, list)))
