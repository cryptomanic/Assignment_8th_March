'''
class Integrate:
	def solve(self,order,coeff,method):
		def f(x):
			s=0
			for i in range(order+1):
				s=s+(coeff[i]*(x**(order-i)))
			return s
		if method=='trapezoid':
			a=float(input('Lower limit: '))
			b=float(input('Upper limit: '))
			n=int((b-a)/0.001)
			x_values=[a]
			for i in range(1,n):
				x_values.append(float(str(x_values[0]+(0.001*i))[:5]))
			x_values.append(b)
			def trapezoid_sol(f,x_values,n):
				s=0
				for i in range(1,n):
					s=s+f(x_values[i])
				s=s*2
				s=s+(f(x_values[0])+f(x_values[n]))
				ans=((x_values[n]-x_values[0])*s)/(2*n)
				return ans
			return trapezoid_sol(f,x_values,n)
		elif method=='simpson':
			a=float(input('Lower limit: '))
			b=float(input('Upper limit: '))
			n=int((b-a)/0.0005)
			x_values=[a]
			for i in range(1,n):
				x_values.append(float(str(x_values[0]+(0.0005*i)[:5]))
			x_values.append(b)
			def simpson_sol(f,x_values,n):
				s1=0
				s2=0
				s3=0
				for i in range(1,n,2):
					s1+=f(x_values[i])
				s1*=4
				for i in range(2,n,2):
					s2+=f(x_values[i])
				s2*=2
				s=s+(f(x_values[0])+f(x_values[n])+s1+s2)
				ans=((x_values[n]-x_values[0])*s)/(3*n)
				return ans
			return simpson_sol(f,x_values,n)
'''
import numpy as np
import  matplotlib.pyplot as plt
class Integrate:
    rec_wid, f = 0.0, ''
    X_initial, X_final, sum = 0.0, 0.0, 0.0 
    Llimit, Ulimit = 0, 0
    def TrapezoidalRule(self, f, Llimit, Ulimit, nop):
        self.f = f
        self.Llimit = Llimit
        self.Ulimit = Ulimit
        self.rec_wid = (Ulimit-Llimit)/(nop*1.0)
        self.X_initial = Llimit
        self.X_final = Llimit + self.rec_wid
        self.plot_the_curve()
        for i in range(nop):
           self.plot_trapezium()
           self.sum += 0.5*self.rec_wid*(f(self.X_initial)+f(self.X_final)) 
           self.X_initial = self.X_final
           self.X_final += self.rec_wid
        plt.show() 
        return self.sum  
    def plot_the_curve(self):   
        my_arr = np.arange(self.Llimit-1.0,self.Ulimit+1.0,10**(-4))
        plt.plot(my_arr,self.f(my_arr),color = 'red', linewidth = 2.0)
    def plot_trapezium(self):
        plt.fill_between([self.X_initial, self.X_final],
        [self.f(self.X_initial), self.f(self.X_final)])
