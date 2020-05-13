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
        x = input("Выберите действие:\n1. Ввести матрицу самостоятельно\n2. Сгенерировать автоматически\nпо умолчанию. Выход\nВаш выбор: ")
        if x=='1':
            auto = False
        elif x=='2':
            auto = True
        else:
            break
        n = int(input("Введите размер матрицы: "))
        matrix = generate_symmetric_matrix(n, auto)
        printMat(matrix)
        T = [800,900,1000]
        K = [0.5,0.6,0.7]
        llist = [800,900,1000]
        s = generate_random_solution(n)
        for t0 in T:
            for k0 in K:
                for L0 in llist:
                    t,k,L = t0,k0,L0
                    print("Исходное решение: \ns = {0}, f(s) = {1}\nИсходная t = {2}\nКоэффициент понижения k = {3}\n".format(s, f(matrix, s), t, k))
                    step = 1
                    while t>k:
                        print("Итерация {2}\ns = {0}, f(s) = {1}".format(s, f(matrix, s), step))
                        step+=1
                        for i in range(L):
                            s1 = swap_in_list(s)
                            delta = f(matrix, s1) - f(matrix, s)
                            if delta<=0:                
                                s = s1     
                            else:
                                r = rndbl()
                                p =exp(-delta/t)
                                if r<p:
                                    s=s1     
                        print("s' = {0}, f(s) = {1}\n".format(s, f(matrix, s)))           
                        t*=k
                print("Оптимальное решение\ns = {0}; f(s) = {1}\nЗавершено на итерации номер {2} при T = {3}\n".format(s, f(matrix,s),step, round(t,3)))

main()