__author__ = 'TriNguyenDang'
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

class Object:
    p = None
    T = None
    W = None
    E = None
    W_0 = None

    def __init__(self,W0,TMax,p):
        self.W = [0  for x in range(TMax + 1)]
        self.W_0 = W0
        self.E = [W0]
        self.T = TMax
        self.p = p


    def Expectation(self):
        t = 1
        while(t <= self.T):
            self.E.append(self.E[t-1] +(2*self.p - 1))
            t+=1


    def Calculate(self):
        self.W[0] = self.W_0
        t = 1
        while(t <= self.T) and(self.W[t-1]>0):
            self.W[t] =  self.W[t-1] + 2 * bernoulli.rvs(self.p) - 1
            t+=1


    #function to get index of W(t)
    def __getitem__(self, item):
        return self.W[item]


    def __setitem__(self, key, value):
        self.W[key] = self.W[key] + value

    #find point where wealth became 0
    def Poin(self):
        i = self.T
        while(i>=0)and(self.W[i]<=0):
            i-=1
        return i


    def MakeDetail(self):

        index = self.Poin()
        plt.annotate('Wealth('+str(index)+')='+str(self.W[index]), xy=(index,self[index]),  xycoords='data',xytext=(-100, 30), textcoords='offset points',arrowprops=dict(arrowstyle="->"))


    def Draw(self,Color,Times):

        plt.plot(self.W,color = Color, lw = 2, label = 'J = '+str(Times))



    def DrawE(self):

        plt.plot(self.E,color = 'black', lw = 3, label = 'Expectation')


    def __add__(self, other):
        for i in range(self.T + 1):
            self.W[i] = self.W[i] + other.W[i]
        return self

    def CalculateAverage(self,Times):
        for i in range(self.T + 1):
            self.W[i] = 1.0* self.W[i]/ Times


    #Print result on terminal
    def __str__(self):
        return 'p = %s\nTMax = %s\nW[0..Tmax] = %s\nE[0..TMax] = %s\n'%(self.p,self.T,self.W,self.E)


def Calculate(Times,Color):
    i = 1
    AVG = Object(W0 = 20, TMax = 500, p = 0.51)
    while(i <= Times):
        A = Object(W0 = 20, TMax = 500, p = 0.51)
        A.Calculate()
        AVG = AVG + A
        i+=1
    AVG.CalculateAverage(Times)
    AVG.Draw(Color,Times)
    AVG.MakeDetail()
    if(Times >= 200):
        AVG.Expectation()
        AVG.DrawE()


Calculate(5,'red')
Calculate(15,'blue')
Calculate(50,'purple')
Calculate(200,'magenta')

plt.grid(True)
plt.legend(loc = 0)
plt.xlabel('bet index(t)')
plt.ylabel('wealth(in $)')
plt.show()







