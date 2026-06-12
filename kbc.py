print("Welcome to KBC")

l = [['''1. What is the correct way to import NumPy?
A. import numpy
B. import numpy as np
C. import np as numpy
D. include numpy''','B'],
     ['''2. Which function creates an array of zeros?
A. np.empty()
B. np.ones()
C. np.zeros()
D. np.array()''','C'],
     ['''3. Which attribute gives the total number of elements in a NumPy array?
A. shape
B. size
C. dtype
D. ndim''','B'],
     ['''4. Which NumPy function is used to create an array with evenly spaced values within a specified interval?
A. zeros()
B. arange()
C. reshape()
D. append()''','B'],
     ['''5. Which attribute returns the number of dimensions (axes) of a NumPy array?
A. size
B. shape
C. ndim
D. dtype''','C']]

price =[1000,2000,3000,4000,5000]
won=0
for i in range(0,len(l)):
    print(l[i][0])
    x=str(input("enter option"))
    if x==l[i][1]:
        won+=1
    else:
        print("WRONG ANSWER you won ",price[i-1])
        break
if won==len(l):
    print("You are crorepati")