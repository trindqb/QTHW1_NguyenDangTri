__author__ = 'TriNguyenDang'
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

class Object:
    p = None
    T = None
    W = None
    def __init__(self,W0,TMax,p):
        self.W = [W0]
        self.T = TMax
        self.p = p
        #Calculate for every t in TMax
        #save by array W where W[0] = W0
        #W(t) = W[t]
        t = 1
        while(t <= self.T):
            if(self.W[t - 1] > 0):
                tmp =  self.W[t-1] + 2 * bernoulli.rvs(self.p) - 1
                if(tmp >= 0):
                    self.W.append(tmp)

                else:
                    self.W.append(0)
            else:
                self.W.append(0)
            t+=1
    def Calculate(self):
        t = 1
        while(t <= self.T):
            if(self.W[t - 1] > 0):
                tmp =  self.W[t-1] + 2 * bernoulli.rvs(self.p) - 1
                if(tmp >= 0):
                    self.W.append(tmp)

                else:
                    self.W.append(0)
            else:
                self.W.append(0)
            t+=1

    #function to get index of W(t)
    def __getitem__(self, item):
        return self.W[item]

    #find point where wealth became 0
    def Poin(self):
        i = 0
        while(i<=self.T)and(self.W[i]>0):
            i+=1
        return i

    def MakeDetail(self):
        # make a pointer to show lasted wealth or where player lose
        if(self.Poin() > self.T):
            plt.annotate('W(TMax) ='+str(self[-1]), xy=(self.T,self[-1]),  xycoords='data',xytext=(-100, 30), textcoords='offset points',arrowprops=dict(arrowstyle="->"))
        else:
            plt.annotate('t = '+str(self.Poin()), xy=(self.Poin(),self[self.Poin()]),  xycoords='data',xytext=(-50, 30), textcoords='offset points',arrowprops=dict(arrowstyle="->"))
    #Plot line
    def Draw(self,Color):
        x = np.arange(len(self.W))
        plt.plot(x,self.W,color = Color, lw = 3,label = 'J = '+str(self.W[0]))

    #Print result on terminal
    def __str__(self):
        return 'p = %s\nTMax = %s\nW[0..Tmax] = %s\n'%(self.p,self.T,self.W)

A = Object(5,500,0.51)
B = Object(15,500,0.51)
C = Object(50,500,0.51)
D = Object(200,500,0.51)

avg = []
for i in range(D.T):
    avg.append((A[i]+B[i]+C[i]+D[i])/4)
x = np.arange(len(avg))
plt.plot(x,avg,color = 'green',lw =3,label = 'avg')

A.Draw('blue')
B.Draw('red')
C.Draw('magenta')
D.Draw('purple')
A.MakeDetail()
B.MakeDetail()
C.MakeDetail()
D.MakeDetail()


#plt.axis([-5,501,-5,401])

plt.grid(True)
plt.legend(loc = 0)
plt.xlabel('bet index(t)')
plt.ylabel('wealth(in $)')
plt.show()

