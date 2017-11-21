def is_palindrome(number_string):
	if len(number_string) == 1:
		return True

	half = int(len(number_string)/2)

	if len(number_string) % 2: # odd number  
		if number_string[0:half] == ''.join(reversed(number_string[half+1:])):
			return True
	else: # even number
		if number_string[0:half] == ''.join(reversed(number_string[half:])):
			return True
	
	return False


def get_base(base, number):
	nums = []
	while number:
		number, r = divmod(number, base)
		nums.append(str(r))
	return ''.join(reversed(nums))


def main():
	with open('palindrome_answers.csv', 'w+') as fi:
		fi.write('decimal, smallest base in which the number is a palindrome\n')
		for i in range(1, 1001):
			is_pal = False
			counter = 2
			while not is_pal:
				is_pal = is_palindrome(get_base(counter, i))
				if is_pal:
					line = '%s, %s\n' % (i, counter)
					fi.write(line)
				counter += 1


main()