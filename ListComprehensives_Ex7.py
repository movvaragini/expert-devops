''' Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.'''

def main():
	a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	'''b = [element for element in a if element % 2 == 0]
	print('---b----:') 
	print(b)
	print(a)
	c = [ele for ele in a if ele % 2 != 0]
	print('------c-----:')
	print(c)
	print(a) '''
	e= [elem for elem in a if a.index(elem) % 2 == 0]
	print('------e-------:')
	print(e)
	print(a)
	
if __name__ == "__main__":
	main()