import sys, string, re, os, fileinput

def readIn():
  lines = sys.stdin.read()
	one_line = ''
	for line in lines:
		one_line += line.rstrip()
	return one_line

def printOut(c, ind):
	if c == ';':
		sys.stdout.write(c)
		sys.stdout.write('\n')
		sys.stdout.write(ind)
	elif c == '{':
		sys.stdout.write(c)
		sys.stdout.write('\n')
		sys.stdout.write(ind)
	elif c == '}':
		sys.stdout.write('\n')
		sys.stdout.write(ind)
		sys.stdout.write(c)
		sys.stdout.write('\n')
		sys.stdout.write(ind)
	elif c == ',':
		sys.stdout.write(c)
		sys.stdout.write(' ')
	else:
		sys.stdout.write(c)

def main():
	line = readIn()
	
	indent = ""
	lenIndent = 0
	inParen = False
	for c in line:
		# Add 4 spaces indent
		if c == '"':
			if inParen:
				inParen = False
			else:
				inParen = True
		if c == '{':
			sys.stdout.write('\n') 
			sys.stdout.write(indent)
			indent = indent + "    "
			lenIndent = lenIndent + 4
		# Remove 4 spaces indent
		if c == '}' and lenIndent > 0:
			indent = indent[:lenIndent-4]
			lenIndent = lenIndent-4
		if inParen:
			sys.stdout.write(c)
		else:
			printOut(c, indent)

main()
