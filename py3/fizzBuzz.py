# fizzBuzz.py by Jigsy (https://github.com/Jigsy1) released under the Unlicense.

for thisLoop in range(1, 101):
	# `-> Start at 1, end at 100.
	if thisLoop % 5 == 0 and thisLoop % 3 == 0:
		print("Fizz Buzz")
		continue
	if thisLoop % 5 == 0:
		print("Buzz")
		continue
	if thisLoop % 3 == 0:
		print("Fizz")
		continue
	print(thisLoop)

# EOF