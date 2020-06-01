# --------------
import pandas as pd
import numpy as np
import math

#Code starts here
class complex_numbers:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
        #return(self.real,'+' if self.imag>=0 else '-', abs(self.imag))
        print(self.real,'+',self.imag,'i')


    
    def __add__(self,other):
        x=self.real+other.real
        y=self.imag+other.imag
        return complex_numbers(x,y)

    def __sub__(self,other):
        x=self.real-other.real
        y=self.imag-other.imag
        return complex_numbers(x,y)    

    def __mul__(self,other):
        x=(self.real*other.real)-(self.imag*other.imag)
        y=(self.imag*other.real)+(self.real*other.imag)
        return complex_numbers(x,y)    

    def __truediv__(self,other):
        x=(self.real*other.real+self.imag*other.imag)/(pow(other.real,2)+pow(other.imag,2))
        y=(self.imag*other.real-self.real*other.imag)/(pow(other.real,2)+pow(other.imag,2))
        return complex_numbers(x,y)    
    
    def absolute(self):
        x=math.sqrt(pow(self.real,2)+pow(self.imag,2))
        return x    
    
    def argument(self):
        x=math.degrees(math.atan(self.imag/self.real))
        return round(x,2)                
    
    def conjugate(self):
        x=self.real
        y=-self.imag
        return complex_numbers(x,y)

comp_1=complex_numbers(3,5)
comp_2=complex_numbers(4,4)
comp_sum=comp_1+comp_2
comp_diff=comp_1-comp_2
comp_prod=comp_1*comp_2
comp_quot=comp_1/comp_2
comp_abs=comp_1.absolute()
print(comp_abs)
comp_arg=comp_1.argument()
print(comp_arg)
comp_conj=comp_1.conjugate()
print(comp_conj)





