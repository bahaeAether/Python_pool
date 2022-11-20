import sys

def isnum(s):
	i = 0
	while i < len(s):
		if s[i] < '0' or s[i] > '9':
			return False
		i += 1
	return True

if len(sys.argv) == 2 and isnum(sys.argv[1]) == True and not (int(sys.argv[1]) == 0 and len(sys.argv[1]) == 1):
	data = int(sys.argv[1])
	if data == 0:
		print("I'm Zero.")
	elif data % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")