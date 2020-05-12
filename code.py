from random import randint as rand
from random import random as rndbl
from math import exp

inf = '∞'

def swap_in_list(lr):
    l = list(lr)
    n = len(l) - 2
    first, second = 0, 0
    while True:
        first = rand(1, n)
        second = rand(1, n)
        if first!=second:
            break
    print("Меняем местами {0} и {1}".format(l[first],l[second]))
    temp = l[first] 
    l[first] = l[second]
    l[second] = temp
    return l

def printMat(mat):
    print("\nИсходная матрица: ")
    for i in mat:
        print(i)
    print()

def f(matrix, solution):
    sum = 0
    for i in range(len(solution)-1):
        sum+=matrix[solution[i]-1][solution[i+1]-1]
    return sum

def generate_random_solution(n):
    setw = list(range(2,n+1))
    solution = [1]
    while len(setw)!=0:
        index = rand(0,len(setw)-1)
        elem = setw[index]
        setw.remove(setw[index])
        solution.append(elem)
    solution.append(1)
    return solution

def generate_symmetric_matrix(n, auto=True):
    maxrandom = 10
    matrix = list()
    for i in range(n):
        row = list()
        for j in range(n):
            if i==j:
                row.append(inf)
            elif i>j:
                row.append(matrix[j][i])
            else:
                a = 0
                if auto:
                    a = rand(1, maxrandom)
                else:
                    a = int(input("расстояние {0} - {1}: ".format(i+1,j+1)))
                row.append(a)
        matrix.append(row)
    return matrix


def main():
    while True:
        x = int(input("Выберите действие:\n1. Ввести матрицу самостоятельно\n2. Сгенерировать автоматически\nпо умолчанию. Выход\nВаш выбор: "))
        if x==1:
            auto = False
        elif x==2:
            auto = True
        else:
            break
        n = int(input("Введите размер матрицы: "))
        matrix = generate_symmetric_matrix(n, auto)
        printMat(matrix)
        t = input("Введите t (оставьте поле пустым для t = 1000): ")
        K = input("Введите k (оставьте поле пустым для k = 0.7: ")
        if t == '':
            T = 1000
        else:
            T = int(t)
        if K == '':
            k = 0.7
        else:
            k = float(K)
        s = generate_random_solution(n)
        print("Исходное решение: \ns = {0}, f(s) = {1}\nИсходная t = {2}\nКоэффициент понижения k = {3}\n".format(s, f(matrix, s), T, k))
        step = 1
        while T>k:
            print("Итерация {2}\ns = {0}, f(s) = {1}".format(s, f(matrix, s), step))
            step+=1
            s1 = swap_in_list(s)
            print("s' = {0}, f(s') = {1}".format(s1, f(matrix, s1)))
            delta = f(matrix, s1) - f(matrix, s)
            print("delta = {0} - {1} = {2}".format(f(matrix, s1), f(matrix, s), delta))
            if delta<=0:                
                s = s1 
                print("delta <= 0\nновое решение s = {0}, f(s) = {1}".format(s, f(matrix, s)))      
            else:
                r = rndbl()
                p =exp(-delta/T)
                print("delta > 0\nr = {0}, exp(-delta/T) = {1}".format(round(r,3), round(p,3)))
                if r<p:
                    s=s1
                    print("r<exp(-delta/T)\nновое решение s = {0}, f(s) = {1}".format(s, f(matrix, s)))
                else:
                    print("r>exp(-delta/T)\nРешение не изменилось")
                    
            T*=k
            print("новая t = {0}\n".format(round(T,3)))
        print("Оптимальное решение\ns = {0}; f(s) = {1}\n".format(s, f(matrix,s)))

main()