#Papa Kwame Twumasi-Ntiamoah
#Student ID: 37352022

#Assignment 1

#This program provides solutions to a quadratic equation.
#Letters, a, b and c will be the values of the coefficients.
#Two values given will represent the final answer of the quadratic formula.

import math
#this code makes the math library available.

def main():
    print("Welcome to Quick Quadratic Math Solver \nThis program finds solutions to a quadratic equation")
#this describes what the program is about    
    
    a= float(input(" Enter your coefficient a: "))
    b= float(input(" Enter your coefficient b: "))
    c= float(input(" Enter your coefficient c: "))
#these inputs are the values of the coefficients
    
    formula = math.sqrt(b * b - 4 * a * c)
    numerator = (-b + formula)/ (2 * a)
    denomenator = (-b - formula)/ (2 * a)
#these inputs are the represent the quadratic formula
    
    ans= round(numerator, 2), round(denomenator,2)
#after deriving the answer, it was rounded up to two decimal places.
    
    print("The solution to your question is=", ans)

    
main()
#this calls the program to run
