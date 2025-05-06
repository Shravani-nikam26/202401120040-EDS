def fib(n,a=0,b=1):
	if n==0:
		return a 
	else:
		return fib(n-1,b,a+b)

n=int(input("Enter terms for Fibonacci series: "))
for i in range (n):
      print(fib(i),end=" ")
