#python 2.7.6

print"Hello, Dcoder!"

def producto(num_a, num_b):
	if(num_b==0):
		return 0
	else:
		return num_a + producto(num_a, num_b-1)

def fibonacci(num):
	if num==1 or num==2:
		return 1
	else:
		return fibonacci(num-1) + fibonacci(num-2)
	
	
print producto(3,2)

print fibonacci(6)