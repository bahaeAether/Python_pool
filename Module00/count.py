import sys
import string

def is_punc(c):
	if c in string.punctuation:
		return True
	return False

def text_analyzer(data = None):
	if not data:
		data = input('What is the text to analyze?\n')
	up = 0
	low = 0
	sp = 0
	pm = 0
	for c in data:
		if c != c.lower():
			up += 1
		if c != c.upper():
			low += 1
		if is_punc(c):
			pm += 1
		if c == ' ':
			sp += 1
	print("The text contains {} character(s):".format(len(data)))
	print("- {} upper letter(s)".format(up))
	print("- {} lower letter(s)".format(low))
	print("- {} punctuation mark(s)".format(pm))
	print("- {} space(s)".format(sp))

text_analyzer()