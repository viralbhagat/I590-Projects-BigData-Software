import sys

def fizzbuzz(n):
	number = 1
	while (number <= n):
		if number%2 == 0 and number%3 == 0:
			print ('fizzbuzz')
		elif number%2 == 0:
			print ('fizz')
		elif number%3 == 0:
			print ('buzz')
		else:
			print (number)
		number+=1

fizzbuzz(int(sys.argv[1]))