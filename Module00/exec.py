import sys

def rev_case(data):
	i = 0
	while i < len(data):
		if data[i] >= 'a' and data[i] <= 'z':
			data = data[:i] + data[i].upper() + data[i + 1:]
		elif data[i] >= 'A' and data[i] <= 'Z':
			data = data[:i] + data[i].lower() + data[i + 1:]
		i += 1
	return data

data = ''
if len(sys.argv) > 1:
	data = ' '.join(sys.argv[1:])
	data = data[::-1]
	data = rev_case(data)
	print(data)
