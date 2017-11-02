'''
Ex 1:
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
Extras:
(1) Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
(2) Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''
from datetime import date
def main():
	name= input("Enter name:")
	print("Hello!!!"+name)
	age=input("Enter age:")
	print("Now you are "+age)
	bday_yet = birthday_yet()
	year = get_year(int(age), bday_yet)
	if year=='greater':
		print('You are 100 years old')
	else:
		print('Hello, {}!'.format(name))
		print('you wll turn 100 in the year {}.'.format(year))
def birthday_yet():
	ans = input('Have you had your birthday yet this year (y/n)?')
	if 'y' in ans.lower():
		return True
	else:
		return False		
def get_year(a, b):
	assert a >= 0, "Age is not allowed to be less than zero."
	if a >= 100:
		return 'greater'
	else:
		today = str(date.today()).split('-')
		#print('today:'+today)
		if bool(b) == True:
			this_year = int(today[0])
			#print('this_year:'+this_year)
			return (this_year + (100 - a))
		else:
			this_year = int(today[0])
			#print('this_year2:'+this_year)
			return (this_year + (99 - a))
		   
if __name__ == "__main__":
	main()