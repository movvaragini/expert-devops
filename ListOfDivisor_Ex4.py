'''Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)'''

# First Method
'''def main():
	num = input("Enter divisor:")
	num_mod=abs(int(float(num)))
	divisor = get_divisor(num_mod)
	for ele in divisor:
		print(ele)
	
def get_divisor(n):
	div = []
	count = 1
	while count <= n:
		if n % count == 0:
			div.append(count)
		count += 1
	return div

if __name__ == "__main__":
	main() '''
	
# Second Method
def main():
	num = int(input("Enter Number:"))
	listRange = list(range(1, num+1))
	div = []
	for ele in listRange:
		if num % ele == 0:
			div.append(ele)
	#print(ele)
	print(div)
			

if __name__ == "__main__":
	main()