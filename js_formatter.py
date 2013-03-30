import sys, string, re, os, fileinput

def main():
  	line = sys.stdin.read()
		
		yes = False
		indent = ""
		lenIndent = 0
		for c in line:
			if c == ';':
				yes = True
			# Add 4 spaces indent
			if c == '{':
				yes = True
				indent = indent + "    "
				lenIndent = 4
				print 
				sys.stdout.write(indent)
			# Remove 4 spaces indent
			if c == '}' and lenIndent > 0:
				print 'hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
				indent = indent[:lenIndent-4]
				lenIndent = lenIndent-4
			sys.stdout.write(c)
			if yes == True:
				print
				sys.stdout.write(indent)
				yes = False
		
		print 
		print "=+=+=+=+ Finish +=+=+=+="
main()
