from random import randint as rand
from random import random as rndbl
from math import exp
import matplotlib.pyplot as plt

inf = '∞'
outputText = ""

def outputFile():
    with open("output.txt", "w", encoding='utf-8') as file:
        file.write(outputText)

def prints(string=""):
    global outputText
    outputText+="\n{0}".format(str(string))
    print(string)

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
    prints("Исходная матрица: ")
    for row in mat:
        prints(row)
    prints()

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
        T = [800,1200,1800]
        K = [0.5,0.6,0.7,0.8,0.9]
        L = 500
        s = generate_random_solution(n)
        s0 = list(s)
        colors = ['r','g','b']
        for t0 in T:
            solves = list()
            for k0 in K:
                t,k = t0,k0
                prints("t = {0}, k = {1}".format(t,k))
                prints("Исходное решение: \ns = {0}, f(s) = {1}".format(s, f(matrix, s)))
                step = 1
                while t>k:                  
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
                    t*=k
                prints("Лучшее решение\ns = {0}; f(s) = {1}\nЗавершено на итерации номер {2} при t = {3}\n".format(s, f(matrix,s),step, round(t,3)))
                solves.append(f(matrix, s))
                s = s0  
            plt.plot(K,solves, label='T={0}'.format(t0),color=colors.pop())   
        plt.legend()
        plt.xlabel("k", fontsize=14, fontweight="bold")
        plt.ylabel("f(s)", fontsize=14, fontweight="bold")
        outputFile()
        plt.show()

main()
