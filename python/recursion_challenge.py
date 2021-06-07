def factorial(x):
	if x == 1:
		return 1
	return x * factorial(x - 1)

def palindrome(string):
	# same spelling forwards and backwards
	pass

def bottles(num):
	if num == 2:
		print(f'{num} bottles of beer on the wall - take one and pass it around - {num - 1} bottle of beer on the wall')
		return bottles(num - 1)
	if num == 1:
		print(f'{num} bottle of beer on the wall - take one and pass it around - no more bottles of beer on the wall')
		return bottles(num - 1)
	if num == 0:
		print(f'No more bottles of beer on the wall - buy some more - 99 bottles of beer on the wall')
	else:
		print(f'{num} bottles of beer on the wall - take one and pass it around - {num - 1} bottles of beer on the wall')
		return bottles(num - 1)

def roman_num(num):
	# arabic to roman numerals
	pass