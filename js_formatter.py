import sys, string, re, os, fileinput

def printOut(c, ind):
	if c == ';':
		sys.stdout.write(c)
		print
		sys.stdout.write(ind)
	elif c == '{':
		sys.stdout.write(c)
		print
		sys.stdout.write(ind)
	elif c == '}':
		print
		sys.stdout.write(ind)
		sys.stdout.write(c)
		print
		sys.stdout.write(ind)
	else:
		sys.stdout.write(c)

def main():
		line = sys.stdin.read()
		
		indent = ""
		lenIndent = 0
		for c in line:
			# Add 4 spaces indent
			if c == '{':
				print 
				sys.stdout.write(indent)
				indent = indent + "    "
				lenIndent = lenIndent + 4
			# Remove 4 spaces indent
			if c == '}' and lenIndent > 0:
				indent = indent[:lenIndent-4]
				lenIndent = lenIndent-4
			printOut(c, indent)
			
				
		
		print 
		print "=+=+=+=+ Finish +=+=+=+="
main()
