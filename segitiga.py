# program dasar Segitiga
import numpy as np

a = eval (input ("Masukan bilangan A : "))
b = eval (input ("masukan bilangan B : "))
c = eval (input ("Masukan bilangan C : "))

z = [a,b,c]

if a < 0 or b < 0 or c < 0 or (max(z) >= sum(np.sort(z)[:-1])):
    print("segitiga tidak dapat dibangun")
elif type(a) is float or type(b) is float or type(c) is float:
    print("Segitiga sama sisi")
elif np.square(max(z)) == sum(np.square(np.sort(z)[:-1])):
    print('Segitiga Siku-Siku')
elif len(np.unique(z)) == 2:
    print('Segitiga Sama Kaki')
elif len(np.unique(z)) == 1:
    print("Segitiga Sama Sisi")
elif max(z) < sum(np.sort(z)[:-1]):
    print("Segitiga Bebas")
