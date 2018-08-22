#Q.1- Create a function to calculate the area of a sphere by taking radius from user.

def sq(n):
    return (4*3.14*n*n)
n=int(input("enter radius"))
x=sq(n)
print(x)

#Q.2- Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. 
#[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3].

def perfect(n):
    sum1 = 0
    for i in range(1, n):
        if(n % i == 0):
            sum1 = sum1 + i
            if (sum1 == n):
                print("The number is a Perfect number!",n)
for j in range(1,1000):
    perfect(j)

#Q.3- Print multiplication table of n using loops, where n is an integer and is taken as input from the user.

n = int(input("Input a number: "))
for i in range(1,11):
   print(n,'x',i,'=',n*i)

#Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.

def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base"))
exp=int(input("Enter exponential value"))
print(power(base,exp))

