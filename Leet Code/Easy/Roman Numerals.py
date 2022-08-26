num_romans = {
	"I": 1,
	"V": 5,
	"X": 10,
	"L": 50,
	"C": 100,
	"D": 500,
	"M": 1000
}

def romanToInt(num):
	collider = 0
	i = 0

	while i < len(num):
		s1 = num_romans[num[i]]

		if i+1 < len(num):
			s2 = num_romans[num[i+1]]
			if s1 >= s2:
				collider += s1
				i += 1
			else:
				collider -= s1
				i += 1

		else:
			collider += s1
			i += 1
	return collider

num = str(input('Enter a number \nr: ')).upper()
print('')
print('{}'.format(romanToInt(num)))
