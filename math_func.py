
# factorial of a number
def fact(no):
	if no==0:
		return 1

	return(no*fact(no-1))

#print(fact(5)) 

# fibonacci sequence generator
def recur_fibo(num):  
   if num <= 1:
   	return num  
   else:
   	return(recur_fibo(num-1) + recur_fibo(num-2)) 

def fibocalc(terms):
	for item in range(0,terms):
		print(recur_fibo(item))
#fibocalc(5)

# Greatest common divisor using recurrsive functions
def gcd(a, b): 

	if (a == 0): 
		return b 
	return gcd(b % a, a) 
#print(gcd(5,16))

# Euler Totient Function 
def phicalc(x): 
	result = 1
	for i in range(2, x): 
		if (gcd(i, x) == 1): 
			result+=1
	return result 

 
def phi(x1): # Driver function for totient
	for n in range(x1): 
		print(phicalc(n))
#phi(6)

# Divisors of a no 

def divisor(value):
	for dv in range(1,value+1):
		if(value%dv== 0):
			print(dv)

#divisor(25400)

# Sum of divisors of a number
def div_sum(divs):
	arr=[];
	for div in range(1,divs+1):
		if(divs%div==0):
			arr.append(div)
	print(sum(arr))
#div_sum(10)
