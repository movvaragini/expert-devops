'''Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

Hint: how does an even / odd number react differently when divided by 2?
Extras:

1.If the number is a multiple of 4, print out a different message.
2.Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
  If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''

import sys
def main():
	num= input('Enter number:')
	check = input('Enter Second number:')
	num_mod = int(float(num))
	check_mod = int(float(check))
	if (num_mod % 2) == 0:
		print('It is Even Number')
	else:
		print('Its Odd number')
		
	if (num_mod % 4) == 0:
		print('Given number is divided by 4')
    
	
	if check_mod == 0:
		print('Zero is not allowed as denominator')
		sys.exit()
	else:
		#out_mod = num_mod % check_mod
		if num_mod % check_mod == 0:
			print('{} divisible'.format(check_mod,num_mod))
		else:
			print('{} not divisible'.format(check_mod,num_mod))
		
if __name__ == "__main__":
	main()