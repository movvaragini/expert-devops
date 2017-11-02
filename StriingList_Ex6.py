'''Ask the user for a string and print out whether this string is a palindrome or not.
 (A palindrome is a string that reads the same forwards and backwards.) '''
 
def main():
	word= input('Enter a string:')
	word_lower = (word.strip()).lower()
	str = word_lower[::-1]
	if str==word_lower:
		print('Palindrome:'+str + word_lower)
	else:
		print('Not palindrome:'+str + word_lower)

if __name__ == "__main__":
	main()